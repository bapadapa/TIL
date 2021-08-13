# 활성함수 Activation Function

## [수식이 안보이면 클릭 후 설치](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related)

## softmax

1. 수식
   - $$y_k = \frac{\exp(a_k)}{\sum_{i=1}^n\exp(a_i)}$$
1. 정의
   - 입력받은 값을 0~1사이의 값으로 정규화후 출력해 주고, 값의 합은 항상 `1`이된다
   - 주로 `출력층 (Output Layer)`에서 사용이
     된다.
   - `예측(Prediction)` 및 `분류(Classification)`로 나뉘어 분류 성질을 가진 값의 활성함수로 주로 사용된다

## Step

1.  identitiy

2.  linear

3.  binary step

4.  sign function
    `

- <img src="https://i.ibb.co/gTfPdT7/Activation-step.png" alt="Activation-step" border="0">

## Sigmoid

1. soft step( Logistic )
1. TanH
1. ArcTan
1. Softsign

- <img src="https://i.ibb.co/VCQX7PZ/Activation-sigmoid.png" alt="Activation-sigmoid" border="0">

## Relu

1. ReLU
1. Leaky ReLU
1. ELU

- <img src="https://i.ibb.co/GMrRmqK/Activation-relu.png" alt="Activation-relu" border="0">

## Other

1. softPlus

1. Thresholed ReLU

1. Bent identity

1. Gaussian
