""""
1. 케라스를 이용하여 지금까지 배운것을 적용시켜보기
2. cifir-10데이터를 이용해서 실습해보기 

"""
#%%
from keras.layers.core import Dropout
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
import matplotlib.pyplot as plt

(X_train, Y_train), (X_test,Y_test) = mnist.load_data()
X_train = X_train.reshape(X_train.shape[0],-1).astype(np.float32)/255
X_test = X_test.reshape(X_test.shape[0],-1).astype(np.float32)/255
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

x_train, x_val,y_train, y_val = train_test_split(X_train,Y_train,test_size=.2)

model = Sequential([
    
    Dense(1024,input_dim = x_train.shape[1],
        activation='relu',kernel_initializer='he_uniform'),
    Dense(512,activation='relu'),
    Dropout(.2),
    Dense(256,activation='relu'),
    Dropout(.2),
    Dense(64,activation='relu'),
    Dense(y_train.shape[1],activation='softmax')
])

print(model.summary())

model.compile(
    optimizer='adamDelta',
    loss= 'categorical_crossentropy',
    metrics=['accuracy']
    )
hist = model.fit(
    x= x_train,
    y= y_train,
    epochs= 100 , 
    batch_size = 64,
    validation_data = (x_val,y_val)
    )
    
plt.plot(np.arange(100),hist.history['val_loss'],'r')
plt.plot(np.arange(100),hist.history['loss'])
plt.plot(np.arange(100),hist.history['accuracy'])
plt.show()


# %%

# cifar10 실습해보기
import numpy as np
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Dropout,Conv2D,MaxPool2D
from keras.datasets import mnist,cifar10
from sklearn.model_selection import train_test_split

(X_train, Y_train), (X_test,Y_test) = cifar10.load_data()

X_train = X_train.reshape(X_train.shape[0],-1).astype(np.float32)/255
X_test = X_test.reshape(X_test.shape[0],-1).astype(np.float32)/255

Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

x_train, x_val,y_train, y_val = train_test_split(X_train,Y_train,test_size=.2)

# 모델 생성하기
model = Sequential([    
    Dense(1024,input_dim = x_train.shape[1],
        activation='LeakyReLU',kernel_initializer='he_uniform'),
    Dropout(.3),
    Dense(512,activation='relu'),
    Dropout(.2),
    Dense(256,activation='elu'),
    Dropout(.1),
    Dense(64,activation='relu'),
    Dense(y_train.shape[1],activation='softmax')
]) 

print(model.summary())

# 컴파일 하기
model.compile(
    optimizer='adam',
    loss= 'categorical_crossentropy',
    metrics=['accuracy']
    )

# fit, 훈련시키기
hist = model.fit(
    x= x_train,
    y= y_train,
    epochs= 100 , 
    batch_size = 64,
    validation_data = (x_val,y_val)
    )
    