"""
RESNET을 구동시켜 보고 싶었지만, 하드웨어 기능이 부족하여 실행은 못함
"""
#%%
import numpy as np
import pandas as pd

import glob
import os
import matplotlib.image as img

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from keras.models import Sequential
from keras.layers import Dense,Conv2D,Concatenate,AveragePooling2D,BatchNormalization,MaxPooling2D,Flatten

from keras.utils import np_utils
from keras.models import Input
from keras import optimizers
from keras import Model
import keras
import tensorflow as tf

#%%
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
# %%
data = fetch_california_housing()
scaler =  StandardScaler()

X = scaler.fit_transform(data.data)
y = data.target
X_train, X_test, Y_train,Y_test = train_test_split(X,y,test_size=.2)

model = Sequential([
    Dense(
        256,
        input_dim = X_train.shape[1],
        activation= 'elu',
        kernel_initializer = 'he_normal',
        ),
    
    Dense( 128, activation = 'elu',),
    
    Dense( 64, activation = 'elu',),
    
    
    Dense(1),
    
])
model.summary() 
model.compile(
    loss = keras.losses.mean_squared_error,    
    optimizer = 'adam',
    metrics=['accuracy']
)
#%%
model.fit(
    x=  X_train,
    y = Y_train,
    epochs = 30,
    batch_size=10,
    validation_data=(X_test,Y_test)
)
#%%
# tensor 쌓기
# API 사용
from keras.models import Input
from keras import  Model
from keras.layers import Concatenate

input_ = Input((8,))
h1 = Dense(64,activation='relu')(input_)
h2 = Dense(32,activation='relu')(h1)
h3 = Dense(16,activation='relu')(h2)
con1 = Concatenate()([h3,input_])
output = Dense(1,activation='linear')(con1)
model = Model(inputs = [input_],outputs = [output])

model.summary()
model.compile(
    loss = keras.losses.mean_squared_error,    
    optimizer = 'adam',
    metrics=['accuracy']
)
model.fit(
    x=  X_train,
    y = Y_train,
    epochs = 30,
    batch_size=10,
    validation_data=(X_test,Y_test)
)

#%%
# RESNET 을 이용하여 두피데이터 예측
# 

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

del(file_list,file_list0,file_list1,file_list2,file_list3,path,path0,path1,path2,path3,data,y0,y1,y2,y3,y,X)
X_train, X_test = X_train/255, X_test/255 

input_ = Input((480,640,3))
cv_1 = Conv2D(64,kernel_size=(7,7),padding='same',kernel_initializer='he_normal',activation='elu')(input_)
nomal_1 = BatchNormalization()(cv_1)
pool_1 = MaxPooling2D(pool_size=(10,10))(nomal_1)
# 64 * 2 * 3
cv_2 = Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(pool_1)
cv_3 = Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_2)
con_1 = Concatenate()([pool_1,cv_3])
nomal_2 = BatchNormalization()(con_1)
pool_2 = MaxPooling2D(pool_size=(10,10))(nomal_2)

cv_4 = Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(pool_2)
cv_5 = Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_4)
con_2 = Concatenate()([pool_2,cv_5])

nomal_3 = BatchNormalization()(con_2)
pool_3 = MaxPooling2D(pool_size=(10,10))(nomal_3)


cv_6 = Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(pool_3)
cv_7 = Conv2D(64,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_6)
con_3 = Concatenate()([con_2,cv_7])

# 128 * 2 * 4
cv_8 = Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_3)
cv_9 = Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_8)
con_4 = Concatenate()([con_3,cv_9])

cv_10 = Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_4)
cv_11 = Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_10)
con_5 = Concatenate()([con_4,cv_11])

cv_12 = Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_5)
cv_13 = Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_12)
con_6 = Concatenate()([con_5,cv_13])

cv_14 = Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_6)
cv_15 = Conv2D(128,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_14)
con_7 = Concatenate()([con_6,cv_15])

# 256 *2 * 6
cv_16 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_7)
cv_17 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_16)
con_8 = Concatenate()([con_7,cv_17])

cv_18 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_8)
cv_19 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_18)
con_9 = Concatenate()([con_8,cv_19])

cv_20 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_9)
cv_21 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_20)
con_10 = Concatenate()([con_9,cv_21])

cv_22 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_10)
cv_23 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_22)
con_11 = Concatenate()([con_10,cv_23])

cv_24 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_11)
cv_25 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_24)
con_12 = Concatenate()([con_11,cv_25])

cv_26 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_12)
cv_27 = Conv2D(256,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_26)
con_13 = Concatenate()([con_12,cv_27])
# 512 * 2 * 3

# cv_28 = Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_13)
# cv_29 = Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_28)
# con_14 = Concatenate()([con_13,cv_29])

# cv_30 = Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_14)
# cv_31 = Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_30)
# con_15 = Concatenate()([con_14,cv_31])

# cv_32 = Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(con_15)
# cv_33 = Conv2D(512,kernel_size=(3,3),padding='same',kernel_initializer='he_normal',activation='elu')(cv_32)
# con_16 = Concatenate()([con_15,cv_33])
 
Pool = AveragePooling2D(pool_size=(10,10))(con_13)
# Pool_2 = AveragePooling2D(pool_size=(8,8))(con_16)

flat_1 = Flatten()(Pool)
h1 = Dense(256,activation= 'relu')(flat_1)

output = Dense(y_train.shape[1],activation='softmax')(h1)
model = Model(inputs = [input_],outputs = [output])
model.summary()

with tf.device('/device:GPU:0'):



    model.compile(
        loss = 'categorical_crossentropy',    
        optimizer = keras.optimizers.adam(learning_rate = 1e-6),
        metrics=['accuracy']
    )

    model.fit(
        x = X_train,
        y = y_train,
        epochs = 30,
        batch_size=10,
        validation_data=(X_test,y_train)
    )
#%%
