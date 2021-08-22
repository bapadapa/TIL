#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as img
import glob
import os

from sklearn.model_selection import train_test_split
import keras

from keras.models import Model, Sequential,load_model
from keras.datasets import fashion_mnist,cifar10
from keras.layers import Dense,Dropout,Activation,Conv2D,Flatten,MaxPool2D,BatchNormalization,AveragePooling2D,Input
from keras.utils import np_utils
from keras.callbacks import EarlyStopping,TensorBoard,LambdaCallback,ModelCheckpoint
from keras.applications import ResNet50


import tensorflow as tf
from tensorflow.python.eager import monitoring
from datetime import datetime
#%%
path = "../../data/HeadSample/원천데이터/1.미세각질/"
path0 = f'{path}0.양호/'
path1 = f'{path}1.경증/'
path2 = f'{path}2.중증도/'
path3 = f'{path}3.중증/'
file_list0 = glob.glob(path0+'*.jpg')
file_list1 = glob.glob(path1+'*.jpg')
file_list2 = glob.glob(path2+'*.jpg')
file_list3 = glob.glob(path3+'*.jpg')
file_list = []
file_list.extend(file_list0)
file_list.extend(file_list1)
file_list.extend(file_list2)
file_list.extend(file_list3)
data = []
for file in file_list:
    tmp = img.imread(file)
    data.append(tmp)
data = np.concatenate(data).reshape(len(data),480,640,3)
y0 = [0]*len(file_list0)
y1 = [1]*len(file_list1)
y2 = [2]*len(file_list2)
y3 = [3]*len(file_list3)
y = []
y.extend(y0)
y.extend(y1)
y.extend(y2)
y.extend(y3)
X = data.copy()
y = np_utils.to_categorical(y)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
# tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)
#%%
# Sequential layers 
model = Sequential([
    Conv2D(32,kernel_size=(3,3),padding='same',input_shape=(480,640,3),kernel_initializer='he_normal',activation='elu'),
    Conv2D(32,kernel_size=(4,4),padding='same',kernel_initializer='he_uniform',activation='elu'),
    MaxPool2D(pool_size=(2,2)),
    BatchNormalization(),
    Dropout(.5),
    Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    AveragePooling2D(pool_size=(2,2)),
    BatchNormalization(),
    Dropout(.5),
    Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    AveragePooling2D(pool_size=(2,2)),
    BatchNormalization(),
    Dropout(.5),
    Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    AveragePooling2D(pool_size=(2,2)), 
    BatchNormalization(),
    Dropout(.5),
    Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
    MaxPool2D(pool_size=(2,2)), 
    BatchNormalization(),
    Dropout(.5),
    
    Flatten(),
    Dense(
        256,        
        activation = 'elu'
        ),
    Dense(
        256,
        activation = 'elu'
    ),
    Dense(
        64,
        activation = 'elu'
    ),
    Dense(
        y_train.shape[1],
        activation = 'softmax'
    )
])
model.summary()
# compile

epochs = 300

batch_size = 8

with tf.device('/device:GPU:0'):
    model.compile(
        loss = 'categorical_crossentropy',
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-6), 
        metrics=['accuracy']
        )
    model.fit(
        X_train,
        y_train,
        epochs = epochs,
        batch_size=batch_size,
        validation_data=(X_test,y_test),
        callbacks = [
            EarlyStopping(monitor='val_loss' , mode='auto', verbose=1,patience=100)
            ]
        )
        

#%%

log_dir = "logs/fit/" + datetime.now().strftime("%Y%m%d-%H%M%S")
with tf.device('/device:GPU:0'):
    model.fit(
        X_train,
        y_train,
        epochs = epochs,
        batch_size=batch_size,
        validation_data=(X_test,y_test),
        callbacks = [
            EarlyStopping(monitor='val_loss' , mode='max', verbose=1, patience=10),
            TensorBoard(log_dir=log_dir, histogram_freq=1)
            ]
        )
        


#%%

def headSkin_predict(
    input_shape,
    output_shape,
    init ='he_uniform',   
    ):
    model = Sequential([
        Conv2D(
            32,
            kernel_size= (3,3),
            input_shape = input_shape,
            kernel_initializer = init,
            activation= 'elu'
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
        Dropout(.2),

        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),        
        Dropout(.2),

        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Dropout(.2),

        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        BatchNormalization(),
        
        Dropout(.2),

        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        MaxPool2D(pool_size=(2,2)), 
        BatchNormalization(),
        Dropout(.5),

        Flatten(),
        Dense(
            64,        
            activation = 'swish'
            ),
        Dense(
            64,
            activation = 'swish'
        ),
        Dense(
            32,
            activation = 'elu'
        ),
        Dense(
            output_shape,
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
    return model
def modelFitting(
    model,
    x_train,
    y_train,
    x_val,
    y_val,    
    epoch = 100,
    batch_size = 64,
    callbacks = [],
    validation_split=.2,
    ):
    with tf.device('/device:GPU:0'):
        model.fit(
            x = x_train,
            y = y_train,
            epochs= epoch,
            batch_size= batch_size,
            validation_data= (x_val,y_val),
            validation_split=validation_split,
            callbacks =callbacks
        )
    model = load_model('cifar100_model.h5')
    return model
#%%
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

model = headSkin_predict(
    input_shape = X_train.shape[1:],
    output_shape = y_train.shape[1],    
    init ='he_uniform',   
    )
#%%
epoch = 100
batch_size = 1
modelFitting(
    model = model,
    x_train= X_train,
    y_train= y_train,
    x_val =X_test,
    y_val = y_test,
    epoch = epoch,
    batch_size= batch_size,
    validation_split=.2,
    callbacks =model_callback

)