# 넘파이를 공부해보자~

`다 작성하면, 디렉토리로 구분할 예정`

<details>
<summary>목차들</summary>  
<div markdown="1">

- [기본정의](#기본정의)

</div>
</details>
<br>

---

# 기본정의

- > 파이썬에는 List는 있지만, 배열(Array)를 제공하지 않는다 <br>
  > 데이터 처리시 속도 및 메모리 측면에서 배열이 빠르다. <br>
  > 그 배열을 사용 할 수 있게 만들어주는 패키지 이다.

- Numpy를 이용하여 배열을 만든다면, `ndarray class객체` 즉 `배열`로 선언이 된다.

  - ndarray는 `N-dimensional Array`의 약자이다.

- 내부적으로는 C로 구현되어, 파이썬의 반복문에 비해 더 빠르다.
- 벡터화 연산을 하기때문에, `선형 대수 연산`에 유리하다.

## 간단규칙

1.  모든 원소는 같은 자료형이다.

    - 연속적인 메모리 배치를 가진다!

2.  원소의 갯수를 바꿀 수 없다.

## 임포트 (Import)

- conda로 설치하였다면 , 기본적으로 설치되어있다.

- ```python
  import numpy as np
  ```
  - 관례적으로 numpy는 `np`로 임포트 해준다.

## 구조

- 데이터 자체를 나타낸다.
- data-type은 array의 단일 고정 크기 요소의 레이아웃 정보이다.
- array scalar는 배령의 요소에 엑세스 될 때 반환되는 배열이다.
- array는 모든 원소가 동일한 data-type을 갖는다.
  - 연속적인 메모리 배치를 가진다!
- numpy 모듈의 array함수를 사용하여 생성한다.

## 차원

- ndarray는 1차원 배열의 특징을 가지며 `차원`, `타입` , `요소`를 갖고 있다.
- 2차원은 1차원 여러개의 배열로 구성된다.
  - matrix와 동일한 구조다.
  - 구조는 동일하지만, matrix는 아니다.
- n차원은 여러 n-1차원의 배열로 구성된다.

- 1차원
  - ````python
    oneDimArray = np.array([ 1,2,3 ])
        ```
    ````
- 2차원

  - ```python
    twoDimArray = np.array([[ 1,2,3] ,[ 4,5,6 ]])
    ```

- 3차원

  - ```python
        threeDimArray = np.array([
            [ [1,2,3],[4,5,6] ],
            [ [7,8,9],[10,11,12] ]
        ])
    ```

## 벡터 연산

- ```python
    oneDimArray = np.array([1,2,3])
    print(oneDimArray * 2)
  ```

  - `결과값 : [2,4,6]`

- ```python
    oneDimArray = np.array([1,2,3])
    print(oneDimArray * 2 + oneDimArray)
  ```

  - `결과값 : [3,6,9]`
    - [2,4,6] + [1,2,3]

## 속성

- np.ndim

  - 구할 ndarray의 차원을 반환
  - ```python
      print(oneDimArray.ndim) # 1 출력 ( 1차원이란 뜻 )
      print(twoDimArray.ndim) # 2 출력 ( 2차원이란 뜻 )
      print(threeDimArray.ndim) #3 출력 ( 3차원이란 뜻 )
    ```

- np.shape

  - (n X m) 과 같은 형식으로 크기 반환
  - ```python
      print(oneDimArray.shape) # (3,) 출력 (3크기 배열)  (행)
      print(twoDimArray.shape) # (2,3) 출력 ( 2x3크기 배열) (열,행)
      print(threeDimArray.shape) # (2,2,3) 출력 ( 2x2x3크기 배열) (깊이,열,행)
    ```

  - np.dtype
    - 원소 타입 확인
  - np.astype('`자료형`')
    - 타입 변환
  - ```python
    dt = np.array(range(10))
    print(dt.dtype) # int32 출력
    dt = dt.astype('float32')
    print(dt.dtype) # float32 출력
    ```

- np.T

  - 객체의 전치된 형태
  - ```python
    twoDimArray = np.array([[ 1,2,3 ],[ 4,5,6 ]])
    print(twoDimArray.T)
    ```
    - 결과값 `[[1 4] [2 5] [3 6]]`

## 인덱싱 및 조회(슬라이싱)

### 인덱싱

- ```python
  twoDimArray = np.array([1,2,3],[4,5,6])
  print(twoDimArray[0,0]) # 1 출력 [행,열]
  print(twoDimArray[0,1]) # 2 출력
  print(twoDimArray[0,-1]) # 3 출력
  ```

### 슬라이싱

- ```python
  twoDimArray = np.array([1,2,3],[4,5,6])
  # [1,2,3] 출력 [행,열] 1번째 행 모두 출력
  print(twoDimArray[0,:])
  # [1,4] 출력 1번째 열 모두 출력
  print(twoDimArray[:,0])
  # [2,3] 출력 1번째 행 2번째 열부터 끝까지 출력
  print(twoDimArray[0,1:])
  ```
  - [시작 : 끝 : 간격(step)]
    - 시작 기본값 : 0
    - 끝 기본값 : -1 (마지막)
    - 간격 기본값 : 1 (순방향) , -1 : (역순)
      - -2 : 역순으로 2칸씩이동

### 조건부 조회

- ndarray에 비교연산자 사용
  - 각 원소에 대해 boolean(True/False) type으로 구성된 ndarray반환
  - 반환된 ndarray를 활용하여 True인 것만 조회가능
  - 조건에 따른 원소 변경 가능
- boolean배열로 조회
  - 배열명[boolean]
- 예시
  - 코드
    - ```python
      arr = np.array([1,2,3,4])
      arr[arr>2]
      ```
  - 결과값
    - `array([3, 4])`

## 데이터 타입

- 동일한 데이터 타입을 갖는다.

  - 분석 알고리즘마다 지원하는 데이터 타입이 다르기 때문에 조심해야한다.

- 종류

  - | 종류         | 설명                                                                                |
    | ------------ | ----------------------------------------------------------------------------------- |
    | `bool_`      | Boolean (True or False) stored as a byte                                            |
    | `int_`       | Default integer type (same as C `long`; normally either `int64` or `int32`)         |
    | `intc`       | Identical to C `int` (normally `int32` or `int64`)                                  |
    | `intp`       | Integer used for indexing (same as C `ssize_t`; normally either `int32` or `int64`) |
    | `int8`       | Byte (-128 to 127)                                                                  |
    | `int16`      | Integer (-32768 to 32767)                                                           |
    | `int32`      | Integer (-2147483648 to 2147483647)                                                 |
    | `int64`      | Integer (-9223372036854775808 to 9223372036854775807)                               |
    | `uint8`      | Unsigned integer (0 to 255)                                                         |
    | `uint16`     | Unsigned integer (0 to 65535)                                                       |
    | `uint32`     | Unsigned integer (0 to 4294967295)                                                  |
    | `uint64`     | Unsigned integer (0 to 18446744073709551615)                                        |
    | `float_`     | Shorthand for `float64`.                                                            |
    | `float16`    | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa                   |
    | `float32`    | Single precision float: sign bit, 8 bits exponent, 23 bits mantissa                 |
    | `float64`    | Double precision float: sign bit, 11 bits exponent, 52 bits mantissa                |
    | `complex_`   | Shorthand for `complex128`.                                                         |
    | `complex64`  | Complex number, represented by two 32-bit floats                                    |
    | `complex128` | Complex number, represented by two 64-bit floats                                    |

- INF와 nan
  - np.inf (infinity)
    - 무한대를 표현해준다. inf / -inf 로 표현된다.
    - log(0)을 연산 하면, `-inf`가 나온다.
  - np.nan (not a number)
    - 정의 할 수 없는 숫자를 표현한다.
    - 0/0 을 연산하면, `nan`이 나온다.

## 배열 생성

- 대부분의 배열선언시, (dtype= '`자료형`')을 이용하여 자료형은 지정해 줄 수 있다.

  - np.array([1,2,3,4,5] , dtype = 'float')

- np.array

  - array 값을 직접 입력
    - np.array([원소])
    - ```python
      np.array([1,2,3,4,5])
      # 출력 : array([1, 2, 3, 4, 5])
      ```

- np.ndarray

  - shape을 입력하면 random normal 값으로 shape에 맞게 생성

    - np.ndarray(shape) shape=(5,3,2)
    - ```python
      np.ndarray((2,2))
      # 출력 : 무작위 값입!
      # array([[2.12199579e-314, 1.12041378e-311],
      # [3.20154539e-321, 3.79442416e-321]])
      ```

- np.ones
  - shape을 입력하면 1로 채워 shape에 맞게 생성
    - np.ones(shape)
    - ```python
      np.ones((2,2,2))
      # 출력 : 모든 곳을 1로 체워준다!
      # array([[[1., 1.], [1., 1.]],
      #       [[1., 1.],[1., 1.]]])
      ```
  - ones_like (`배열명`)
    - 선언시 튜플(크기)를 지정하지 않고 다른 배열의 크기와 동일하게 선언하고 싶을 시 사용한다.
- np.zeros

  - shape을 입력하면 0으로 채워 shape에 맞게 생성
    - np.zeros(shape)
    - ```python
      np.zeros((2,2,2))
      # 출력 : 모든 곳을 0으로 채워준다!
      # array([[[0., 0.],[0., 0.]],
      #        [[0., 0.],[0., 0.]]])
      ```
  - zeros_like (`배열명`)
    - 선언시 튜플(크기)를 지정하지 않고 다른 배열의 크기와 동일하게 선언하고 싶을 시 사용한다.

- np.empty
  - 비어 있는 ndarray 생성
    - 배열을 초기화하는데 시간이 오래걸림으로, 그 때 사용한다.
    - np.empty(shape)
    - ```python
      np.empty((3,5))
      # 출력 : 빈 배열이지만, 쓰레기값이 들어있는 경우도 있음
      # array([
      # [0., 0., 0., 0., 0.],
      # [0., 0., 0., 0., 0.],
      # [0., 0., 0., 0., 0.]])
      ```
- np.identity
  - 대각선이 1인 정방행렬(`단위행렬`) 생성
    - np.identity(n) n = 행수(rows)
    - ```python
      np.identity(4)
      # 출력 : 무작위 값입!
      # array([
      # [1., 0., 0., 0.],
      # [0., 1., 0., 0.],
      # [0., 0., 1., 0.],
      # [0., 0., 0., 1.]])
      ```
- np.eye
  - 대각선이 1인 정방행렬, k값에 따라 1이되는 열의 위치가 달라짐
    - np.eye(n,k) k(default=0)
    - ```python
      np.eye(4 , k =-1)
      # 출력 : 무작위 값입!
      #array([
      # [0., 0., 0., 0.],
      # [1., 0., 0., 0.],
      # [0., 1., 0., 0.],
      # [0., 0., 1., 0.]])
      ```
- np.linspace
  - start 부터 stop까지 num(`개수`)에 정의된 값만큼의 배열을 균일한 간격으로 생성
    - np.linspace(start,stop,num)
    - ```python
      np.linspace(0,60,10)
      # 출력 : 0~60까지의 10개의 구간을 배열로 생성
      #array([ 0.        ,  6.66666667, 13.33333333, 20.        , 26.66666667,       33.33333333, 40.        , 46.66666667, 53.33333333, 60.        ])
      ```
  - np.logspace
    - 로그 구간으로 구분하고 싶다면, 사용한다.
- np.arange
  - range 함수와 비슷하게 사용되며, ndarray를 반환 하게 됨
    - np.arange(start,stop,step)
    - ```python
      np.arange(0,60,2)
      # 출력 : 0,60까지 2칸씩 띄어지는 배열
      #array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58])
      ```

## 배열 복사

- np.copy를 이용하여 복사한다.
- 단순히 삽입 `a = b` 로 복제한다면, 깊은복사(a의 값이 변경되면 b도 변경됨.)가 된다.
  - 이것을 방지하기위해 `a = b.copy()`를 사용하여 얕은복사(a의 값이 변경되도, b가 변경되지 않음)을 할 수 있다.

## 난수 발생 모듈

- random 모듈과 사용 함수
  - random 모듈 사용 : np.random.함수명
  - random 모듈의 함수확인 dir(np.random)
  - replace : return 값으로 기존 값을 변경시켜줌 (True : 복원, False : 비복원)
- random 모듈에서 많이 사용하는 함수의 기능

  - seed : np.random.seed(`num`) seed의 num을 통한 난수생성(동일한난수발생)
    - seed를 바꾸지 않으면 같은 난수 발생
    - 예시 : `np.random.seed(10)`
  - randint : np.random.randint(`start`,`stop`,`num`) 균일분포의 정수 난수 생성
    - 예시 : `np.random.randint(1,10,10) `
    - 결과값 : `array([3, 7, 3, 9, 9, 7, 7, 6, 7, 1])`
  - rand : np.random.rand(`shape`) 0부터 1사이의 균일분포에서 난수 matrix array 생성
    - `shape`에 삽입한 크기에 따라 `return`하는 크기가 다름
    - 예시 : `np.random.rand(2,2)`
    - 결과값 : `array([[0.59758229, 0.87239246],[0.98302087, 0.46740328]])`
  - randn : np.random.randn(`shape`) 표준 정규 분포에서 난수 matrix array 생성
    - 예시 : `np.random.randn(2,2)`
    - 결과값 : `array([[ 0.98925209, 0.25922513],[-0.02419319, 0.35849666]])`
  - shuffle : np.random.shuffle(obj) obj 데이터의 순서바꾸기
    - 예시
      - ```python
        obj = [1,2,3,4]
        np.random.shuffle(obj)
        obj
        ```
      - 결과 값 : `[2, 3, 1, 4]`
  - choice : np.random.chice([`배열`],`갯수`)

    - 예시 :`np.random.choice([1,2,3,4],4,replace=False)`
    - 결과값 : `array([2, 4, 1, 3])`

# 함수

## axis(축)

- 개념
  - axis 에서 0 : 행, 1 : 열을 나타낸다
  - numpy에서 axis를 기준으로 `행(0)` 혹은 `열(1)`연산을 할 수 있다.

## 자주 사용하는 함수들

- 아래 함수들은 필요할때 사용하면 된다.
  - square() : 거듭제곱
  - sqrt() : 제곱근
  - power(a,b) : 두배열의 거듭제곱
  - hypot(a,b) : a와 b의 거리 ![수식](https://latex.codecogs.com/svg.image?%5Cbg_white%20%5Cinline%20%5Csqrt%7Ba%5E2+b%5E2)
  - ceil : 각 원소보다 같거나 큰 정수 반환
  - floor : 각 원소보다 같거나 작은 정수 반환
  - rint : 각 원소의 소수점 반올림

## where함수(정말 빠르다 잘 사용하자)

- `간단히 3항연산자라고 생각하면 편하다.`
- where
  - 사용법
    - np.where(조건식,참일때값,거짓일때값)
    - np.where(조건식) 조건식만 있을때는 조건에 맞는 원소 위치 반환
- Unique : 중복 제거 후 출력 함수
  - 사용법
    - np.unique(ndarray)
    - np.unique(ndarray,`return_counts=True`)
      - `return_counts=True`로 함으로써 중복된 값의 개수를 알 수 있다.
- where & unique 예시
  - 코드
    - ```python
      # -10 ~ 10 까지의 값중 10개를 랜덤으로 추출하여
      arr = np.random.randint(-10,10,10)
      # 랜덤원소가 음수일 경우 -1, 양수일 경우 1로 값이 할당된 배열을   만들면
      print(arr)
      signed_arr = np.where(arr>0,1,-1)
      print(signed_arr)
      # unique한 것을 출력(-1,1)을 출력
      np.unique(signed_arr, return_counts=True)
      #위의 식에서 0이 나왔을 경우 0으로 할당하도록 코드 작성
      ```
  - 출력 <br>`[ 6 2 -10 7 5 2 -2 0 3 1]`<br>`[ 1 1 -1 1 1 1 -1 -1 1 1]`<br> `(array([-1, 1]), array([3, 7], dtype=int64))`

## Numpy 중요 메소드

- reshape<sup>**\***</sup> : 배열의 모양을 변경

  - 전체 원소 수가 변경하려는 shape의 수와 같아야 한다
  - array_obj.reshape(변경할shape)
  - 예시
    - 코드
      - ```python
        arr = np.array(range(10))
        arr.reshape(2,5)
        ```
    - 결과
      - `array([[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]])`

- flatten() / ravel() : 1차원 배열로 변환
  - flatten() / ravel() 은 동일한 결과를 return한다.
  - 코드
    - ```python
      arr = np.array([range(5),range(5)])
      arr.flatten()
      # arr.ravel()
      ```
  - 결과
    - `array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4])`

### 함수들

- `np.concatenate`

  - array를 연결하는 함수로 여러 array를 한번에 연결
  - axis 옵션을 통해 row, column기준으로 연결 가능
  - 예시
    - 코드
      - ```python
        c1 = np.arange(1,5)
        c2 = np.arange(5,9)
        c3 = np.arange(9,11)
        np.concatenate((c1,c2,c3))
        ```
    - 결과
      - `array([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`

- 행 연결 (col 추가)
  - `np.hstack`
    - 행 수가 같은 2개 이상의 배열을 옆으로 연결한다.
  - `np.r\_`
    - hstack과 동일한 기능을한다
    - 차이점
      - ()가 아닌 []를 이용하여 배열을 입력한다.
- 열 연결 (row 추가)
  - `np.vstack`
    - 열 수가 같은 2개 이상의 배열을 위아래로 연결한다.
  - `np.c\_`
    - vstack과 동일한 기능을한다
    - 차이점
      - ()가 아닌 []를 이용하여 배열을 입력한다.
- `np.dstack`
  - 깊이 방향으로 배열을 합친다.
  - 개인적 이해
    1. a,b배열이 있다면, a의 1행 b의 1행을 `hstack`으로 묶는다
    2. 위 과정을 순차적으로한다.
    3. 과정이 끝나면 모든 배열을 `vstack`으로 묶어준다.
- `np.stack`
  - 사용자가 지정한 차원(축으로) 배열을 연결한다.
  - axis를 이용하여 묶는 방법을 결정한다.
- `np.tile`
  - 동일한 배열을 반복하여 연결해줌.
  - 파이썬함수 repeat과 유사.
- `np.split`
  - Array 자르기!
  - ```ipython
    np.split(arr, integer) # integer 등분
    np.split(arr, 1-D array) # 구간 [n, m] : 0 ~ n-1, n ~ m - 1, m ~ len(arr)  ( index 기준 )
    ```
  - 예시
    - 코드
      - ```ipython
        x = [1, 2, 3, 99, 99, 3, 2, 1,1, 2, 3, 99, 99, 3, 2, 1]
        x1, x2, x3 ,x4 = np.split(x, [3,5,7])
        print(x1, x2, x3,x4)
        ```
    - 결과값
      - `[1 2 3] [99 99] [3 2] [ 1 1 2 3 99 99 3 2 1]`

## 범용함수 Ufunc :vectorized operation

### 벡터 계산

- 속도
  - '%timeit'을 이용하여 Operator(+,-,\*,/ ...)를 사용한 것 보다 np.함수를 사용한게 약 `2000배` 빨랐다.
  - ```ipython
    big_array = np.random.randint(1, 100, size=1000000)
    %timeit compute_reciprocals(big_array)
    %timeit (1.0 / big_array)
    ```
  - `8.14 s ± 1.02 s per loop (mean ± std. dev. of 7 runs, 1 loop each) 3.79 ms ± 1.09 ms per loop (mean ± std. dev. of 7 runs, 100 loops each)`

### - 산술연산

| Operator | Equivalent ufunc  | Description                           |
| -------- | ----------------- | ------------------------------------- |
| `+`      | `np.add`          | Addition (e.g., `1 + 1 = 2`)          |
| `-`      | `np.subtract`     | Subtraction (e.g., `3 - 2 = 1`)       |
| `-`      | `np.negative`     | Unary negation (e.g., `-2`)           |
| `*`      | `np.multiply`     | Multiplication (e.g., `2 * 3 = 6`)    |
| `/`      | `np.divide`       | Division (e.g., `3 / 2 = 1.5`)        |
| `//`     | `np.floor_divide` | Floor division (e.g., `3 // 2 = 1`)   |
| `**`     | `np.power`        | Exponentiation (e.g., `2 ** 3 = 8`)   |
| `%`      | `np.mod`          | Modulus/remainder (e.g., `9 % 4 = 1`) |

### 절댓값(Absolute value)

- 절댓값을 구할때 abs()함수 이용하면 된다.
  - 파이썬 내장함수 및 numpy함수가 있다.
  - 예시
    - ```python
      # python 내장 함수
      x = np.array([-2, -1, 0, 1, 2])
      abs(x)
      # numpy 함수
      np.absolute(x) #  np.abs(x)
      ```
  - 결과
    - `array([2, 1, 0, 1, 2])`

### 삼각함수

- 삼각함수 연산시 사용
  - | 함수명 | numpy함수   |
    | ------ | ----------- |
    | sin    | np.sin()    |
    | cos    | np.cos()    |
    | tan    | np.tan()    |
    | arcsin | np.arcsin() |
    | arccos | np.arccos() |
    | arctan | np.arctan() |

### 지수 로그

- | 함수명   | numpy함수 |
  | -------- | --------- |
  | 지수함수 | np.exp()  |
  | 로그     | np.log()  |
  - np.lon`n`()
    - n값에 따라 로그 n으로 변경시킬 수 있다.
    - `np.log2()`,`np.log10()`, 등.

### out 옵션

- 위 연산식에 `out = 변수명`옵션을 사용하여 output 을 지정할 수 있다.
- 주의사항 : 연산시 연산가능한 크기(두 배열의 크기)를 잘 맞춰줘야 에러가 발생하지 않는다.
- 예시
  - 코드
    - ```python
      x = np.arange(5)
      np.multiply(x, 10, out=z) # output 지정
      z
      ```
  - 결과값
    - `array([ 0, 10, 20, 30, 40])`

## 집합 함수( aggregation func )

### aggregation functions

| Function Name   | NaN-safe Version   | Description                               |
| --------------- | ------------------ | ----------------------------------------- |
| `np.sum`        | `np.nansum`        | Compute sum of elements                   |
| `np.prod`       | `np.nanprod`       | Compute product of elements               |
| `np.mean`       | `np.nanmean`       | Compute mean of elements                  |
| `np.std`        | `np.nanstd`        | Compute standard deviation                |
| `np.var`        | `np.nanvar`        | Compute variance                          |
| `np.min`        | `np.nanmin`        | Find minimum value                        |
| `np.max`        | `np.nanmax`        | Find maximum value                        |
| `np.argmin`     | `np.nanargmin`     | Find index of minimum value               |
| `np.argmax`     | `np.nanargmax`     | Find index of maximum value               |
| `np.median`     | `np.nanmedian`     | Compute median of elements                |
| `np.percentile` | `np.nanpercentile` | Compute rank-based statistics of elements |
| `np.any`        | N/A                | Evaluate whether any elements are true    |
| `np.all`        | N/A                | Evaluate whether all elements are true    |

### reduce, accumulate

- reduce : 연산결과만 출력(최종값)
- 예시
  - 코드
    - ```python
      x = np.arange(1, 6)
      np.add.reduce(x)
      ```
  - 결과
    - `15`
- reduce : 연산결과를 중첩시킴
- 예시
  - 코드
    - ```python
      print(np.add.accumulate(x))
      print(np.cumsum(x))
      ```
  - 결과
    - `[ 1 3 6 10 15] [ 1 3 6 10 15]`
