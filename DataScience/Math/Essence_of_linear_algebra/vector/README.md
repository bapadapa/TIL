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
        - ![벡터 합](https://i.ibb.co/vYWcbG7/aa.gif)
          - [이미지 출처](https://www.3blue1brown.com/lessons/vectors)

   1. 곱
      - 곱한것 만큼 길이가 변한다
        - 위와같이 길이가 변하는 것을 `Scaling` 이라고 부른다.
          - 2를 곱하면, 길이가 2배만ㅋ큼늘어나고, 1/2를 곱하면 길이가 반으로 준다.
          - 음수를 곱하면, 방향을 바꾸고, 곱한만큼 길이가 변한다.
        - `Scaling`시 곱하는 값을 `Scalar`라고 부른다.
      - 벡터를 `Scalar`로 `Scaling` 한다는 것은 벡터의 곱과 같은 의미이다.
      - 간단 예시
        - $ 3\vec{c} = 3 ⋅ \begin{bmatrix} x \\ y \\ \end{bmatrix} = \begin{bmatrix}3x \\ 3y \\ \end{bmatrix}
          $

   - ![벡터 곱(scaling)](https://i.ibb.co/T8L4TMh/aa.gif)
     - [이미지 출처](https://www.3blue1brown.com/lessons/vectors)

## Linear combinations, span, and basis vectors

### Unit vector / 단위벡터

1. x 축
   1. 수식
      - $\hat{i}$
   1. 명칭
      1. i-hat (아이 헷)
      1. x축의 unit vector
1. x축
   1. 수식
      - $\hat{j}$
   1. 명칭
      1. j-hat (아이 헷)
      1. y축의 unit vector

- 위 2개 모두 Basis(기저)라고 부른다
  - 실질적으로 Scaling 하는 대상

## Linear Combinations ( 선형 조합)

1. 두 벡터의 `방향성이 다르다`.

   - 스칼라의 값을 자유롭게 변환시킨다면, 대부분의 벡터 쌍(의 경우 평면의 모든 점에 도달할 수 있다.
     - ![방향이 다른 선형 조합](https://i.ibb.co/nb3NHbr/aa.gif)
       - [이미지 출처](https://www.3blue1brown.com/lessons/span)
     - 2D상에서 Span에 제한이없다.

1. 두 벡터의 `방향성이 같다`

   - 직선으로 제한이 된다.
     - ![방향이 같은 선형 조합](https://i.ibb.co/HpdwqtC/aa.gif)
       - [이미지 출처](https://www.3blue1brown.com/lessons/span)
     - 2D상에서 Span이 직선으로 제한된다.

1. 두 벡터가 Zero Vectir(영벡터)라면 원점에 갇힌다.
1. Span
   - Span은 1,2번과 같이 벡터쌍의 조합으로 나타낼 수 있는 벡터 집합
   - ![1,2번 둘을 비요해주는 영상](https://i.ibb.co/zJ2gvWR/aa.gif)
     - [이미지 출처](https://www.3blue1brown.com/lessons/span)

## Vector & Point

- 간단하게 생각하면 Vector가 가르키는 `위치값(꼬리 위치)`가 Point라고 생각하면 편하다
  - 그것의 조합을 `Matrix(행열)`로 나타내 사용한다(컴퓨터 관점)
  - ![Vector & Point](https://i.ibb.co/K5Crr47/aa.gif)
    - [이미지 출처](https://www.3blue1brown.com/lessons/span)

## Linear dependent & Independent

- span의 확장(차원추가 가능 여부)에 따라 dependent와 Independent로 나뉜다.

  - ![span의 확장](https://i.stack.imgur.com/NKvYQ.gif)
    - [이미지 출처](https://newbedev.com/how-can-i-visualize-independent-and-dependent-set-of-vectors)

- 불필요한 벡터가 있어 Vector를 추가(차원증가)시켜도 Span이 학장되지 않는 것
- $\vec{u} = a\vec{v} + b\vec{w} \quad for\ some\ a\ and\ b$

- Vector중 하나가 다른 벡터들의 선형 조합으로 표현 가능한 경우
  - ![선형 종속](https://i.ibb.co/LRT5ZGw/dependent.gif)

### Linear Independent / 선형 독립

- 각 Vector가 기존 Span에 또 다른 차원을 추가하는게 가능한 것
- $\vec{u} \ne a\vec{v} + b\vec{w} \quad for\ some\ a\ and\ b$

## Linear transformations and matrices

### Linear Transformation / 선형 변환

1. Transformation (변형) == function (함수) ($f(x)$)
   1. Input이 들어가면 그에 상응하는 Output을 반환하는 것
      - Input $\vec{v}$ -> $L(\vec{v})$ -> Output $\vec{v}$
        - 이것을 vector가 이동한다고 생각하면 이해하기 편하다
1. Linear (선형)
   1. 모든 선은 변환 후에도 직선이어야한다.
      - 변환 후에도 `평행`하고 `동일한 간격`으로 `격자`가 구성되어야한다
   1. 원점은 변환 이후에도 원점이어야한다.
   1. 간단 이미지
      - ![Linear Transformaion](https://3b1b-posts.us-east-1.linodeobjects.com//content/lessons/2016/linear-transformations/question1.png)
        - [이미지 출처](https://www.3blue1brown.com/lessons/linear-transformations)
      - `C`만 Linear Transformaion이라고 볼 수 있다.
1. Linear Transformation
   1. 변환 후 에도 선형결합을 유지한다.
      - 즉 `Bias`의 비율이 유지된다.
      - ![선형 변환](https://i.ibb.co/g32GBPn/aa.gif)
        - [출처](https://www.3blue1brown.com/lessons/linear-transformations)
      - 즉 $\hat{i}$ & $\hat{j}$의 변한 정도를 안다면, $\vec{v}$를 추론할 수 있다.
1. Rotation

   - $\vec{v}$ 의 차원의 방향을 돌려준다.
     - ![Rotation](https://i.ibb.co/SNDTsTW/Rotation.gif)

1. Shear

   - $\hat{i}$ 이변하지 않는다
   - $\hat{j}$ 의 위치값은 `( 1, 1 )` 로 변한다
   - ![spear](https://i.ibb.co/7jgNKbc/aa.gif)
     - [출처](https://www.3blue1brown.com/lessons/linear-transformations)

1. Linearly dependent columns / 선형 종속 열
   - $\vec{v}$의 scaled 처럼 차원을 늘리고 비트는 과정
   - 즉 선형변환을 함으로써 2D 공간을 압축한다.
   - ![Linear Dependent](https://i.ibb.co/TbkNgdF/aa.gif)
