#%%
from keras import activations, layers
from keras.backend import dropout
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as img
import glob
import os

from sklearn.model_selection import train_test_split
from keras.models import Model, Sequential
from keras.datasets import fashion_mnist,cifar10
from keras.layers import Dense,Dropout,Activation,Conv2D,Flatten,MaxPool2D,BatchNormalization,AveragePooling2D
from keras.utils import np_utils
from keras.callbacks import EarlyStopping,TensorBoard

import tensorflow as tf
from tensorflow.python.eager import monitoring
from datetime import datetime

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


# Sequential layers 
with tf.device('/device:GPU:0'):

    model = Sequential([
        Conv2D(64,kernel_size=(3,3),padding='same',input_shape=(480,640,3),kernel_initializer='he_normal',activation='elu'),
        Conv2D(64,kernel_size=(4,4),padding='same',kernel_initializer='he_uniform',activation='elu'),
        MaxPool2D(pool_size=(4,4)),
        BatchNormalization(),

        Dropout(.5),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu'),
        Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        AveragePooling2D(pool_size=(3,3)),
        BatchNormalization(),

        Dropout(.4),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        AveragePooling2D(pool_size=(3,3)),
        BatchNormalization(),

        Dropout(.5),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        AveragePooling2D(pool_size=(3,3)), 
        BatchNormalization(),

        Dropout(.5),
        Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_uniform',activation='elu'),
        MaxPool2D(pool_size=(4,4)), 
        BatchNormalization(),

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
    epochs = 2000
    batch_size = 6
    model.compile(
        loss = 'categorical_crossentropy',
        optimizer='adam', 
        metrics=['accuracy']
        )
    model.fit(
        X_train,
        y_train,
        epochs = epochs,
        batch_size=batch_size,
        validation_data=(X_test,y_test),
        callbacks = [
            EarlyStopping(monitor='val_loss' ,patience=10)
            ]
        )


#%%
# API

