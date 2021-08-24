#%%
import keras
from keras.layers import Conv2D,MaxPooling2D,Activation,Flatten,Dense,BatchNormalization,Reshape,UpSampling2D,LeakyReLU,Dropout,Conv2DTranspose
from keras.optimizers import SGD,Adam
from keras.models import Sequential
import tensorflow as tf

import numpy as np



#%%
class unKnown():
    def discriminator_model():
        model = Sequential()
        model.add(Conv2D(64, (5, 5), padding='same', input_shape=self.input_shape))
        model.add(Activation('tanh'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Conv2D(128, (5, 5)))
        model.add(Activation('tanh'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Flatten())
        model.add(Dense(1024))
        model.add(Activation('tanh'))
        model.add(Dense(1))
        model.add(Activation('sigmoid'))
        return model

    def generator_model():
        model = Sequential()
        model.add(Dense(input_dim=100, units=1024))
        model.add(Activation('tanh'))
        model.add(Dense(128*7*7))
        model.add(BatchNormalization())
        model.add(Activation('tanh'))
        model.add(Reshape((7, 7, 128), input_shape=(128*7*7,)))
        model.add(UpSampling2D(size=(2, 2)))
        model.add(Conv2D(64, (5, 5), padding='same'))
        model.add(Activation('tanh'))
        model.add(UpSampling2D(size=(2, 2)))
        model.add(Conv2D(1, (5, 5), padding='same'))
        model.add(Activation('tanh'))
        return model

    def build_model(g, d):
        model = Sequential()
        model.add(g)
        d.trainable = False
        model.add(d)
        return model

    def train(X_train, y_train, X_test, y_test, epochs=100, batch_size=32):
        d_optimizer = SGD(lr=0.0005, momentum=0.9, nesterov=True)
        g_optimizer = SGD(lr=0.0005, momentum=0.9, nesterov=True)
        self.generator.compile(loss='binary_crossentropy', optimizer="SGD")
        self.gan.compile(loss='binary_crossentropy', optimizer=g_optimizer)
        self.discriminator.trainable = True
        self.discriminator.compile(loss='binary_crossentropy', optimizer=d_optimizer)
        for epoch in range(1,epochs):
            print("Epoch {}".format(epoch))
            for index in range(int(X_train.shape[0]/batch_size)):
                image_batch = X_train[index*batch_size:(index+1) * batch_size]
                rand_vector = np.random.uniform(-1, 1, size=(batch_size, 100))
                generated_images = self.generator.predict(rand_vector, verbose=0)
                X = np.concatenate((image_batch, generated_images))
                y = [1] * batch_size + [0] * batch_size
                d_loss = self.discriminator.train_on_batch(X, y)
                rand_vector = np.random.uniform(-1, 1, (batch_size,  100))
                self.discriminator.trainable = False
                g_loss = self.gan.train_on_batch(rand_vector, [1] * batch_size)
                self.discriminator.trainable = True
                print("\rbatch {} d loss: {} g loss: {}".format(index, d_loss, g_loss), end="")
                print()

#%%
class Gan:
    def __init__(self, img_data):
        img_size = img_data.shape[1] 
        channel = img_data.shape[3] if len(img_data.shape) >= 4 else 1 
        self.img_data = img_data 
        self.input_shape = (img_size, img_size, channel) 
        self.img_rows = img_size 
        self.img_cols = img_size 
        self.channel = channel 
        self.noise_size = 100 
        # Create D and G.
        self.create_d() 
        self.create_g() 
        # Build model to train D. 
        optimizer = Adam(lr=0.0008) 
        self.D.compile(loss='binary_crossentropy', optimizer=optimizer) 
        # Build model to train G. 
        optimizer = Adam(lr=0.0004) 
        self.D.trainable = False 
        self.AM = Sequential() 
        self.AM.add(self.G) 
        self.AM.add(self.D) 
        self.AM.compile(loss='binary_crossentropy', optimizer=optimizer) 
        
    def create_d(self): 
        self.D = Sequential() 
        depth = 64 
        dropout = 0.4 
        self.D.add(Conv2D(depth*1, 5, strides=2, input_shape=self.input_shape, padding='same')) 
        self.D.add(LeakyReLU(alpha=0.2)) 
        self.D.add(Dropout(dropout)) 
        self.D.add(Conv2D(depth*2, 5, strides=2, padding='same')) 
        self.D.add(LeakyReLU(alpha=0.2)) 
        self.D.add(Dropout(dropout)) 
        self.D.add(Conv2D(depth*4, 5, strides=2, padding='same')) 
        self.D.add(LeakyReLU(alpha=0.2)) 
        self.D.add(Dropout(dropout)) 
        self.D.add(Conv2D(depth*8, 5, strides=1, padding='same')) 
        self.D.add(LeakyReLU(alpha=0.2)) 
        self.D.add(Dropout(dropout)) 
        self.D.add(Flatten()) 
        self.D.add(Dense(1)) 
        self.D.add(Activation('sigmoid')) 
        self.D.summary() 
        return self.D 
    def create_g(self): 
        self.G = Sequential() 
        dropout = 0.4 
        depth = 64+64+64+64 
        dim = 7 
        self.G.add(Dense(dim*dim*depth, input_dim=self.noise_size)) 
        self.G.add(BatchNormalization(momentum=0.9)) 
        self.G.add(Activation('relu')) 
        self.G.add(Reshape((dim, dim, depth))) 
        self.G.add(Dropout(dropout)) 
        self.G.add(UpSampling2D()) 
        self.G.add(Conv2DTranspose(int(depth/2), 5, padding='same')) 
        self.G.add(BatchNormalization(momentum=0.9)) 
        self.G.add(Activation('relu')) 
        self.G.add(UpSampling2D()) 
        self.G.add(Conv2DTranspose(int(depth/4), 5, padding='same')) 
        self.G.add(BatchNormalization(momentum=0.9)) 
        self.G.add(Activation('relu')) 
        self.G.add(Conv2DTranspose(int(depth/8), 5, padding='same')) 
        self.G.add(BatchNormalization(momentum=0.9)) 
        self.G.add(Activation('relu')) 
        self.G.add(Conv2DTranspose(1, 5, padding='same')) 
        self.G.add(Activation('sigmoid')) 
        self.G.summary() 
        return self.G 
    def train(self, batch_size=100): 
        # Pick image data randomly. 
        images_train = self.img_data[np.random.randint(0, self.img_data.shape[0], size=batch_size), :, :, :] 
        # Generate images from noise. 
        noise = np.random.uniform(-1.0, 1.0, size=[batch_size, self.noise_size]) 
        images_fake = self.G.predict(noise) 
        # Train D. 
        x = np.concatenate((images_train, images_fake)) 
        y = np.ones([2*batch_size, 1]) 
        y[batch_size:, :] = 0 
        self.D.trainable = True 
        d_loss = self.D.train_on_batch(x, y) 
        # Train G. 
        y = np.ones([batch_size, 1]) 
        noise = np.random.uniform(-1.0, 1.0, size=[batch_size, self.noise_size]) 
        self.D.trainable = False 
        a_loss = self.AM.train_on_batch(noise, y) 
        return d_loss, a_loss, images_fake
