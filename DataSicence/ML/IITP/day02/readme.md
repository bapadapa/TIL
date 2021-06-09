# numpy~!

- numpy?

  - Numerical Python의 줄임 말
  - 고성능 수치 연산을 하기 위해 생성됨.

- ndArray?
  - N차원 배열 객체다
  - 같은 종류의 데이터만 담을 수 있다.
    - 모두 `int 형`이다가, `1개`라도 float이면, dtpye이 float으로 생성된다.
    - `간단생성`
    ```python
    import numpy as np
    data = [1,2,3,4,5]
    arr = np.array(data)
    ```
