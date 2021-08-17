# 벡터

## 관점

1. 물리학
   - 벡터 : 길이와 방향을가진 공간의 화살표
     - 2차원이면 2차원 벡터
     - 3차원이면 3차원 벡터
1. CS
   - 순차 숫자 리스트
   - $
     \begin{bmatrix}
     0 \\
     1 \\
     2 \\
     3 \\
     \end{bmatrix}
     $
1. ## 수학자
   -

## 선형대수에서의 벡터

1. 의미

   - 일반적으로 `방향 및 길이`를 뜻하고, 물리학에서는 어떤 좌표 에서도 사용하지만, 선형대수학에서는 주로 `원점(Origin)`에서 시작하는 경우가 대부분이다.

1. 벡터의 좌표

   - 숫자 쌍이다. (원점(Origin)으로 부터의 `거리(좌표)`)

   - `모든 벡터`는 `대응`되는 `숫자 쌍(좌표,값)`이 있다.

1. 벡터의 션산
   1. 합
      - 벡터의 `이동량`이라고 생각하면 된다.
        - $
          \begin{bmatrix}
          1 \\ 2 \\
          \end{bmatrix} + \begin{bmatrix}
          3 \\ -1 \\
          \end{bmatrix} = \begin{bmatrix}
          1+3 \\ 2+(-1) \\
          \end{bmatrix}
          $
        - $
          \begin{bmatrix}
          x_1 \\ x_2 \\
          \end{bmatrix} + \begin{bmatrix}
          y_1 \\ y_2 \\
          \end{bmatrix} = \begin{bmatrix}
          x_1 + x_2 \\ y_1+y_2 \\
          \end{bmatrix}
          $
          - 좌표값 -> $\begin{bmatrix}
            X \\ Y \\
            \end{bmatrix}$
        - ![벡터 합](https://mathinsight.org/media/image/image/vector_parallelogram_law.png)
   1. 곱
      - 곱한것 만큼 길이가 변한다
        - 위와같이 길이가 변하는 것을 `Scaling` 이라고 부른다.
          - 2를 곱하면, 길이가 2배만ㅋ큼늘어나고, 1/2를 곱하면 길이가 반으로 준다.
          - 음수를 곱하면, 방향을 바꾸고, 곱한만큼 길이가 변한다.
        - `Scaling`시 곱하는 값을 `Scalar`라고 부른다.
      - 벡터를 `Scalar`로 `Scaling` 한다는 것은 벡터의 곱과 같은 의미이다.
      - 간단 예시
        - $
        3 * \begin{bmatrix}
        x \\ y \\
        \end{bmatrix} = \begin{bmatrix}
        3x \\ 3y \\
        \end{bmatrix}
        $
   - ![벡터 곱](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Scalar_multiplication_of_vectors2.svg/250px-Scalar_multiplication_of_vectors2.svg.png)
