#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
# 간단 선형회기
X = np.random.randn(100)
W = np.random.randn(1)
b = np.random.randn(1)
y = X*W

plt.scatter(X,y)
#%%
# 신경망 회기
costs = []
weights = np.linspace(-10,10,100)
for weight in weights:
    hypothesis = weight*X
    cost = ((hypothesis - y)**2).mean()
    costs.append(cost)
plt.plot(weights,costs)


#%%

w = np.random.uniform(-1.0,1.0)
B = np.random.uniform(-1.0,1.0)
hypothesis = w*X
#Learning Rate
lr = 0.001
epochs = np.arange(1000)
for epoch in epochs:
    w = w- lr*((hypothesis -y)*X).mean()
    hypothesis = w*X
    cost = ((hypothesis - y)**2).mean()
    print(cost)


# %%
#  신경망 선형회기 다항식
x1 = np.random.randn(100)
x2 = np.random.randn(100)
w1 = np.random.rand(1)
w2 = np.random.rand(1)

y = x1*w1 +x2*w2

w1 = np.random.randn(1) 
w2 = np.random.randn(1)
hx = x1*w1 +x2*w2
#%%

lr = 0.01
epochs = np.arange(1000)
for epoch in epochs:
    w1 = w1- lr*((hx -y)*x1).mean()
    w2 = w2- lr*((hx -y)*x2).mean()
    hx = x1*w1 +x2*w2
    cost = ((hx - y)**2).mean()
    print(cost)


#%%
w = np.random.randn(1) 
b = np.random.randn(1)
hx = w*X  +b
lr = 0.01
epochs = np.arange(1000)
for epoch in epochs:
    w = w - lr*((hx -y)*X).mean()
    b = b - lr*((hx -y)*y).mean()
    hx = w*X  +b
    cost = ((hx - y)**2).mean()
    print(cost)

#%%
# 3항 선형회귀
x1 = np.random.randn(100)
x2 = np.random.randn(100)
x3 = np.random.randn(100)
real_w1 = np.random.randn(1)
real_w2 = np.random.randn(1)
real_w3 = np.random.randn(1)
real_b = np.random.randn(1)

y =real_w1 *x1 + real_w2 *x2 + real_w3 *x3 + b
#%%
#가설 함수
w1 = np.random.randn(1)
w2 = np.random.randn(1)
w3 = np.random.randn(1)
b = np.random.randn(1)
hx =w1 *x1 + w2 *x2 + w3 *x3 + b

lr = 0.001
epochs = np.arange(1000)

for epoch in epochs :
    w1 = w1 - lr*((hx - y ) * x1).mean()
    w2 = w2 - lr*((hx - y ) * x2).mean()
    w3 = w3 - lr*((hx - y ) * x3).mean()
    b = b - lr*(hx-y).mean()
    hx = w1 *x1 + w2 *x2 + w3 *x3 +b
    cost = ((hx - y)**2).mean()
    print(cost)


# %%
X = np.c_[x1,x2,x3]
y = y.reshape(-1,1)
w = np.random.randn(3,1)
hx = np.dot(X,w) + b

# %%
# 3*1
epochs = np.arange(100000)
for epoch in epochs :
    w = w - lr*np.dot(X.T,(hx-y))/len(X)
    b = b - lr*(hx-y).mean()
    hx = np.dot(X,w) + b
    cost = ((hx - y)**2).mean()
    # print(cost)
#%%
# boston 데이터를 이용하여 선형회기
from sklearn.datasets import load_boston
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import train_test_split
data = load_boston()
X = data.data
y = data.target
#%%
def rmse(y_hat,y):
    result = mse(y_hat , y)
    return np.sqrt(result)
#%%
model = LinearRegression()
model.fit(X, y)
print('r2',model.score(X, y))
print('rmse',rmse(model.predict(X),y))

#%%
X.shape
#%%
w = np.random.randn(X.shape[1],1)
b = np.random.randn(1)
hx = np.dot(X,w) + b
lr = 6e-6
y = y.reshape(-1,1)
epochs = np.arange(100000)
for ephoch in epochs:
    w = w - lr * np.dot(X.T,(hx-y))/X.shape[0]
    b = b - lr*(hx-y).mean()
    hx = np.dot(X,w) + b
    cost = ((hx - y)**2).mean()
    print(cost)
#%%
def myModel(X,y,epochs = np.arange(100000)):
    w = np.random.randn(X.shape[1],1)
    b = np.random.randn(1)
    hx = np.dot(X,w) + b
    lr = 6e-6
    y = y.reshape(-1,1)
    for _ in epochs:
        w = w - lr * np.dot(X.T,(hx-y))/X.shape[0]
        b = b - lr*(hx-y).mean()
        hx = np.dot(X,w) + b
        cost = ((hx - y)**2).mean()
    return np.sqrt(cost)
#%%
myModel(X,y.reshape(-1,1))

#%%

from sklearn.datasets import load_boston
data = load_boston()
x = data.data
y = data.target
#%%
x.shape
#%%
x = data.data
y = data.target.reshape(-1,1)
w = np.random.randn(x.shape[1])
b = np.random.randn(1)
hx = np.dot(x,w) + b

lr = 1e-5
epochs = 1000
#%%
print(x.shape)
print(y.shape)
print(w.shape)
print(b.shape)
print(hx.shape)
#%%
for _ in epochs:
    w = w + lr*np.dot(x.T,)


