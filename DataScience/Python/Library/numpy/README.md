# 넘파이를 공부해보자~

- 기본 정의

  - > 파이썬에는 List는 있지만, 배열(Array)를 제공하지 않는다 <br>
    > 데이터 처리시 속도 및 메모리 측면에서 배열이 빠르다. <br>
    > 그 배열을 사용 할 수 있게 만들어주는 패키지 이다.

  - Numpy를 이용하여 배열을 만든다면, `ndarray class객체` 즉 `배열`로 선언이 된다.

    - ndarray는 `N-dimensional Array`의 약자이다.

  - 내부적으로는 C로 구현되어, 파이썬의 반복문에 비해 더 빠르다.
  - 벡터화 연산을 하기때문에, `선형 대수 연산`에 유리하다.
  - 간단 규칙
    1. 모든 원소는 같은 자료형이다.
       - 연속적인 메모리 배치를 가진다!
    2. 원소의 갯수를 바꿀 수 없다.

## 임포트 (Import)

- ```python
  import numpy as np
  ```
  - 관례적으로 numpy는 `np`로 임포트 해준다.

## 배열생성

- 1차원
  - ````python
    oneDimArray = np.array([1,2,3])
        ```
    ````
- 2차원
  - ````python
    twoDimArray = np.array([1,2,3],[4,5,6])
        ```
    ````
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

  - `결과값 : [3,5,7]`
    - [2,4,6] + [1,2,3]

## 배열 크기구하기

- np.ndim

  - ```python
      print(oneDimArray.ndim) # 1 출력 ( 1차원이란 뜻 )
      print(twoDimArray.ndim) # 2 출력 ( 2차원이란 뜻 )
      print(threeDimArray.ndim) #3 출력 ( 3차원이란 뜻 )
    ```

- np.shape
  - ```python
      print(oneDimArray.shape) # (3,) 출력 (3크기 배열)  (행)
      print(twoDimArray.shape) # (2,3) 출력 ( 2x3크기 배열) (열,행)
      print(threeDimArray.shape) # (2,2,3) 출력 ( 2x2x3크기 배열) (깊이,열,행)
    ```

## 인덱싱

- ```python
  twoDimArray = np.array([1,2,3],[4,5,6])
  print(twoDimArray[0,0]) # 1 출력 [행,열]
  print(twoDimArray[0,1]) # 2 출력
  print(twoDimArray[0,-1]) # 3 출력
  ```

## 슬라이싱

- ```python
  twoDimArray = np.array([1,2,3],[4,5,6])
  # [1,2,3] 출력 [행,열] 1번째 행 모두 출력
  print(twoDimArray[0,:])
  # [1,4] 출력 1번째 열 모두 출력
  print(twoDimArray[:,0])
  # [2,3] 출력 1번째 행 2번째 열부터 끝까지 출력
  print(twoDimArray[0,1:])
  ```
  - [시작 : 끝 : 간격]
    - 시작 기본값 : 0
    - 끝 기본값 : -1 (마지막)
    - 간격 기본값 : 1 (순방향) , -1 : (역순)
      - -2 : 역순으로 2칸씩이동
