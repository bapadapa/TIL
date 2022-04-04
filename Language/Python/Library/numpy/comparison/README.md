# 비교연산자들

- 단순하다 지금까지 배웠던 연산자들을 이용하여 사용한다

- 만약 비교연산자를 배열 안에 넣으면 `broadcast`되어 모든 값에 비교가 들어간다.

  | Operator | Equivalent             | ufunc Operator | ufunc Equivalent   |
  | -------- | ---------------------- | -------------- | ------------------ |
  | `==`     | `np.equal`             | `!=`           | `np.not_equal`     |
  | `<`      | `npnp.sum(x < 6).less` | `<=`           | `np.less_equal`    |
  | `>`      | `np.greater`           | `>=`           | `np.greater_equal` |
  | `&`      | `np.bitwise_and`       | `\|`           | `np.bitwise_or`    |
  | `^`      | `np.bitwise_xor`       | `~`            | `np.bitwise_not`   |

- 간단 예시
  - 코드
    - ```python
      import numpy as np
      x = np.array([1, 2, 3, 4, 5])
      np.sum(x < 6)
      ```
  - 결과
    - `8`

## 구조화된 데이터 Structured Data

#### Dtype

| Character    | Description            | Example                            |
| ------------ | ---------------------- | ---------------------------------- |
| `'b'`        | Byte                   | `np.dtype('b')`                    |
| `'i'`        | Signed integer         | `np.dtype('i4') == np.int32`       |
| `'u'`        | Unsigned integer       | `np.dtype('u1') == np.uint8`       |
| `'f'`        | Floating point         | `np.dtype('f8') == np.int64`       |
| `'c'`        | Complex floating point | `np.dtype('c16') == np.complex128` |
| `'S'`, `'a'` | String                 | `np.dtype('S5')`                   |
| `'U'`        | Unicode string         | `np.dtype('U') == np.str_`         |
| `'V'`        | Raw data (void)        | `np.dtype('V') == np.void`         |

- 위 데이터타입을 이용하여 배열 형변환을 시켜줄 수 있다.
