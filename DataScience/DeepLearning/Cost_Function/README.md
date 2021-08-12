# 손실함수 (Cont / Loss Function)

## cross entropy

### 수식

<script id="MathJax-script" async src="<url-to-your-site>/mathjax/tex-chtml.js"></script>

$$-\frac{1}{n} \sum_{i=1}^{n} \sum_{c=1}^{C} L_{ic}log(P_{ic})$$

- n = 데이터 갯수
- C = 범주 갯수
- L = 실제 값 (주로 0 또는 1)
- P = 실제 값에 대한 확률 값 (0~1)
