# %%
from typing import Text
from nltk import tokenize
from sklearn.datasets import fetch_20newsgroups
# newsdata = fetch_20newsgroups
newsdata = fetch_20newsgroups(subset='train')
newsdata.data[0]
# %%
# 단어사전으로 감정가 부여
from afinn import Afinn
afinn = Afinn()
for i in range(10):
    print(afinn.score(newsdata.data[i]))
# %%
# 시각화 ( 빈도수 )
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

positive = 0
neutral = 0
negetive = 0

for i in newsdata.data:
    score = afinn.score(i)
    if score > 0:
        positive+=1
    elif score == 0:
        neutral +=1
    else :
        negetive +=1
    
plt.bar(np.arange(3),[positive,neutral,negetive])
plt.xticks(np.arange(3),['positive','neutral','negetive'])
plt.show()