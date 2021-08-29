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
# %%
#ML을 이용한 감정분석   
import re
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.layers import Embedding, Dense, LSTM
from keras.models import Sequential
from keras import optimizers,losses
import tensorflow as tf
import json
from bs4 import BeautifulSoup
# %%

# 데이터 가져오기
dt=  pd.read_csv('./data/Reviews.csv',nrows=30000)
data = dt[['Text','Score']]
# Y = dt['Score']

# 중복제거
data.drop_duplicates(subset='Text',inplace= True)
# na제 거
data.replace('',np.nan, inplace= True)
data.dropna(how='any')
# Text 정제
#축약 사전
with open('./data/shortCut.json') as fp:
    contraction_mapping = json.load(fp)
stop_words = set(stopwords.words('english'))
def text_cleaner(text,num = 0):
    newString = text.lower()
    newString = BeautifulSoup(newString, "lxml").text
    newString = re.sub(r'\([^)]*\)', '', newString)
    newString = re.sub('"','', newString)
    newString = ' '.join([contraction_mapping[t] if t in contraction_mapping else t for t in newString.split(" ")])    
    newString = re.sub(r"'s\b","",newString)
    newString = re.sub("[^a-zA-Z]", " ", newString) 
    newString = re.sub('[m]{2,}', 'mm', newString)
    if(num==0):
        tokens = [w for w in newString.split() if not w in stop_words]
    else:
        tokens=newString.split()
    long_words=[]
    for i in tokens:
        if len(i)>1:                                                 #removing short word
            long_words.append(i)   
    return (" ".join(long_words)).strip()

#call the function`
cleaned_text = []
for t in data['Text']:
    cleaned_text.append(text_cleaner(t))
data['Text'] = cleaned_text
# %%
# 토큰화 및 불용어 제거
#punkt,averaged_perceptron_tagger이 없다면 다운로드할것
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
#%%
x = []
for sentence in data['Text']:    
    x.append([word[0] for word in nltk.pos_tag(nltk.word_tokenize(sentence))])
x
#%%
# Tokenizing 해주기
tokenizer = Tokenizer()
# 문자 데이터 -> 리스트 형태로 변경
tokenizer.fit_on_texts(x)
# tokenizer을 key : value, 즉 dict로 만들어줌
print(tokenizer.word_index)
#%%
# 빈도수가 너무 적은 단어는 제거해주기
threshold = 3
words_cnt = len(tokenizer.word_index)
rare_cnt = 0
words_freq = 0
rare_freq = 0

for key, value in tokenizer.word_counts.items():
    words_freq += value
    # 길이가 작으면 rare하다
    if value < threshold:
        rare_cnt +=1
        rare_freq += value
print('전체 단어수 : ', words_cnt)    
print(f"빈도수가 {threshold-1} 이 하인 희귀 단어 수 {rare_cnt}")
print(f'희귀 단어 비율 : {(rare_cnt/words_cnt) * 100}')
print(f"희귀 단어 등장 빈도 비율 : {(rare_freq/words_freq) * 100}")
#%%
vocab_size = words_cnt - rare_cnt +2
print(vocab_size)
#%%
# oov == out of vocabulary
tokenizer = Tokenizer(vocab_size , oov_token = 'OOV')
tokenizer.fit_on_texts(x)
# sentence를 index값 즉 시퀀스로 만들어줌
x = tokenizer.texts_to_sequences(x)
y =np.array(data['Score'])

#%%
# 전처리하면서 길이가 0이된 문장 삭제
drop_ = [idx for idx, sentence in enumerate(x) if len(sentence) < 1]
x = np.delete(x , drop_ ,axis=0)
y = np.delete(y , drop_ ,axis=0)
#%%
#padding 길이를 맞추고, 입력을 동일한 길이로 맞춰줌
print('최대 길이 :  ', max(len(x) for l in x))
print('평균 길이 :  ', sum(map(len, x))/len(x))
#%%
# 플롯팅하여 최대길이 지정해주기
plt.hist([len(s) for s in  x],bins = 50)
plt.xlabel('length')
plt.ylabel('number')
plt.show()
#%%
max_len = 100
x= pad_sequences(x,maxlen=max_len)
#%%

X_train, X_test, Y_train,Y_test = train_test_split(x,y,test_size=.2)
# %%

#%%


# 훈련모델

# %%
model = Sequential([
    Embedding(vocab_size, 256),
    LSTM(512,kernel_initializer='he_uniform',return_sequences=True,dropout=0.4,recurrent_dropout=0.4),
    LSTM(512,kernel_initializer='he_uniform'),
    Dense(256, activation='relu',kernel_initializer='he_uniform'),
    Dense(1, activation='softmax')
])
model.summary()
model.compile(
    optimizer= optimizers.RMSprop(learning_rate=1e-3),
    loss = losses.CategoricalCrossentropy(),
    metrics = ['acc']
)
#%%
with tf.device('/device:GPU:0'):
    history = model.fit(
        x = X_train,
        y = Y_train,
        epochs= 15,
        batch_size= 512,
        validation_split= .2
    )

#%%
#훈련결과 확인
hist_dict = history.history
loss = hist_dict['loss']
val_loss = hist_dict['val_loss']
acc = hist_dict['acc']
val_acc = hist_dict['val_acc']

plt.plot(loss, 'b--', label = 'train loss')
plt.plot(val_loss, 'r:' , label = 'val loss')
plt.legend()
plt.grid()

plt.figure()
plt.plot(acc, 'b--', label = 'train acc')
plt.plot(val_acc, 'r:' , label = 'val acc')
plt.legend()
plt.grid()

plt.show()

# %%
