# 선형회기 ( Linear_Regression )

## [수식이 안보이면 클릭 후 설치](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related)

## 간단 설명

- 가설함수를 생성하고, 실제 데이터에 맞는 Weight 과 Bias를 찾는것이 목적

## 프로세스

1.  `X`를 선언한다.
    - 가상의 X를 선언한다.
1.  `Y`를 선언한다.
    - 가상의 Y를 선언한다.
1.  `Weight를` 선언한다.
    - 실질적으로 구하고자 하는 것이다.
    - 의미하는 것은 `가중치`이다.
1.  `Bias`를 선언한다.
    - 실질적으로 구하고자 하는 것이다.
    - ## 편향을 의미한다.
1.  `Hyperparameter`를 선언한다.
    - W와 B를 구할 떄 사용하는 가설함수이다
      - 예시aa
        - $$w_1*x_1 + ... +w_n*x_n  + b$$
          - $b$ : Bias
          - $w$ : Weight
1.  `Cost`를 선언한다.
    - [`Loss함수`](../../Function/Cost_Function)를 구하는 것 이다.
    - 이 모델이 얼마나 잘 객체를 설명하는것에 대한 것을 수치로 보여준다.
1.  `Optimizer`를 선언한다.
    - 파라미터를 갱신하는 부분이다.
    - 즉 위에 선언한 것을 이용하여 실제 가중치등의 변화를 진행시키는 부분이다.

## 예제

1. [`Matrix`](###Matrix)
1. [`Tensorflow`](###Tensorflow)

### Matrix

1. [`미사용`](####미사용)
2. [`사용`](####사용)

#### 미사용

```python
# 3항 선형회귀
x1 = np.random.randn(100)
x2 = np.random.randn(100)
x3 = np.random.randn(100)
# 3개의 Weight(가중치) 선언
real_w1 = np.random.randn(1)
real_w2 = np.random.randn(1)
real_w3 = np.random.randn(1)
# 1개의 Bais(편향) 선언
real_b = np.random.randn(1)

# Target(y값) 선언
y =real_w1 *x1 + real_w2 *x2 + reaYl_w3 *x3 + b

# 예측을 위한 Weight(가중치) 선언
w1 = np.random.randn(1)
w2 = np.random.randn(1)
w3 = np.random.randn(1)
# 예측을 위한 Bais(편향) 선언
b = np.random.randn(1)
# 예측을 위한 HyperParameter(가설함수) 선언
hx =w1 *x1 + w2 *x2 + w3 *x3 + b

# Learning rate 선언
lr = 0.001

# (epoch)훈련횟수 선언
epochs = np.arange(1000)
# 훈련을 통하여 실제 hyperParameter 예측하기
for epoch in epochs :
    w1 = w1 - lr*((hx - y ) * x1).mean()
    w2 = w2 - lr*((hx - y ) * x2).mean()
    w3 = w3 - lr*((hx - y ) * x3).mean()
    b = b - lr*(hx-y).mean()
    hx = w1 *x1 + w2 *x2 + w3 *x3 +b
    cost = ((hx - y)**2).mean()
```

- 간단하게 `선형회기`가 어떻게 `구성`되는지 `확인`하기는 편하지만, 실질적으로 사용하기는 `비효율` 적이다.
- 이유
  - 칼럼 1개당 변수를 최소 3개(Y, X , W) 를 선언 해주어하는데, 그러한 하드코딩은 비효율 적이다.

#### 사용

```python
# 3항 선형회귀
x1 = np.random.randn(100)
x2 = np.random.randn(100)
x3 = np.random.randn(100)
# 3개의 Weight(가중치) 선언
real_w1 = np.random.randn(1)
real_w2 = np.random.randn(1)
real_w3 = np.random.randn(1)
# 1개의 Bais(편향) 선언
real_b = np.random.randn(1)

# Target(y값) 선언
y =real_w1 *x1 + real_w2 *x2 + real_w3 *x3 + b

# 각 x 값 가져오기
X = np.c_[x1,x2,x3]
# N*1 모양인 Y를  1*N모양으로 변경
# 행렬곱을 하기 위해서 변경
y = y.reshape(-1,1)
# 랜덤하게 3개의 Weight을 가져옴
w = np.random.randn(3,1)
# 랜덤하게 1개의 Bais를 가져옴
b = np.random.randn(1)
# 생성된 가상의 값들로 hyperParameter생성
hx = np.dot(X,w) + b
# Learning Rate를 선언하여 1회 훈련당 변화량을 선언
lr = 6e-6
# (epoch)훈련횟수 선언
epochs = np.arange(1000)
# 훈련
for ephoch in epochs:
    w = w - lr * np.dot(X.T,(hx-y))/X.shape[0]
    b = b - lr*(hx-y).mean()
    hx = np.dot(X,w) + b
    cost = ((hx - y)**2).mean()

```

- Matrix를 사용 하지 않은 것 보다는 `상대적으로 편하다`.
- 위 코드에서는 임의의 데이터를 삽입하였지만, 실질적으로 사용시 데이터셋(DataSet)을 불러와서 사용하기 때문에 조금 더 편하다.

### Tensorflow

```python
# X,Y를 placeholder 생성
x_train = tf.placeholder(tf.float32)
y_train = tf.placeholder(tf.float32)
# Tensorflow를 이용하여 Weight 생성
w =tf.Variable(tf.random_normal([1]),name = 'wight')
# Tensorflow를 이용하여 Bais 생성
b =tf.Variable(tf.random_normal([1]),name = 'bais')
# HyperParameter 생성
hx = x_train *w+b
# 비용/손실함수 생성
cost = tf.reduce_mean(tf.square(hx-y_train))
# Optimizer생성
optimaizer = tf.train.GradientDescentOptimizer(
    learning_rate =0.01)
#cost값 측정 및 훈련을 위한 Training 모델 생성
train = optimaizer.minimize(cost)
# 세션 생성
sess = tf.Session()
# 초기값 지정
sess.run(tf.global_variables_initializer())
# 훈련시작
for epoch in np.arange(1000):
    cost_val, W_val, b_val, _ = sess.run(
        [cost, w, b, train],
        feed_dict = {x_train: [1, 2, 3], y_train: [1, 2, 3]}
        )
```
