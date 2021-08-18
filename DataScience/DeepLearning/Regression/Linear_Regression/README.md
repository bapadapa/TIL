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
import numpy as np
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

### Tensorflow (ver == 1.5)

```python
import tensorflow as tf
import numpy as np
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

### Keras

1. ```python
   from keras.layers.core import Dropout
   from sklearn.model_selection import train_test_split
   from keras.utils import np_utils
   from keras.datasets import mnist
   from keras.models import Sequential
   from keras.layers import Dense, Activation
   import numpy as np
   import matplotlib.pyplot as plt
   ```

   - 필요한 라이브러리를 import 한다.

1. ```python
   # 모델 불러오기
   (X_train, Y_train), (X_test,Y_test) = mnist.load_data()
   # 이미지이기 때문에 전처리
   X_train = X_train.reshape(X_train.shape[0],-1).astype(np.float32)/255
   X_test = X_test.reshape(X_test.shape[0],-1).astype(np.float32)/255

   # Target이기 떄문에 Categorical Value로 변경
   Y_train = np_utils.to_categorical(Y_train)
   Y_test = np_utils.to_categorical(Y_test)

   # Train <-> Test 로 분할
   x_train, x_val,y_train, y_val = train_test_split(X_train,Y_train,   test_size=.2)
   ```

   1. Concept
      1. `전처리` 단계이다.
      1. 데이터를 불러오고, `원하는 Shape`로 만들어준다.
      1. 만들어진 Shape을 훈련을 위해 `Train,Test`로 분할해준다
   1. Process
      1. 데이터를 호출해혼다.
      1. 이미지의 색이 256이기 때문에 255로 나눠준다.
      1. Y의 기본값이 integer로 나열되어 있기 떄문에 categorical로 변경해 준다.
      1. 전처리한 `X,y`를 `Train,Test`로 나눠준다.

1. ```python
   # 모델 생성
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
   # 생성된 모델 구성 확인
   print(model.summary())
   ```

   1. 위와 같이 Layer를 구성해준다.
      - Layer구성에는 정답이 없다.
      - Layer가 수가 많아 좋고, 적어서 나쁜 결과를 내는것은 이니다.
        - `Layer는 양보다는 질` 즉, 잘 구성해야한다.
   1. Dense

      1. Concept

         1. Multi-layer Perceptron(다층 퍼셉트론 신경망)에서 사용되는 레이어
         1. `Input과 Output`을 `연결`시켜주는 역할

      1. Parameter
         1. Output Dim (기본 값임)
            - 현 Layer에서 연산 후 전달할 크기를 지정해줌
         1. input_dim
            - 전달받을 파라미터의 모양
            - 최초 1회는 필수로 작성해야한다.
              - 이후에는 자동으로 할당해주기 때문에 굳이 작성할 필요는 없다.
         1. activation
            - 활성함수 삽입
            - 산출된 Weight(가중치)에 작성한 활성함수를 적용시켜준다.
            - [Activation Function 상세](../../Function/Activation_Function)
         1. kernel_initializer
            - Layer 시작시 Kernel값을 어떻게 초기화 시킬지 정한다.
              - 즉, Keras Layer의 `초기 난수 가중치`를 어떻게 `설정`할지를 지정하는 것 이다.

1. ```python
   # 모델 컴파일
   model.compile(
       optimizer='adamDelta',
       loss= 'categorical_crossentropy',
       metrics=['accuracy']
       )
   ```

   1. Concept
      1. 메소드를 통해서 학습 방식에 대한 환경설정한다.
   1. Parameter

      1. optimizer (정규화기)

         1. 실질적으로 파라미터를 갱신시키는 역할을한다.
         1. 여러 Optimizer가 있다.
            - [공식홈페이지](https://keras.io/api/optimizers/)에서 확인해보자

      1. loss

         1. `손실/비용함수`
         1. 데이터를 최적화하기 위한 함수다.
         1. 여러 함수가 있는데, 필요에 따라 적절히 사용해야 한다.
         1. [상세 내용](../../Function/Cost_Function)

      1. metrics
         1. 위 연산에 따른 Log값을 지정한다.
         1. 위 예제는 `accuracy`를 사용했음으로 `accuracy`에 대한 값을 자동 저장한다.

1. ```python

   # 모델 훈련
   hist = model.fit(
       x= x_train,
       y= y_train,
       epochs= 100 ,
       batch_size = 64,
       validation_data = (x_val,y_val)
       )

   ```

   1. Concept
      1. 생성된 모델을 가지고 실질적으로 훈련시키는 과정이다.
   1. Parameter
      1. x,y
         - 훈련시킬 Train Data Set을 삽입한다.
      1. epochs
         - `Layer Set`의 훈련횟수를 작성한다.
      1. batch_size
         - 데이터를 몇등분으로 하여 훈련시킬지 지정해준다.
           - 10이면 데이터를 10등분하여 훈련(즉 10회 훈련)
      1. validation_data
         - 훈련시킨 모델을 검증하는 데이터이다
           - 즉, Test데이터를 삽입한다.
