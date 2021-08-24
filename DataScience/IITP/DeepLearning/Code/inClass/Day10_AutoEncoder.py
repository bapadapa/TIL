"""
AutoEncoder 구현
"""
#%%
from http.client import responses
from keras.datasets import mnist,cifar100,fashion_mnist
from keras.models import Input,Model,Sequential
from keras.layers import Dense
from keras import losses
from keras import optimizers
from numpy.core.fromnumeric import reshape
from tensorflow import keras 
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras import activations
from tensorflow.python.keras.layers.convolutional import Conv2D
from tensorflow.python.keras.layers.core import Flatten, Reshape
from keras.layers import Conv2DTranspose

#%%
# plt를 이용한 시각화
def mnist_visualize(x_test,decoded_imgs):
    n = 10  # How many digits we will display
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # Display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(x_test[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # Display reconstruction
        ax = plt.subplot(2, n, i + 1 + n)
        plt.imshow(decoded_imgs[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()

(X_train,Y_train),(X_test,Y_test) = mnist.load_data()
x_train = X_train.reshape(-1,28*28)/255
x_test = X_test.reshape(-1,28*28)/255
x_train =  x_train.astype(np.float32)
x_test =  x_test.astype(np.float32)
latent_dim = 32

# %%
input_ = Input(shape=x_train.shape[1:])
encoded = Dense(latent_dim,activation='relu')(input_)
decoded = Dense(x_train.shape[1],activation='sigmoid')(encoded)
autoencoder = Model(inputs=[input_],outputs=[decoded])

encoder = Model(inputs=[input_], outputs=[encoded])
encoded_input = Input(shape=(latent_dim,))
decoder_layer = autoencoder.layers[-1]
decoder = Model(inputs=[encoded_input], outputs=[decoder_layer(encoded_input)])

# %%
autoencoder.compile(
    loss = 'binary_crossentropy',
    optimizer = keras.optimizers.Adam(learning_rate= 1e-5)

)
autoencoder.summary()
with tf.device("/device:gpu:0"):
    autoencoder.fit(
        x = x_train,
        y = x_train,
        epochs=100,
        batch_size=256,
        shuffle=True, 
        validation_data=(x_train,x_train)
        )
encoded_imgs = encoder.predict(x_train)
decoded_imgs = decoder.predict(encoded_imgs)
#%%
mnist_visualize(x_test,decoded_imgs)

#%%
#Class로 만들어보기
class Autoencoder(Model):
    def __init__(self,latent_dim,decoder_dim):
        super(Autoencoder,self).__init__()        
        self.encoder = Sequential(
            [
                Dense(latent_dim,activation='relu')
            ]
        )
        self.decoder = Sequential(
            [
                Dense(decoder_dim,activation='sigmoid',name = 'decoder')
            ]
        )
    def call(self,x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded


#%%
latent_dim = 32
autoencoder = Autoencoder(    
    latent_dim=latent_dim,
    decoder_dim = x_train.shape[1])

autoencoder.compile(
    loss = 'binary_crossentropy',
    optimizer = keras.optimizers.Adam(learning_rate= 1e-5)

)
#%%
with tf.device("/device:gpu:0"):
    autoencoder.fit(
        x_train,
        x_train,
        epochs=300,
        batch_size=256,
        shuffle=True,
        validation_data=(x_train,x_train))
#%%
encoded_imgs = autoencoder.encoder(x_test).numpy()
decoded_imgs = autoencoder.decoder(encoded_imgs).numpy()
mnist_visualize(x_test,decoded_imgs)

#%%

class Ae(Model):
    def __init__(
        self ,
        latent_dim,
        decoder_dim,
        
        ):
        super(Ae,self).__init__()    
        self.encoder = Sequential([
            Flatten(),
            Dense(latent_dim , activation='elu')
        ])
        self.decoder = Sequential([
            Dense(decoder_dim,activation='sigmoid'),

        ])
    def call(self,x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded 

#%%
(X_train,Y_train),(X_test,Y_train) = cifar100.load_data()
X_train = (X_train.reshape(-1,32*32*3)/255).astype(np.float32)
X_test = (X_test.reshape(-1,32*32*3)/255).astype(np.float32)



#%%
model = Ae(
    latent_dim = 128,
    decoder_dim = 32*32*3
    )
model.compile(
    loss = "mean_absolute_error",
    optimizer = optimizers.Adam(1e-3)
)
with tf.device("/device:gpu:0"):
    model.fit(
        X_train,
        X_train,
        epochs=300,
        batch_size=256,
        validation_data=(X_train,X_train))


# %%
encoded_imgs = model.encoder(X_test).numpy()
decoded_imgs = model.decoder(encoded_imgs).numpy()
# mnist_visualize(X_train,decoded_imgs)


n = 10  # How many digits we will display
plt.figure(figsize=(20, 4))
for i in range(n):
    # Display original
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(X_test[i].reshape(32,32,3))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    # Display reconstruction
    ax = plt.subplot(2, n, i + 1 + n)
    plt.imshow(decoded_imgs[i].reshape(32,32,3))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
plt.show()
# %%

#%%
(X_train,Y_train),(X_test,Y_train) = fashion_mnist.load_data()


noise = 0.2
X_train_noisy = X_train + noise *np.random.normal(size = X_train.shape)
X_test_noisy = X_test + noise *np.random.normal(size =  X_test.shape)
X_train_noisy = np.clip(X_train_noisy,0.,1.).reshape(60000,28,28,1)/255
X_test_noisy = np.clip(X_test_noisy,0.,1.).reshape(10000,28,28,1)/255

#%%
class RemoveNoisy(Model):
    def __init__(self):
        super(RemoveNoisy,self).__init__()
        self.encoder = Sequential([            
            Input(shape  = (28,28,1)),
            Conv2D(
                32,
                kernel_size = (3,3),
                padding = 'same',
                activation = 'elu',                
            ),
            Conv2D(
                16, 
                kernel_size = (3,3),
                padding = 'same',
                activation = 'elu',                
            )

        ])
        self.decoder = Sequential([
            Conv2DTranspose(
                16,
                kernel_size = 3,
                padding = 'same',
                activation = 'elu'
            ),
            Conv2DTranspose(
                32,
                kernel_size = 3,
                padding = 'same',
                activation = 'elu'
            ),
            Conv2D(
                1,
                kernel_size = (3,3),
                padding = 'same',
                activation =  'sigmoid'
                )
        ])
    def call(self,x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded 


#%%

model = RemoveNoisy()

model.compile(
    loss = 'binary_crossentropy',
    optimizer = keras.optimizers.Adam(learning_rate= 1e-5)
)
with tf.device("/device:gpu:0"):
    model.fit(
        X_train_noisy,
        X_train_noisy,
        epochs=10,
        batch_size=256,
        shuffle=True,
        validation_data=(X_train_noisy,X_train_noisy))
#%%
model.summary()
#%%
encoded_imgs = model.encoder(X_test_noisy).numpy()
decoded_imgs = model.decoder(encoded_imgs).numpy()
mnist_visualize(x_test,decoded_imgs)

#%%
class RemoveNoisy(Model):
    def __init__(self):
        super(RemoveNoisy,self).__init__()
        self.encoder = Sequential([            
            Input(shape  = (28,28,1)),
            Conv2D(
                32,
                kernel_size = (3,3),
                strides = 2,
                padding = 'same',
                activation = 'elu',                
            ),
            Conv2D(
                16, 
                kernel_size = (3,3),
                strides = 2,
                padding = 'same',
                activation = 'elu',                
            ), 

        ])
        self.decoder = Sequential([
            
            Conv2DTranspose(
                16,
                kernel_size = 3,
                strides = 2,
                padding = 'same',
                activation = 'elu'
            ),

            Conv2DTranspose(
                32,
                kernel_size = 3,
                strides = 2,
                padding = 'same',
                activation = 'elu'
            ),
            Conv2D(
                1,
                kernel_size = (1,1),
                padding = 'same',
                activation =  'sigmoid'
                )
        ])
    def call(self,x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded 

# %%
