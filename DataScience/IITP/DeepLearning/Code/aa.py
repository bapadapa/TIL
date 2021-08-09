#%%
import numpy as np
import matplotlib.pyplot as plt
#%%
# 간단 선형회기
X = np.random.randn(100)
W = np.random.randn(1)
b = np.random.randn(1)
y = X*W

plt.scatter(X,y)
#%%
# 신경망 회기
