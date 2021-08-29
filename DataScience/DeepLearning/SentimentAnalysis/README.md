# Sentiment Analysis(감정(문맥)분석)

## 정의

1. 텍스트에 등장하는 단어를 통해 감정을 분석하는 기법
1. Opinion Mining이라고도 불림
1. 분석시 미리 정의된 `어휘 사전`이 필요
   1. 어휘 사전의 단어 분포에 따라 텍스트 감정이 좌우된다.
1. 토픽 모델링이 텍스트의 주체를 찾으면, 감정 분석은 Text의 의견을 찾음
1. Text = Topic + Opinion

   - Topic -> Topic Modeling
   - Opinion -> Opinion Mining

1. 감정분석 -> SNS에서 유용함
1. 구분
   1. 어휘사전을 이용한 분류
      1. 분류한 사전을 통해 Text분류 후 감정가 계산
         - 감정에 해당되는 단어를 미리 정의해야 함
   1. ML을 이용한 감정 분류
      1. Text의 빌부를 훈련데이터로 사용해 Text 감정 상태 분류
         - Text <-> Label 맵핑이 되어 있어야함

## 어휘 사전을 통한 분류

### Processe

1. 감정 사전 준비.

   - pip install afinn

1. 데이터 준비

   - ```python
       from sklearn.datasets import fetch_20newsgroup
       newsdata = fetch_20newsgroups

     ```

1. 감정 상태 분류 및 시각화

   - ```python
       from afinn import Afinn
       afinn = Afinn()
       for i in range(10):
           print(afinn.score(newsdata.data[i]))
     ```

   - ```python
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

     ```

## 기계학습을 이용한 감정 분석

1. 과정

   1. 필요 libiray 가져오기

      - ```py
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
        ```

   1. 데이터 수집
      - 본인이 분석하고자 하는 데이터를 가져온다.
      - 이 때 text와 target 즉, `x,y`로 나뉘어진 데이터가 필요하다
   1. 데이터 정제

      1. 불필요한 Text 제거

         1. na값 제거
         1. 중복 제거
         1. 불용어 제거

         - 위와 같이 훈련에 방해되는 Text가 들어가 있을 경우가 많다. 모두 제거해준다.

         - ```python
            #축약 사전
            with open('./data/shortCut.json') as fp:
                contraction_mapping = json.load(fp)
            # 중복제거
            data.drop_duplicates(subset='Text',inplace= True)
            # na제 거
            data.replace('',np.nan, inplace= True)
            data.dropna(how='any')

            # Text 정제
            stop_words = set(stopwords.words('english'))
            def text_cleaner(text,num = 0):
                newString = text.lower()
                newString = BeautifulSoup(newString, "lxml").text
                newString = re.sub(r'\([^)]*\)', '', newString)
                newString = re.sub('"','', newString)
                newString = ' '.join([contraction_mapping[t] if t in contraction_mapping else t             for t in newString.split(" ")])
                newString = re.sub(r"'s\b","",newString)
                newString = re.sub("[^a-zA-Z]", " ", newString)
                newString = re.sub('[m]{2,}', 'mm', newString)
                if(num==0):
                    tokens = [w for w in newString.split() if not w in stop_words]
                else:
                    tokens=newString.split()
                long_words=[]
                for i in tokens:
                    if len(i)>1:                                                 #removing short            word
                        long_words.append(i)
                return (" ".join(long_words)).strip()

            #call the function`
            cleaned_text = []
            for t in data['Text']:
                cleaned_text.append(text_cleaner(t))
           ```

           - 영어를 기반으로 감정분석을 진행하여 축약사전을 가져와 풀어주었다.
             - `aren't` -> `are not`
           - 불용어 처리를 위해 nltk의 `stopwords`을 이용하였다.

      1. 데이터 토큰화

         - ```python
            # Tokenizing 해주기
            tokenizer = Tokenizer()
            # 문자 데이터 -> 리스트 형태로 변경
            tokenizer.fit_on_texts(x)
            # tokenizer을 key : value, 즉 dict로 만들어줌
            print(tokenizer.word_index)
           ```

      1. 데이터 출현 빈도가 너무 적으면 제거

         - ```python
            # 빈도수가 너무 적은 단어는 제거해주기
            threshold = 3
            words_cnt = len(tokenizer.word_index)
            rare_cnt = 0
            words_freq = 0
            rare_freq = 0
            # word_count를 이용하여 각 단어별 출현 빈도 추출
            for key, value in tokenizer.word_counts.items():
                words_freq += value
                # 길이가 작으면 rare하다
                if value < threshold:
                    rare_cnt +=1
                    rare_freq += value

            vocab_size = words_cnt - rare_cnt +2

            #%%
            # oov == out of vocabulary
            #     oov_token = 'OOV' -> 새로 만나게된 단어를 무시하지 않고, 특수값으로 처리함.
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
           ```

      1. 데이터 Padding추가

         - ```python
            max_len = 100
            x= pad_sequences(x,maxlen=max_len)
           ```

           - 전처리 하면서 나온 값을 이용하여 `plot`을 띄워 적절한 길이로 Padding을 체워줌
             - Padding 하는이유 : `모든 Text`의 `길이를 동일`하게 만들어주기 위해 사용한다.

   1. 모델 생성 및 훈련

      1. Train, Test 나누기

         - ```python
            X_train, X_test, Y_train,Y_test = train_test_split(x,y,test_size=.2)
           ```

           - sklearn에 있는 train_test_split을 사용함

      1. 모델 생성

         - ```python
            model = Sequential([
               Embedding(vocab_size, 256),
               LSTM(512,kernel_initializer='he_uniform',return_sequences=True,dropout=0.4,recurrent_dropout=0.4),
               LSTM(512,kernel_initializer='he_uniform'),
               Dense(256, activation='relu',kernel_initializer='he_uniform'),
               Dense(1, activation='softmax')
           ])
           ```

           - 간단하게 [LSTM모델](./LSTM)만 이용하여 생성

      1. 모델 Compile

         - ```py
            model.compile(
               optimizer= optimizers.RMSprop(learning_rate=1e-3),
               loss = losses.CategoricalCrossentropy(),
               metrics = ['acc']
           )

           ```

           - 원하는 조합을 이용하여 생성할 수 있음
           - loss는 여러개를 분류하는 것 이기 때문에 `CategoricalCrossentropy`를 사용함

      1. 훈련

         - ```py
           with tf.device('/device:GPU:0'):
              history = model.fit(
                  x = X_train,
                  y = Y_train,
                  epochs= 15,
                  batch_size= 512,
                  validation_split= .2
              )
           ```

           - fit을 이용하여 훈련시켜 준다.

      1. 결과 확인

         - ```py
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
           ```

           - `Tensor Board`를 이용하여 훈련 결과를 확인할 수 있지만, 간편하게 `pyplot`를 이용하여 확인할 수 도 있다.
             - 확인할 것 : train / val loss, train / val accuracy
