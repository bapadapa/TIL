#%%
import numpy as np

from keras.datasets import imdb,mnist,cifar100
from keras.models import Input, Model
from keras.layers import Dense,Conv1D,MaxPool1D,GlobalAveragePooling1D,Flatten,Embedding,MaxPool2D
from keras.utils import np_utils
from keras.preprocessing import sequence
from keras.optimizers import RMSprop
from keras.callbacks import EarlyStopping, ModelCheckpoint
import keras
from numpy.lib.npyio import load
from numpy.matrixlib.defmatrix import matrix


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import callbacks, losses, optimizers
from tensorflow.python.keras import activations
from tensorflow.python.keras.backend import binary_crossentropy, dropout
from tensorflow.python.keras.engine.sequential import Sequential
from tensorflow.python.keras.layers.convolutional import Conv2D
from tensorflow.python.keras.layers.core import Activation, Dropout
from tensorflow.python.keras.layers.normalization import BatchNormalization
from tensorflow.python.keras.layers.pooling import AveragePooling2D
from tensorflow.python.keras.saving.save import load_model

# %%
max_Feature = 10000
max_len = 500
(X_train , Y_train),(X_test,Y_test) = imdb.load_data(num_words= max_Feature)

X_train = sequence.pad_sequences(X_train,max_Feature,padding= 'post').astype(float)
X_test = sequence.pad_sequences(X_test,max_Feature,padding= 'post').astype(float)
#%%
model = Sequential([
    Embedding(max_Feature,128,input_length=max_len),
    Conv1D(32,7,activation = 'relu'),
    MaxPool1D(5),
    Conv1D(32,7,activation='relu'),
    GlobalAveragePooling1D(),
    Dense(1,activation='sigmoid')
])
model.summary()

model.compile(
    loss = "binary_crossentropy",
    optimizer= keras.optimizers.RMSprop(learning_rate= 1e-5),
    metrics= ['acc']
)
with tf.device('/device:GPU:0'):
    model.fit(
        x = X_train,
        y = Y_train,
        epochs= 10,    
        batch_size= 128,
        validation_split=.2
    )




#%%
X = np.random.normal(size = (100,1))
Y = X*3 +4
print(X.shape)
print(Y.shape)

# %%

model = Sequential([
    Dense(64,input_dim = 1,kernel_initializer='he_normal',activation='relu'),
    BatchNormalization(),
    Dense(1)    
])
model.summary()
model.compile(
    loss = 'mse',
    optimizer = 'sgd',
    metrics= ['acc']
)
with tf.device('/device:GPU:0'):
    model.fit(
        x = X,
        y = Y,
        epochs= 1000,
        batch_size= 128,
        validation_split=.2
    ) 
test =  np.array([10,11,12,13])
print(test*3 + 4)
test.reshape(-1,1)
model.predict(test)

# %%


(X_train,Y_train) , (X_test,Y_test) = mnist.load_data() 
X_train = X_train.reshape(X_train.shape[0],-1).astype(np.float32)/255
X_test = X_test.reshape(X_test.shape[0],-1).astype(np.float32)/255
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

print( X_train.shape)
print( Y_train.shape)
print( X_test.shape)
print( Y_test.shape)

#%%
def mnist_predict(
    x_train,
    y_train, 
    x_val,
    y_val,
    input_dim,
    n_classes,
    dropout = .2,
    callback_Func = [],    
    init = 'he_uniform', 
    epochs=10, 
    batch_size=64
    ):

    model = Sequential([
        Dense(
            64,
            input_dim = input_dim,
            activation='relu',
            kernel_initializer= init,            
            ),
        Dropout(dropout),
        Dense(
            128,
            activation = 'relu',
        ),
        Dropout(dropout),    
        Dense(n_classes, activation = 'softmax' )    
    ])
    model.summary()
    model.compile(
        loss = 'CategoricalCrossentropy',
        optimizer = tf.keras.optimizers.Adam(learning_rate= 1e-5),
        metrics= ['accuracy']
    )

    with tf.device('/device:GPU:0'):
        model.fit(
            x =  x_train,
            y =  y_train,
            epochs= epochs,
            batch_size= batch_size,
            validation_data= (x_val, y_val),
            validation_split = 0.2,
            callbacks = callback_Func
        )
    model =load_model('softmax_model.h5')
    return model

# %%

model_chcekpoint = ModelCheckpoint( filepath= './softmax_model.h5',monitor='val_acc',save_best_only=True)
model_EarlyStopping = EarlyStopping(monitor='val_loss' , mode='auto', verbose=1,patience=30)
model_callback = [model_chcekpoint,model_EarlyStopping]
model = mnist_predict(
    x_train = X_train,
    y_train = Y_train, 
    x_val = X_test,
    y_val = Y_test,
    dropout = 0.5,
    input_dim = X_train.shape[1],
    n_classes = Y_train.shape[1],
    callback_Func = model_chcekpoint,
    init = 'he_uniform', 
    epochs=100, 
    batch_size=64
    )



#%%
#cifar100 함수로 구현
def cifar100_predict(
    x_train,
    y_train,
    x_val,
    y_val,
    input_shape,
    output_shape,
    epoch = 100,
    batch_size = 64,
    callbacks = [],
    init ='he_uniform',   
    ):
    model = Sequential([
        Conv2D(
            32,
            kernel_size= (3,3),
            input_shape = input_shape,
            kernel_initializer = init,
            activation= 'swish'
        ),
        Conv2D(
            32,
            kernel_size= (3,3),
            input_shape = input_shape,
            kernel_initializer = init,
            activation= 'elu'
        ),
        AveragePooling2D( 2,2 ),
        BatchNormalization(),        
        # Dropout(.2),

        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),        
        # Dropout(.2),

        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        # Dropout(.2),

        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        # Dropout(.2),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        # Dropout(.2),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        # Dropout(.2),

        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        MaxPool2D(pool_size=(2,2)), 
        BatchNormalization(),
        # Dropout(.5),

        Flatten(),
        Dense(
            512,        
            activation = 'swish'
            ),
        Dense(
            512,
            activation = 'swish'
        ),
        Dense(
            64,
            activation = 'elu'
        ),
        Dense(
            y_train.shape[1],
            activation = 'softmax'
        )
        ]
    )
    model.summary()
    model.compile(
        loss = 'CategoricalCrossentropy',
        optimizer = keras.optimizers.Adamax(learning_rate=1e-5),
        metrics = ['accuracy'],
    )
    with tf.device('/device:GPU:0'):
        model.fit(
            x = x_train,
            y = y_train,
            epochs= epoch,
            batch_size= batch_size,
            validation_data= (x_val,y_val),
            validation_split=.2,
            callbacks =callbacks
        )
    model = load_model('cifar100_model.h5')
    return model

#%%
(X_train,Y_train) , (X_test,Y_test) = cifar100.load_data() 
x_train = X_train.astype(np.float32)/255
x_test = X_train.astype(np.float32)/255
y_train =np_utils.to_categorical(Y_train)
y_test =np_utils.to_categorical(Y_test)

cp = ModelCheckpoint(
    filepath= './cifar100_model.h5',
    monitor='val_acc',
    save_best_only=True)
es = EarlyStopping(
    monitor= 'val_loss',
    mode = 'max',
    verbose= 1,
    patience= 50
)
model_callback = [cp,es]

model = cifar100_predict(
    x_train = X_train,
    y_train = y_train,
    x_val = X_test,
    y_val = y_test,
    input_shape = X_train.shape[1:],
    output_shape = Y_train.shape[1],
    epoch = 100,
    batch_size = 128,
    callbacks = model_callback,
    init ='he_uniform',   
    )
#%%
print( X_train.shape)
print( Y_train.shape)
print( X_test.shape)
print( Y_test.shape)
#%%

# %%
