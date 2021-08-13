# 로지스틱 회귀 ( Logistic_Regression )

## 수식

- $$H(X) = \frac{1}  {1 + e^-W^TX}$$
- $$cost(W) = -\frac{1}{m}\sum_{}y\log(H(x)) + (1-y)(\log(1-H(x)))$$
- $$w := W - \alpha\frac{\partial}{\partial}cost(W)$$
