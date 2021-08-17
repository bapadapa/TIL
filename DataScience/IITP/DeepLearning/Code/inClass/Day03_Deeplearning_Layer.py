#%%
from math import e
from matplotlib.pyplot import scatter
from sklearn import datasets
import matplotlib
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.ops.array_ops import one_hot
from tensorflow.python.ops.gen_math_ops import cos, sqrt
from tensorflow.python.ops.gen_string_ops import encode_base64
from tensorflow.python.ops.variables import global_variables_initializer
from sklearn.datasets import load_boston
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import train_test_split

# %%
# TF를 이용하여 구현하는 선형회기 , 활성함수 : softMax
# Train Set
x_data = [[1, 2, 1], [1, 3, 2], [1, 3, 4], [1, 5, 5], [1, 7, 5], [1, 2, 5], [1, 6, 6], [1, 7, 7]]
y_data = [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0], [1, 0, 0]]

# Test Set
x_test = [[2, 1, 1], [3, 1, 2], [3, 3, 4]]
y_test = [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

# 선형회기를 위한 가설생성
# 가상의 x,y
x = tf.placeholder(tf.float32,shape = [None,3])
y = tf.placeholder(tf.float32,shape = [None,3])

# 가상의 w(가중치) , b(편향)
w = tf.Variable(tf.random_normal([3,3]))
b = tf.Variable(tf.random_normal([3]))

# 가상의 함수
z = tf.matmul(x,w)+b
# 활성함수 적용
hx = tf.nn.softmax(z)

# cost 추출
cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(hx),axis = 1))

# optimizer 생성 ( leanring_rate == 탐색 정도)
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-5)
train = optimizer.minimize(cost)

# tf를 사용하기위해 session열기
sess = tf.Session()
# 초기 설정
sess.run(tf.global_variables_initializer())
# 훈련 횟수
epochs = np.arange(1000)
val_losses = [] 
acc_losses = []
val_rate = []
acc_rate = []

def getRate(x,y,x_data,y_data):
    # 훈련당 결과값 저장
    train_predict = sess.run(hx,feed_dict = {x:x_data})
    # 훈련을 통해 얻은 결과값
    train_result = np.apply_along_axis(np.argmax,1,train_predict)
    # 훈련을 통해 예측한 y값
    train_y = np.apply_along_axis(np.argmax,1,np.array(y_data))
    # 정확도, 즉 TT 비율 
    acc = sum(train_result == train_y)/ train_result.size
    return train_predict,train_result,train_y,acc

for epoch in epochs:
    # 훈련시키기
    sess.run(train,feed_dict={x:x_data,y:y_data})
    
    # Rate 구하기
    train_predict,train_result,train_y,acc = getRate(x,y,x_data,y_data)
    acc_rate.append(acc)

    # 추출된 val값을 리스트에 추가
    val_predict,val_result,val_y,val = getRate(x,y,x_test,y_test)    
    val_rate.append(val)

    # Train Set 이용
    # Loss 구하기
    acc_loss = sess.run(cost,feed_dict = {x : x_data , y : y_data})
    acc_losses.append(acc_loss)

    # Test Set 이용
    val_loss = sess.run(cost,feed_dict = {x : x_test , y : x_test})
    val_losses.append(val_loss)

    if epoch % 100 == 0 :
        print(f'epoch ==> {epoch}')
        print(f'train accuracy ==> {acc*100}%  , train rate ==> {acc_loss}')
        print(f'validation accuracy ==> {val*100}%  ,  validation rate ==> {val_loss}\n')


# %%
# Non-normalized inputs

xy = np.array([[828.659973, 833.450012, 908100, 828.349976, 831.659973],
              [823.02002, 828.070007, 1828100, 821.655029, 828.070007],
              [819.929993, 824.400024, 1438100, 818.97998, 824.159973],
              [816, 820.958984, 1008100, 815.48999, 819.23999],
              [819.359985, 823, 1188100, 818.469971, 818.97998],
              [819, 823, 1198100, 816, 820.450012],
              [811.700012, 815.25, 1098100, 809.780029, 813.669983],
              [809.51001, 816.659973, 1398100, 804.539978, 809.559998]])
x_data = xy[:,:-1]
y_data = xy[:,-1].reshape(-1,1)

x = tf.placeholder(tf.float32,shape = [ None, x_data.shape[1] ])
y = tf.placeholder(tf.float32,shape = [ None, 1 ] )
w = tf.Variable(tf.random_normal([ x_data.shape[1] , 1 ]))
b = tf.Variable(tf.random_normal([ 1 ]))
hx = tf.matmul(x,w) + b
cost = tf.reduce_mean(tf.square(hx- y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-8)
train = optimizer.minimize(cost)


with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())
    epochs = np.arange(10000)
    for epoch in epochs:
        sess.run(train,feed_dict = {x : x_data, y : y_data})
        print(sess.run(cost,feed_dict = {x : x_data, y : y_data}))
#%%
# normalized inputs
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
xy = sc.fit_transform(xy)

x_data = xy[:,:-1]
y_data = xy[:,-1].reshape(-1,1)

x = tf.placeholder(tf.float32,shape = [ None, x_data.shape[1] ])
y = tf.placeholder(tf.float32,shape = [ None, 1 ] )
w = tf.Variable(tf.random_normal([ x_data.shape[1] , 1 ]))
b = tf.Variable(tf.random_normal([ 1 ]))
hx = tf.matmul(x,w) + b
cost = tf.reduce_mean(tf.square(hx- y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-3)
train = optimizer.minimize(cost)


with tf.Session() as sess :
    sess.run(tf.global_variables_initializer())
    epochs = np.arange(10000)
    for epoch in epochs:
        sess.run(train,feed_dict = {x : x_data, y : y_data})
        print(sess.run(cost,feed_dict = {x : x_data, y : y_data}))

#%%
# mnist
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
mnist = input_data.read_data_sets('MNIST_data/',one_hot = True)
batch_xs, batch_ys = mnist.train.next_batch(100)
#%%
plt.imshow(batch_xs[0].reshape([28,28]))
    
np.argmax(batch_ys[0])

#%%
x = tf.placeholder(tf.float32, shape = [None,batch_xs.shape[1]])
y = tf.placeholder(tf.float32, shape = [None,10])

w = tf.Variable(tf.random_normal([batch_xs.shape[1], 10 ]))
b = tf.Variable(tf.random_normal([10]))

hx = tf.nn.softmax(tf.matmul(x,w)+b)

cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(hx), axis = 1))

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-5).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    epochs = np.arange(2000)
    for epoch in epochs:
        sess.run(optimizer , feed_dict = {x : batch_xs, y : batch_ys})


#%%
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt


mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
x,y= mnist.train.next_batch(mnist.train.num_examples)
x /=255
# y /=255
oh = OneHotEncoder()
y_one= oh.fit_transform(y.reshape(-1,1)).toarray()
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
x_train,x_val,y_train,y_val = train_test_split(x_test,y_test,test_size=0.2)

#1 가상 x
x = tf.placeholder(tf.float32, shape = [None,batch_xs.shape[1]])
#2 가상 y
y = tf.placeholder(tf.float32, shape = [None,10])
#3 가상 weight ( 가중치 )
w = tf.Variable(tf.random_normal([batch_xs.shape[1],10]))
#4 가상 bias ( 편향치 )
b = tf.Variable(tf.random_normal([10]))
#5 Activate Function을 적용한 hyperparameter
hx = tf.nn.softmax(tf.matmul(x,w) + b)
#6 cross-Entropy
cost = tf.reduce_mean(-tf.reduce_sum(y * tf.log(hx), axis = 1))
#7 Optimizer
Optimizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-5)
train = Optimizer.minimize(cost)

#8_1 Batch Size 미사용
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    epochs = np.arange(1000)
    for epoch in epochs:
        sess.run(train,feed_dict = {x:x_train,y:y_train})
        predict = sess.run(hx,feed_dict = {x:x_val})
        predict_result = np.apply_along_axis(np.argmax,1,predict)
        real = np.apply_along_axis(np.argmax,1,y_val)        
        
        if epoch %100 == 0:         
            val_acc = sum(predict_result == real)/real.size   
            print(f'epoch :{epoch} validation accuracy : {val_acc}')

#%%
#8_2 Batch Size 사용
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    epochs = np.arange(15)
    batch_size = 10
    for epoch in epochs:
        total_batch = int(x_train.shape[0]/batch_size)
        for batch in range(total_batch):     
            batch_xs = x_train[batch_size*batch:batch_size*(batch+1)]
            batch_ys = y_train[batch_size*batch:batch_size*(batch+1)]
            
            sess.run(train,feed_dict = {x:batch_xs,y:batch_ys})

        predict = sess.run(hx,feed_dict = {x:x_val})
        predict_result = np.apply_along_axis(np.argmax,1,predict)
        real = np.apply_along_axis(np.argmax,1,y_val)        
        val_acc = sum(predict_result == real)/real.size
        print(f'epoch :{epoch} validation accuracy : {val_acc}')
            
#%%
batch_size = 100
for epoch in epochs:
    total_batch = int(x_train.shape[0]/batch_size)
    start = 0
    end = 1
    for start in range(total_batch):  
        print(start,end)

#%%
# XOR data set

x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_data = np.array([[0],    [1],    [1],    [0]], dtype=np.float32)

x = tf.placeholder(tf.float32,shape = [None,x_data.shape[1]])
y = tf.placeholder(tf.float32,shape = [None,1])

w = tf.Variable(tf.random_normal([x_data.shape[1],1]))
b = tf.Variable(tf.random_normal([1]))

hx = tf.sigmoid(tf.matmul(x,w)+b)

cost = -tf.reduce_mean(y *  tf.log(hx) + (1 - y ) * tf.log(1-hx))

optimizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-5)
train = optimizer.minimize(cost)

with tf.Session() as sess:
    sess.run(global_variables_initializer())
    epochs = np.arange(1000)
    for epoch in epochs:
        sess.run(train ,feed_dict = {x:x_data , y:y_data})
        result = sess.run(hx ,feed_dict = {x:x_data})
        predict = np.where(result >= .5 , 1, 0)

        print(f'   epoch ==> {epoch+1}')
        print(f'accuracy ==> {sum(y_data == predict)/x_data.shape[0]}\n')
        

#%%
x_data.shape[1]
#%%
# Layer 쌓기
x_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=np.float32)
y_data = np.array([[0],    [1],    [1],    [0]], dtype=np.float32)

x = tf.placeholder(tf.float32,shape = [None,x_data.shape[1]])
y = tf.placeholder(tf.float32,shape = [None,y_data.shape[1]])

# Layer 1층!
w1 = tf.Variable(tf.random_normal([x_data.shape[1],2]))
b1 = tf.Variable(tf.random_normal([2]))
layer1 = tf.sigmoid(tf.matmul(x,w1)+b1)

# Layer 2층!
w2 = tf.Variable(tf.random_normal([x_data.shape[1],1]))
b2 = tf.Variable(tf.random_normal([1]))
hx = tf.sigmoid(tf.matmul(layer1,w2)+b2)

cost = -tf.reduce_mean(y *  tf.log(hx) + (1 - y ) * tf.log(1-hx))
train = tf.train.GradientDescentOptimizer(learning_rate = 1e-1).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in np.arange(10000):
        sess.run(train,feed_dict={x:x_data ,y:y_data})
        predict = sess.run(hx,feed_dict={x : x_data})
        result = np.where(predict >= 0.5,1,0)
        if epoch %100 == 0 :            
            acc = sum(result == y_data)/x_data.shape[0]        
            print(f'epoch ==> {epoch} , acc ==> {acc}')
