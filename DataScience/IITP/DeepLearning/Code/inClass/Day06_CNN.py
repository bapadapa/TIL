"""
CNN

"""
#%%

from keras import activations, layers
from keras.backend import dropout
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as img


from sklearn.model_selection import train_test_split
from keras.models import Model, Sequential
from keras.datasets import fashion_mnist,cifar10
from keras.layers import Dense,Dropout,Activation,Conv2D,Flatten,MaxPool2D,BatchNormalization
from keras.utils import np_utils


#%%
# fashion_mnist 데이터 실습
(X_train, Y_train), (X_test,Y_test) = fashion_mnist.load_data()

x_train = X_train.reshape(X_train.shape[0],28,28,1)
x_test = X_test.reshape(X_test.shape[0],28,28,1)

y_train = np_utils.to_categorical(Y_train)
y_test = np_utils.to_categorical(Y_test)

x_train,x_val,y_train,y_val = train_test_split(x_train,y_train,test_size= .7)
epochs = 30
batch_size = 20

class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
    ]


    #%%
model = Sequential([
    Conv2D(
        32,
        kernel_size = (3,3),
        padding = 'same',
        input_shape = (28,28,1),
        kernel_initializer='he_normal',
    ),
    Activation('elu'),
    MaxPool2D(
        pool_size=(2,2)
    ),
    Dropout(.2),
    Conv2D(
        32,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer='he_uniform',
    ),
    Flatten(),    
    Dropout(.2),
    # 연쇄적으로 Shape을 넘겨주기 떄문에 inpush_dim을 작성할 필요가 없다
    Dense(
        256,
        kernel_initializer='he_uniform'
        ),
    Activation ('elu'),
    Dense(
        64,
        kernel_initializer= 'he_normal',
        activation= 'elu'
        ),
    Dense(
        y_train.shape[1]
        ),
    Activation ('softmax')
])
model.summary()
#%%
model.compile(
    optimizer='adam',
    loss= 'categorical_crossentropy',
    metrics=['accuracy']
    )
hist = model.fit(
    x= x_train,
    y= y_train,
    epochs= epochs , 
    batch_size = batch_size,
    validation_data = (x_val,y_val)
    )
#%%

class_names[np.argmax(model.predict(x_train[200:201]))]
class_names[np.argmax(y_train[200:201])]

#%%
# cifar10 데이터 실습
(X_train,Y_train),(X_test,Y_test) = cifar10.load_data()
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

x_train,x_val,y_train,y_val = train_test_split(X_train,Y_train)

model = Sequential([
    Conv2D(
        128,
        kernel_size = (4,4),
        input_shape = (x_train.shape[1],x_train.shape[2],x_train.shape[3]),
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    MaxPool2D(3,3),
    Dropout(.2),
    Conv2D(
        128,
        kernel_size = (3,3),
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Dropout(.2),
    Flatten(),
    Dense(
        128,        
        activation = 'elu'
        ),
    Dense(
        64,
        activation = 'leaky_relu'
    ),

    Dense(
        y_train.shape[1],
        activation = 'softmax'
    )
])
model.summary()
#%%
model.summary()
model.compile(
    optimizer='adam',
    loss = 'categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(
    x = x_train,
    y = y_train,
    epochs= 30,
    batch_size = 64,
    validation_data= (x_val,y_val)

)

#%%
(X_train,Y_train),(X_test,Y_test) = cifar10.load_data()
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

x_train,x_val,y_train,y_val = train_test_split(X_train,Y_train)

model = Sequential([
    Conv2D(
        64,
        kernel_size = (3,3),
        padding = 'same',
        input_shape = (x_train.shape[1],x_train.shape[2],x_train.shape[3]),
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    BatchNormalization(),
    Conv2D(
        64,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    BatchNormalization(),
    MaxPool2D(pool_size = (2,2)),

    Conv2D(
        128,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        128,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    MaxPool2D(pool_size = (2,2)),

    Conv2D(
        256,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        256,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        256,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        256,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    MaxPool2D(pool_size = (2,2)),

    Conv2D(
        512,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        512,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        512,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        512,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    MaxPool2D(pool_size = (2,2)),

    Conv2D(
        512,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        512,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        512,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    Conv2D(
        512,
        kernel_size = (3,3),
        padding = 'same',
        kernel_initializer= 'he_normal',
        activation = 'elu'
    ),
    MaxPool2D(pool_size = (2,2)),


    Flatten(),
    Dense(
        256,        
        activation = 'elu'
        ),
    Dense(
        128,
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
model.compile(
    optimizer='adam',
    loss = 'categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(
    x = x_train,
    y = y_train,
    epochs= 30,
    batch_size = 64,
    validation_data= (x_val,y_val)
)
