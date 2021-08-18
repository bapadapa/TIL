(X_train, Y_train), (X_test,Y_test) = cifar10.load_data()

X_train = X_train.reshape(X_train.shape[0],-1).astype(np.float32)/255
X_test = X_test.reshape(X_test.shape[0],-1).astype(np.float32)/255

Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)

x_train, x_val,y_train, y_val = train_test_split(X_train,Y_train,test_size=.2)

# 모델 생성하기

model = Sequential([    
    Dense(1024,input_dim = x_train.shape[1],
        activation='elu',kernel_initializer='he_uniform'),
    Dropout(.5),
    Dense(512,activation='selu'),
    Dropout(.3),
    Dense(256,activation='relu'),
    Dropout(.2),
    Dense(64,activation='LeakyReLU'),
    Dense(y_train.shape[1],activation='softmax')
]) 

print(model.summary())

model.compile(
    optimizer='adam',
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
#%%

from math import e
import matplotlib
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.ops.array_ops import one_hot
from tensorflow.python.ops.gen_array_ops import shape
from tensorflow.python.ops.gen_math_ops import cos, sqrt
from tensorflow.python.ops.gen_string_ops import encode_base64
from tensorflow.python.ops.math_ops import argmax
from tensorflow.python.ops.variables import global_variables_initializer
from tensorflow.examples.tutorials.mnist import input_data
from sklearn.datasets import load_breast_cancer,load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import math
from sklearn.metrics import accuracy_score
import time
import pickle
# %%
#mnist 데이터 가져오기
# softmax를 사용하여 구현하기
mnist = input_data.read_data_sets("MNIST_data/")
x, y = mnist.train.next_batch(mnist.train.num_examples)

oh = OneHotEncoder()
y = oh.fit_transform(y.reshape(-1,1)).toarray()

X_train, X_test , y_train, y_test = \
    train_test_split(x,y,test_size =0.2)
   
X = tf.placeholder(tf.float32 , shape = [None , x.shape[1]])
Y = tf.placeholder(tf.float32 , shape = [None , 10])

W = tf.Variable(tf.random_normal([x.shape[1], 10]))
B = tf.Variable(tf.random_normal([10]))

z = tf.matmul(X,W)+B
hx = tf.nn.softmax(z)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hx ),axis = 1))
optimizer =  tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)
sess =tf.Session()
sess.run(tf.global_variables_initializer())
for i in np.arange(1000):
    sess.run(train,feed_dict = {X:X_train,Y:y_train})
    predict = sess.run(hx, feed_dict = {X : X_train})
    predict_result = np.apply_along_axis(np.argmax,1,predict)

real = np.apply_along_axis(np.argmax,1,predict)
accuracy_score(predict_result,real)

# 셈플보기
test_set = X_test[:20]
for i in np.arange(20):
    print(np.argmax(predict[i]))
    plt.imshow(test_set[i].reshape(28,28))
    plt.show()

#%%
# 1,7 일때 1로
# 나머지는 0으로 예측해보기

# sigmoid 사용
x, y = mnist.train.next_batch(mnist.train.num_examples)
y = np.where((y == 1) | (y == 7) ,1,0)

X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2)
X = tf.placeholder(tf.float32, shape=[None,784])
Y = tf.placeholder(tf.float32, shape=[None,10])
W = tf.Variable(tf.glorot_normal_initializer()(shape=[784,10]))
b = tf.Variable(tf.random_normal([10]))
z = tf.matmul(X,W) + b
hx = tf.nn.sigmoid(z)
cost = -tf.reduce_mean(Y*tf.log(hx)+(1-Y)*tf.log(1-hx))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)


sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in np.arange(1000):
    sess.run(train,feed_dict = {X:X_train,Y:y_train})
    # predict = sess.run(hx, feed_dict = {X : X_train})
    # predict_result = np.apply_along_axis(np.argmax,1,predict)

predict = sess.run(hx, feed_dict = {X : X_train})
predict_result =  np.where(predict )
test_set = X_test[:10]
for  i in range(10):
    print('예측값', predict_result[i])
    plt.imshow(test_set[i].reshape(28,28))
    plt.show()
#%%
# softmax 사용
x, y = mnist.train.next_batch(mnist.train.num_examples)

oh = OneHotEncoder()
y = oh.fit_transform(y.reshape(-1,1)).toarray()
y = np.where((y == 1) | (y == 7) ,1,0)

X_train, X_test , y_train, y_test = train_test_split(x,y,test_size =0.2)

X = tf.placeholder(tf.float32 , shape = [None , x.shape[1]])
Y = tf.placeholder(tf.float32 , shape = [None , 10])

W = tf.Variable(tf.random_normal([x.shape[1], 10]))
B = tf.Variable(tf.random_normal([10]))

z = tf.matmul(X,W)+B
hx = tf.nn.softmax(z)

cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hx ),axis = 1))
optimizer =  tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)


sess =tf.Session()
sess.run(tf.global_variables_initializer())
for i in np.arange(1000):
    sess.run(train,feed_dict = {X:X_train,Y:y_train})
predict = sess.run(hx, feed_dict = {X : X_train})
predict_result = np.apply_along_axis(np.argmax,1,predict)

test_set = X_test[:10]
for  i in range(10):
    print('예측값', predict_result[i])
    plt.imshow(test_set[i].reshape(28,28))
    plt.show()

#%%
# relu, leaky_relu,softmax
# glorot_normal_initializer -> 분산을 이용하여 생성
# 
# 파일 불러오기
mnist = input_data.read_data_sets("MNIST_data/")
x, y = mnist.train.next_batch(mnist.train.num_examples)
# 원핫 인코딩하기
oh = OneHotEncoder()
y = oh.fit_transform(y.reshape(-1,1)).toarray()

# train,test 분리
x_train, x_test,y_train,y_test = train_test_split(x,y,train_size=0.2)
x_train, x_val,y_train,y_val = train_test_split(x_train,y_train,train_size=0.2)

x = tf.placeholder(tf.float32, shape=[None,x_train.shape[1]])
y = tf.placeholder(tf.float32, shape=[None,y_train.shape[1]])

# relu
w1 = tf.Variable(tf.glorot_normal_initializer()(\
    shape = [x_train.shape[1],512]
    ))
b1 = tf.Variable(tf.random_normal([512]))

layer1 = tf.nn.relu(tf.matmul(x,w1)+b1)

# leaky_relu
w2 = tf.Variable(tf.glorot_normal_initializer()(\
    shape = [512,256]
    ))
b2 = tf.Variable(tf.random_normal([256]))

layer2 = tf.nn.leaky_relu(tf.matmul(layer1,w2)+b2)

# softmax
w3 = tf.Variable(tf.glorot_normal_initializer()(\
    shape = [256,y_train.shape[1]]
    ))
b3 = tf.Variable(tf.random_normal([y_train.shape[1]]))

hx =  tf.nn.softmax(tf.matmul(layer2,w3)+b3)

cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(hx ),axis = 1))

# GradientDescent 사용
# train = tf.train.GradientDescentOptimizer(learning_rate = 1e-1).minimize(cost)

# adam 사용
train = tf.train.AdamOptimizer(learning_rate = 1e-1).minimize(cost)


sess = tf.Session()
sess.run(tf.global_variables_initializer())

val_ross, train_loss = [],[]
val_acc , train_acc = [] ,[]

epochs = np.arange(1000)

for epoch in epochs:
    start = time.time()  # 시작 시간 저장
    sess.run(train, feed_dict = {x : x_train, y : y_train})

    va = sess.run(hx,feed_dict = {x : x_val})
    ta = sess.run(hx,feed_dict = {x : x_train})
    val_acc.append(
        accuracy_score(
            np.apply_along_axis(np.argmax,1,y_val),
            np.apply_along_axis(np.argmax,1,va)
        )
    )
    train_acc.append(
            accuracy_score(
                np.apply_along_axis(np.argmax,1,y_train),
                np.apply_along_axis(np.argmax,1,ta)
            )
        )
    val_tmp_acc = sess.run(cost,feed_dict = {x : x_val , y : y_val})
    val_acc.append(val_tmp_acc)

    train_tmp_acc = sess.run(cost,feed_dict = {x : x_val , y : y_val})
    train_acc.append(train_tmp_acc)  

    print(f'{epoch} / {len(epochs)} , 소요시간 : {time.time() - start}')
    print(f'val_acc : {val_tmp_acc} , train_acc : {train_tmp_acc}\n')

predict = sess.run(hx,feed_dict = {x : x_test, y : y_test})
result = np.apply_along_axis(np.argmax,1,predict)

y_hat = np.apply_along_axis(np.argmax,1,y_test)

print(f'테스트 정확도 {accuracy_score(result,y_hat)}')


#%%

print(f'테스트 정확도 {accuracy_score(result,y_hat)}')

#%%
x_train.shape[1]
#%%


"""
cifar10 를 이용한 실습
"""

import tensorflow as tf
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
import time

# 파일 다운로드하기.
data = tf.keras.datasets.cifar10.load_data()

oh = OneHotEncoder()

x = data[0][0]
y = data[0][1]

x_data = x.reshape(50000,32*32*3)
y_data = oh.fit_transform(y).toarray()

x_train, x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.2)
x_train, x_val,y_train,y_val = train_test_split(x_train,y_train,train_size=0.2)

x = tf.placeholder(tf.float32, shape=[None,x_train.shape[1]])
y = tf.placeholder(tf.float32, shape=[None,y_train.shape[1]])
# relu
w1 = tf.Variable(tf.glorot_normal_initializer()(shape = [x_train.shape[1],32]))
b1 = tf.Variable(tf.glorot_normal_initializer()(shape = [32]))
layer1 = tf.nn.tanh(tf.matmul(x,w1)+b1)

w2= tf.Variable(tf.glorot_normal_initializer()(shape = [32,64]))
b2 = tf.Variable(tf.glorot_normal_initializer()(shape = [64]))
layer2 = tf.nn.elu(tf.matmul(layer1,w2)+b2)

w3= tf.Variable(tf.glorot_normal_initializer()(shape = [64,32]))
b3 = tf.Variable(tf.glorot_normal_initializer()(shape = [32]))
layer3 = tf.nn.selu(tf.matmul(layer2,w3)+b3)

w4= tf.Variable(tf.glorot_normal_initializer()(shape = [32,y_train.shape[1]]))
b4 = tf.Variable(tf.glorot_normal_initializer()(shape = [y_train.shape[1]]))
hx = tf.nn.softmax(tf.matmul(layer3,w4)+b4)

cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(hx),axis = 1))

# GradientDescent 사용
# train = tf.train.GradientDescentOptimizer(learning_rate = 1e-1).minimize(cost)

# adam 사용
train = tf.train.AdamOptimizer(learning_rate = 1e-5).minimize(cost)


sess = tf.Session()
sess.run(tf.global_variables_initializer())

val_ross, train_loss = [],[]
val_acc , train_acc = [] ,[]

epochs = np.arange(1000)

for epoch in epochs:
    start = time.time()  # 시작 시간 저장
    sess.run(train, feed_dict = {x : x_train, y : y_train})

    va = sess.run(hx,feed_dict = {x : x_val})
    ta = sess.run(hx,feed_dict = {x : x_train})
    val_acc.append(
        accuracy_score(
            np.apply_along_axis(np.argmax,1,y_val),
            np.apply_along_axis(np.argmax,1,va)
        )
    )
    train_acc.append(
            accuracy_score(
                np.apply_along_axis(np.argmax,1,y_train),
                np.apply_along_axis(np.argmax,1,ta)
            )
        )
    val_tmp_acc = sess.run(cost,feed_dict = {x : x_val , y : y_val})
    val_acc.append(val_tmp_acc)

    train_tmp_acc = sess.run(cost,feed_dict = {x : x_val , y : y_val})
    train_acc.append(train_tmp_acc)  

    print(f'{epoch} / {len(epochs)} , 소요시간 : {time.time() - start}')
    print(f'val_acc : {val_tmp_acc} , train_acc : {train_tmp_acc}\n')

predict = sess.run(hx,feed_dict = {x : x_test, y : y_test})
result = np.apply_along_axis(np.argmax,1,predict)

y_hat = np.apply_along_axis(np.argmax,1,y_test)

print(f'테스트 정확도 {accuracy_score(result,y_hat)}')


#%%
print(f'테스트 정확도 {accuracy_score(result,y_hat)}')