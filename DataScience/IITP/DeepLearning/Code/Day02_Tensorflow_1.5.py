#%%
# tensor version == 1.5
from sklearn import datasets
import tensorflow as tf
import matplotlib
import pandas as pd
import numpy as np
from tensorflow.python.ops.variables import global_variables_initializer

#%%
node1 = tf.constant(3.0,tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1,node2)
sess = tf.Session()
print(sess.run([node1,node2]))
print(sess.run([node3]))

#%%

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
# 람다 생성이라고 생각하면 편할듯
adder_node = a+b
# adder_node사용하여 합 구하기
print(sess.run(adder_node,feed_dict={a:3,b:4.5}))
print(sess.run(adder_node,feed_dict={a:[1,3],b:[2,4]}))

#%%
x_train = [1,2,3]
y_train = [1,2,3]
w =tf.Variable(tf.random_normal([1]),name = 'wight')
b =tf.Variable(tf.random_normal([1]),name = 'bais')
hx = x_train *w+b
cost = tf.reduce_mean(tf.square(hx-y_train))
optimaizer = tf.train.GradientDescentOptimizer(
    learning_rate =0.01)

#%%
train = optimaizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
# %%
for step in range(20001):
 
    if step % 100 == 0:
        print(step,sess.run(cost),sess.run(w),sess.run(b))
# %%
# placeholder사용하기

x_train = tf.placeholder(tf.float32)
y_train = tf.placeholder(tf.float32)
w =tf.Variable(tf.random_normal([1]),name = 'wight')
b =tf.Variable(tf.random_normal([1]),name = 'bais')
hx = x_train *w+b
cost = tf.reduce_mean(tf.square(hx-y_train))
optimaizer = tf.train.GradientDescentOptimizer(
    learning_rate =0.01)
train = optimaizer.minimize(cost)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
# %%
for epoch in np.arange(1000):
    cost_val, W_val, b_val, _ = \
        sess.run([cost, w, b, train],
                feed_dict={x_train: [1, 2, 3], y_train: [1, 2, 3]})

    if epoch % 100 == 0:
        print(epoch,cost_val, W_val, b_val)
# %%

# sess.run(hx,feed_dict={x_train[1]})

x1 = np.random.randn(100)
x2 = np.random.randn(100)
x3 = np.random.randn(100)
x = np.c_[x1,x2,x3]
x= x.astype(np.float32)
y = x1*np.random.randn(1) + x2 * np.random.randn(1) + x3 * np.random.randn(1)
y = y.reshape(-1,1)
w = tf.Variable(tf.random_normal([3,1]))
b = tf.Variable(tf.random_normal([1]))
hx = tf.matmul(x,w)
cost = tf.reduce_mean(tf.square((hx-y)))

optimaizer = tf.train.GradientDescentOptimizer(learning_rate = 0.01)
train = optimaizer.minimize(cost)


sess = tf.Session()
sess.run(tf.global_variables_initializer())

# %%
for ephoch in np.arange(10001):
    sess.run(train)
    if ephoch %100 == 0:
        print(ephoch,sess.run(cost),sess.run(w),sess.run(b))
# %%
import matplotlib.pyplot as plt
def plot(x,y):
    return plt.plot(x,y)

# sigmoid
def sigmoid(x):
    return 1/(1+np.exp(-x))
x = np.arange(-5,5,0.1)

plot(x,sigmoid(x))
#%%

def step (val):
    if val >= 0:
        return 0
    return 1
x = np.linspace(0,100,1000)
# y == 1
plot(x,-np.log(x))

# y == 0
plot(x,-np.log(x))


#%%
x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]

# Sigmoid 
X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])
w = tf.Variable(tf.random_normal([2,1]))
b = tf.Variable(tf.random_normal([1]))
hx = tf.matmul(X,w)+b
cost = tf.reduce_mean(Y * tf.log(hx) + (1-y)*tf.log(1-hx))

optimaizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-3)
train = optimaizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
predicted = tf.cast(hx > 0.5 , dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype = tf.float32))

for epoch in np.arange(10000):
    sess.run(train,feed_dict={X: x_data, Y: y_data})

            
#%%
sess.run(hx,feed_dict={X:[[2,6]]})


#%%
# %%
from sklearn.datasets import load_diabetes
# %%

# model = load_diabetes()

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv')
x_data = df.iloc[:,:-1]
x_data = x_data.astype(np.float32)
y_data = df.iloc[:,-1].values.reshape(-1,1)
y_data = y_data.astype(np.float32)

x = tf.placeholder(tf.float32 , shape = [None,x_data.shape[1]])
y = tf.placeholder(tf.float32 , shape = [None,1])
w = tf.Variable(tf.random_normal([x_data.shape[1],1]))
b = tf.Variable(tf.random_normal([1]))
hx = tf.matmul(x,w)+b
hx = tf.sigmoid(hx)
cost = tf.reduce_mean(Y * tf.log(hx) + (1-y)*tf.log(1-hx))

optimaizer = tf.train.GradientDescentOptimizer(learning_rate = 1e-5)
train = optimaizer.minimize(cost)

predict = tf.cast(hx > 0.5 , dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predict,Y),dtype = tf.float32))

#%%
sess = tf.Session()
sess.run(tf.global_variables_initializer())
for epoch in np.arange(10000):
    cost,w,b,acc,pre,_= sess.run([cost, w, b,accuracy,predict, train],feed_dict={x: x_data, y: y_data})
    # sess.run(train,feed_dict={x: x_data, y: y_data})
    # print(sess.run(accuracy,feed_dict = {x_data[0]}))

#%%