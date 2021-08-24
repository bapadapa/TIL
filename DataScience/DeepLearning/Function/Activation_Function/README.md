# 활성함수 Activation Function

[수식이 안보이면 클릭 후 설치](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related)

## 간단 정의

1. `Input` 에서 들어온 `값(가중치 등)`을 활성함수에 삽입하고, 각 선택한 함수에 따른 `결과값`을 `Output로` 산출하는 함수

   - 즉, `불필요한 데이터 포인트를 배제`시켜 주는 역할

2. 신경망에 비선형성을 추가하기 위해 사용

|                                                                                                                      |                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| ![과정](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d243324bcba9144370e261_Screenshot%20(205).jpg>) | ![상세](https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d2424009416f21db643e21_Group%20807.jpg) |

## 활성함수 종류

### `Step`

1. #### `identitiy`

   1. 정의
   1. 수식
   1. 그래프
   1. 장점
   1. 단점

1. #### `linear`

   1. 정의

      - 입력값과 비례하는 항등함수
        - 즉 입력값에 특정 상수를 곱한 값을 반환함

   1. 수식
      - $f(x) = X$
   1. 그래프
      - | $cx$                                                                                                                         |
        | ---------------------------------------------------------------------------------------------------------------------------- |
        | ![linear](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d244bb0e12c94fb442c01e_pasted%20image%200%20(4).jpg>) |
   1. 장점
      1. 다중출력이 가능하다.
   1. 단점
      1. Backpropagation이 불가하다.
         - `Backpropagation`
           - `Activation Fuction`을 미분하여 손실값을 줄이는 과정
         - 이유
           - Linear Fucntion의 미분값은 상수이기 때문에 불가능하다.
      1. 신경망의 모든 Layer가 1개로 함축된다.
         - 마지막 Layer는 첫 번쨰 Layer의 선형 함수기 떄문

1. #### `binary step`

   1. 수식
      - $f(n)=
         \begin{cases}
         0  & x < 0 \\
         1  & x \ge 0 \\
         \end{cases}$
   1. 정의
      - 임계값 기준으로 임계값보다 `크면 1( 활성 )`, `작으면 0(비활성)` 을 반환해주는 활성함수
        - 출력이 다음 은닉층으로 전달되지 않는다.
   1. 문제점
      1. `다중 출력을 할 수 없다`
         - A or B 와 같은 분류문제에서만 사용 가능하다.
      1. 기울기가 0이기 때문에 `역전파 과정에서 방해`가 된다.

1. #### `sign function`

- | Activation-step                                                   |
  | ----------------------------------------------------------------- |
  | ![Activation-step](https://i.ibb.co/gTfPdT7/Activation-step.png") |

---

### `Sigmoid`

1. #### `soft step( Logistic / sigmoid )`

   1. 정의
      1. S자 형태를 띄는 함수
      1. 값을 전달받으면 0~1사이의 값으로 변환하여 출력해줌.
      1. 입력값이 클수록 1, 작을수록 0으로 출력한다.
   1. 수식
      1. 함수
         - $\sigma(x) = \frac{1}{1-e^-x} $
      1. 도함수
         - $\sigma^\prime(x) = \sigma(x)(1-\sigma(x))$
   1. 그래프
      - | $\sigma(x)$                                                                                                                       | $\sigma^\prime(x)$                                                                                                                       |
        | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
        | ![$\sigma(x)$](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d24547f85f71e3bd2339f8_pasted%20image%200%20(5).jpg>) | ![$\sigma^\prime(x)$](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d2458396cfc63d0a02b0c8_pasted%20image%200%20(6).jpg>) |
   1. 장점

      1. 유연한 미분값을 가진다.
      1. 미분식이 단순하다.
      1. 값범위가 0~1사이이기 떄문에 exploding gradient(기울기 폭주)이 방지된다.

   1. 단점
      1. Vanishing Gradient이 발생할 수 있다.
      1. 기울기 중심이 0이 아니다.
         - 모든 Neuran이 양수값 을 가져서 Zigzag꼴로 합습을 하지 못하여 비용/효율면에서 불리하다.
      1. exp연산 비용이 크다.
         - 위와같은 단점 때문에 현재는 많이 사용하지 않는다.

1. #### `TanH`

   1. 정의
      1. Sigmoid가 변형된 모양이다.
         - 값의 범위가 -1~1사이다.
      1. 값이 크면 1, 작으면 -1에 가까워진다.
   1. 수식
      1. 함수
         1. $tanh(x) = 2\sigma(2x)-1$
         1. $tanh(x) = \frac{e^x-e^{-x}}{e^x + e^{-x}}$
      1. 도함수
         1. $tanh\prime(x) = 1 - tanh^2(x)$
   1. 그래프
      - | $tanh(x)$                                                                                                       | $tanh\prime(x)$                                                                                                                       |
        | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
        | ![$tanh(x)$](https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d246555e0bd43f4bf17b77_Group%2022.jpg) | ![$tanh\prime(x)$](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d245b38d468ca69828e8f5_pasted%20image%200%20(7).jpg>) |
   1. 장점
      1. Zero Centered(기울기 값의 중심이 0이다)
         - 강한 양수, 중립, 강한 음수로 쉽게 맵핑할 수 있다.
      1. `-1 ~1 사이`에 있기 때문에 일반적으로 은닉층에서 사용된다.
         - 데이터를 중앙에 배치하기 좋고, 다음 계층에 대한 학습이 쉬워진다.
   1. 단점
      1. 지수함수를 사용하여 `Overflow`가 생길 수 있다.
      1. Vanishing Gradient(기울기 소실)가 생길 수 있다.
         - 중심이 0이기 때문에 특정 방향으로만 편향되지 않는다
         - 위와같은 이유 때문에 Sigmoid보다 선호된다

1. #### `ArcTan`

   1. 정의
   1. 수식
   1. 그래프
   1. 장점
   1. 단점

1. #### `Softsign`

   1. 정의
   1. 수식
   1. 그래프
   1. 장점
   1. 단점

- | Activation-sigmoid                                                     |
  | ---------------------------------------------------------------------- |
  | ![Activation-sigmoid](https://i.ibb.co/VCQX7PZ/Activation-sigmoid.png) |

---

### `ReLU`

1. #### `Relu(Rectified Linear Unit )`

   1. 정의

      1. 이하의 값은 뉴런에서 비활성화를 시켜 부분적 정보 만 수용하는 함수
      1. CNN에서 좋은 성능을 갖고 있다.
      1. 딥러닝에서 가장 많이 사용한다.
      1. 처음 `DeepLearning Layer`를 구성할때 `Hidden Layer`의 `Activation Function`을 `Relu`로 구성 후, 필요에 따라 변경시키는 것이 좋다.

   1. 수식
      1. 함수
         - $f(x) = max(0,x)$
      1. 도함수
         - $f\prime(n)=\begin{cases}0  & x < 0 \\1  & x \ge 0 \\\end{cases}$
   1. 그래프
      - | $f(x)$                                                                                                    | $f\prime(n)$                                                                                                                                                                         |
        | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        | ![$max(0,x)](https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d24d1ac2cc1ded69730feb_relu.jpg) | ![$f\prime(n)=\begin{cases}0  & x < 0 \1  & x \ge 0 \end{cases}$](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d2472c7c7683854f329e45_pasted%20image%200%20(9).jpg>) |
   1. 장점

      1. 특정 뉴런만 활성화 되어 Sigmoid,tanH등과 비교하여 연산이 빠르다.
      1. `비포화 속성(Non - Saturation)`이여서 경사하강의 수렴이 가속화된다.

         - 비포화 속성(Non - Saturation)
           - 간단히 말하면 출력의 범위가 제한되지 않는다.

      1. 비선형함수이다.
         - backpropagation을 허용한다.

   1. 단점
      1. Dying Relu(음수에서 모든 값이 0이된다.)
         - Backpropagtion시 일부 뉴런이 갱신되지 않는다
         - 훈련 모델의 성능(기능)이 감소될 수 있다.

1. #### `Leaky Relu`

   1. 정의

      1. Relu의 Dying Relu를 개선한 버전의 Relu
      1. 음수값에서도 Backpropagation을 수행할 수 있다.

   1. 수식
      1. 함수
         - $f(x) = max(0.1x,x)$
      1. 도함수
         - $f\prime(x) = \begin{cases}0.1 &, x\le 0\\1&, x\>0\\\end{cases}$
   1. 그래프
      |$f(x)$|$f\prime(x)$|
      |-|-|
      |![$f(x) = max(0.1x,x)$](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d2474e3a0f7a4010b6129e_pasted%20image%200%20(10).jpg>) | ![$\begin{cases}0.1, x\le 0\1, x>0\end{cases}$](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d248619e91e2238803bb97_pasted%20image%200%20(11).jpg>)|
   1. 장점
      1. Dying Relu 문제를 방지한다.
      1. 연산이 빠르다.
      1. Relu보다 균현적인 값을 반환한다.
   1. 단점
      1. 항상 Relu보다 좋은 결과를 얻는 것이 아니다.
         - 단순히 대안책이라고 보면 된다.
      1. 음수값에 대한 예측이 일관되지 않을 수있다.

1. #### 'PReLU`

   1. 정의
      1. `Leaky ReLU`와 거이 유사하다.
      1. 다른부분은 $\alpha$값(음수값의 기울기)을 지정할 수 있다.
         - Backpropagation연산을 통해 적절한 $\alpha$값을 알아낼 수 있다.
   1. 수식
      1. 함수
         - $f(x) = max(\alpha x,x)$
      1. 도함수
         - $f\prime(x) = \begin{cases}\alpha \qquad , x\le 0\\1 \qquad , x\>0\\\end{cases}$
   1. 그래프
      |$f(x)$|$f\prime(x)$|
      |-|-|
      |![$f(x) = max(0.1x,x)$](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d24887a3d0cc7966aa0aa7_pasted%20image%200%20(12).jpg>) | ![$\begin{cases}0.1, x\le 0\1, x>0\end{cases}$](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d248619e91e2238803bb97_pasted%20image%200%20(11).jpg>)|
   1. 장점
      1. 유동적으로 $\alpha$값을 설정할 수 있다.
   1. 단점
      1. 유동적으로 $\alpha$값을 설정할 수 있다.
         - 절절히 설정해야한다.

1. #### `ELU ( Exponential Linear Unit )`

   1. 정의
      1. 음수 부분의 기울기를 $\exp$를 적용하여 표현한다.
         - 음수 부분을 $\log$ 곡선을 이용하여 표현한다
   1. 수식
      1. 함수
         - $\begin{cases} x & for x \ge 0 \\ \alpha(e^x -1) & for x < 0 \end{cases} $
      1. 도함수
         - $\begin{cases} 1 & for x \ge 0 \\ f(x) + \alpha & for x < 0 \end{cases} $
   1. 그래프
      |$f(x) \qquad + \qquad f\prime(x)$|
      |-|
      | ![ELU + Derivative](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d248fe0377d17681762682_pasted%20image%200%20(14).jpg>)|
   1. 장점

      1. Dying ReLU의 문제점을 해결했다.
      1. $-\alpha$ 가 될 떄 까지 기울기값이 완만하다
      1. 네트워크가 Weight 와 Bais가 적절히 이동하는데 도움이 된다.

   1. 단점
      1. $\exp$연산을 하여 `Cost`가 높다.
      1. $\alpha$값에 대한 학습이 없다.
      1. `Exploding Gradddient`(기울기 포화/폭발) 문제가 야기된다.
         - Exploding Gradddien
           - Weight/Bais 값이 너무 커진다.

- | Activation-relu                                                  |
  | ---------------------------------------------------------------- |
  | ![Activation-relu](https://i.ibb.co/GMrRmqK/Activation-relu.png) |

---

### `ETC`

1.  #### `softPlus`

    1. 정의
       - Sigmoid의 적분값
    1. 수식
       1. 함수
          - $f(x) = \ln(1+e^x) $
       1. 도함수
          - $f\prime(x) = \frac{1}{1+e^{-x}} = \sigma(x)$
    1. 그래프
       - | $f(x) \qquad + \qquad f\prime(x)$                                                          |
         | ------------------------------------------------------------------------------------------ |
         | ![https://subinium.github.io/introduction-to-activation/](https://i.imgur.com/U25SJPS.png) |
    1. 장점
       1. ReLU와 다르게 결정 경계가 부드럽다.
    1. 단점
       1. 경계가 부드러워 `정규화에서 약점`을 보인다.
       1. ReLU보다 `속도가 느리다`.

1.  #### `Bent identity`

    1. 정의
    1. 수식
       1. 함수
          - $f(x) = \frac{\sqrt{x^2+1}-1}{2} + x$
       1. 도함수
          - $f\prime(x) = \frac{x}{\sqrt{x^2+1}} + 1$
    1. 그래프
       - |                                                                                                               |
         | ------------------------------------------------------------------------------------------------------------- |
         | ![Activation_bent_identity](https://upload.wikimedia.org/wikipedia/commons/c/c3/Activation_bent_identity.svg) |
    1. 장점
    1. 단점

1.  #### `Gaussian`

    1. 정의
    1. 수식
       1. 함수
          - $f(x) =  e^{-x^2}$
       1. 도함수
          - $f\prime(x) =  -2xe^{-x^2}$
    1. 그래프
       - |                                                                                                     |
         | --------------------------------------------------------------------------------------------------- |
         | ![Activation_gaussian](https://upload.wikimedia.org/wikipedia/commons/f/fe/Activation_gaussian.svg) |
    1. 장점
    1. 단점

- | ETC                                      |
  | ---------------------------------------- |
  | ![ETC](https://i.ibb.co/0X7vQp0/ETC.png) |

---

### `Other`

1. #### `Thresholed ReLU`

   1. 정의
      - 임계치를 지정한 ReLU
      - $\theta = 0$ 일시 ReLU와 동일하여 일부 분제의 대안으로 사용한다.
   1. 수식
      - $f(x , \theta) = \begin{cases} 0, & x \le 0 \\ x, & x> 0 \end{cases}$

1. #### `Swish`

   1. 정의
      1. 구글에서 개발한 활성함수
      1. SiLu ( Sigmoid Liinear Unit)이라고도 부른다.
      1. 이미지 분류, 번역 등에서 많이 사용한다.
      1. DeepLearnig에서 ReLU와 비슷/이상의 성능을 갖는다
   1. 수식
      1. 함수
         - $f(x) = \frac{x}{1+e^{-x}} = x \times \sigma (x)$
      1. 도함수
         - $f\prime(x) = f(x) + \sigma(x)(1-f(x))$
      - $\sigma$ == `sigmoid`
   1. 그래프
      - | f(x)                                                                                                                         |
        | ---------------------------------------------------------------------------------------------------------------------------- |
        | ![swish](<https://assets.website-files.com/5d7b77b063a9066d83e1209c/60d24c9fa6b752098fd3f047_pasted%20image%200%20(16).jpg>) |
   1. 장점
      - 음수 부분의 기울기 값의 변화가 부드럽다.
      - 단조롭지 않아 합습할 가중치 및 입력 데이터의 표현이 향상됨
      - DeepLearnig Layer구성시 `깊은층`(Layer 수가 많음)일 때 엄청난 효율을 보인다.
   1. 단점
      - DeepLearnig Layer구성시 `얕은층`(Layer 수가 적음)일 때 엄청난 효율을 보이지 않는다.

1. #### `softmax`

   1. 정의
      - 입력받은 값을 0~1사이의 값으로 정규화후 출력해 주고, 값의 합은 항상 `1`이된다
      - 주로 `출력층 (Output Layer)`에서 사용이
        된다.
      - `예측(Prediction)` 및 `분류(Classification)`로 나뉘어 분류 성질을 가진 값의 활성함수로 주로 사용된다
   1. 수식
      - $$y_k = \frac{\exp(a_k)}{\sum_{i=1}^n\exp(a_i)}$$
   1. 장점
      1. `다중 분류`에 적용이 가능하다.
      1. 정규화 기능을 갖고 있다.
   1. 단점
      1. 지수함수를 사용하여 `Overflow` 위험이 있다.

1. #### `maxout`

   1. 정의
      - `Dropout`의 `효과를 극대화` 시키기 위해 고안된 `Activation Function(활성함수)`다
      - 여러개의 출력으로 이루어진 활성함수다
   1. 수식
      - $f(\vec{x}) = \underset{i}\max x_i$

---

## 참고

1. [v7labs](https://www.v7labs.com/blog/neural-networks-activation-functions)
1. [subinium](https://subinium.github.io/introduction-to-activation/)
