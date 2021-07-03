"""
크롤링 -> 형태소 분석 -> 빈도수등 분석 -> 워드클라우드
# 파이썬 : 3.8.8
# JAVAC : 16.0.1
# 설치 확인 방법
- 패키지.__version__
    - 위 코드를 실행시키면 버전이 나오면 잘 설치된것!
1. 크롤링
    1. BS4
    2. Selenum
2. 형태소 분석
    1. Konlpy 
        - jpype : 1.1.2
3. 빈도수 분석
    1 빈도수
        - frequency,wordcount....
    2. IF-IDF
        - sklearn
    3. LDA
        - gensim
    4. TESTREANK
        - gensim


"""

# %%
## 크롤링
from os import replace
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import datetime as dt
import pandas as pd
import time

driver = webdriver.Chrome()
startDate = dt.date(year = 2021, month=1,day = 1)
untilDate = dt.date(year = 2021, month=1,day = 2)
endDate = dt.date(year = 2021, month=1,day = 2)
count = 0
# 크롤링할 단어
query = '코로나'
totaltweets = []
# while endDate > startDate and count < 10:
while not endDate == startDate:
    # 인기글
    # url='https://twitter.com/search?q='+query+'%20since%3A'+str(startDate)+'%20until%3A'+str(untilDate)+'&amp;amp;amp;amp;amp;amp;lang=eg'
    # 최신글
    url='https://twitter.com/search?q='+query+'%20since%3A'+str(startDate)+'%20until%3A'+str(untilDate)+'&f=live'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    
    lastHeight = driver.execute_script("return document.body.scrollHeight")

    # time.sleep(2)
    while True:
        # dailyfreq = {'Date': startDate}

        wordfreq = 0 
        # tweets=soup.find_all("div", {"class": "css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"})
        tweets = str(soup.find_all("div", {"class": "css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}))
        tweets = re.sub('<.+?>', '', tweets, 0).strip()
        tweets = re.sub('\n', '', tweets, 0).strip()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        time.sleep(1)

        newHeight = driver.execute_script("return document.body.scrollHeight")

        if newHeight != lastHeight:
            html = driver.page_source
            soup = BeautifulSoup(html,'html.parser')
            tweets = str(soup.find_all("div", {"class": "css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}))
            tweets = re.sub('<.+?>', '', tweets, 0).strip()
            tweets = re.sub('\n', '', tweets, 0).strip()
            # wordfreq =len(tweets)
            totaltweets.append(tweets)
            
            
        else:
            # dailyfreq['Frequency'] = wordfreq
            # wordfreq = 0
            startDate = untilDate
            untilDate+= dt.timedelta(days=1)
            # dailyfreq={}
            
            break
        # pprint(tweets)        
        lastHeight = newHeight
        count = count +1
        if count == 10:
            startDate += dt.timedelta(days=2)
            break
driver.close()
# df = pd.DataFrame(columns=['id','message'])
# number = 1
# for i in range(len(totaltweets)):
#     for j in range(len(totaltweets[i])):
#         df = df.append({'id':number,'message':(totaltweets[i][j]).text},ignore_index=True)
#         nubmer = number +1
# df.to_csv('./aa.csv',index=False)
#%%
import pandas as pd
df = pd.read_csv('./aa.csv')
#%%
# df
df = pd.DataFrame(totaltweets , columns=['message']).reset_index().rename(columns={"index" : 'number'})
df.number = df.number.apply(lambda x : x+1)
df.to_csv('./aa.csv',index=False)

# %%
## 형태소 분석
from konlpy.tag import Kkma, Okt
from konlpy.utils import pprint
okt = Okt()
kkma = Kkma()
result = []
for i in df['message']:
    # 어절 추출
    result = result +okt.phrases(i)
    # result = result +kkma.nouns(i)

# %%
## 빈도수 분석
from collections import Counter

count = Counter(result)
# count = count.most_common(100)
count
#%%
#TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
tfidfv = TfidfVectorizer().fit(result)
print(tfidfv.transform(result).toarray())
# print(tfidfv.vocabulary_)

# %%
## 워드 클라우드

from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Cough = Image.open('Cough.png')
Cough = Image.open('aa2.png')
Cough = np.array(Cough)

NGwords = ['19', '1년', '1월','코로나']
stopwords = set(STOPWORDS)
for NGword in NGwords:
    stopwords.add(NGword)

wordcloud = WordCloud(
            font_path='C:/Windows/Fonts/HMKMRHD.ttf',
            background_color= 'white',
            stopwords= stopwords,
            max_font_size=100,
            mask=Cough
            )
            
wordcloud.generate_from_frequencies(dict(count))
# wordcloud.generate(text)
# wordcloud.recolor(color_func=ImageColorGenerator(Cough))

plt.figure(figsize=(22,22)) #이미지 사이즈 지정
plt.imshow(wordcloud, interpolation='lanczos') #이미지의 부드럽기 정도
plt.axis('off') #x y 축 숫자 제거
plt.show()



# %%
NGwords = ['19', '1년', '1월','코로나']
stopwords = set(STOPWORDS)
for NGword in NGwords:
    stopwords.add(NGword)
stopwords
# %%
from pathos.multiprocessing import ProcessingPool as Pool #pip install pathos 

# class Parser(): 
#     def __init__(self): 
#         self.pool = Pool(processes=3) 
#         """웹드라이버가 여기에 있으면 오류가 난다! 웹드라이버는 싱글스레드라서!""" 
#         # self.driver = webdriver.Chrome('./chromedriver.exe') 
#     def open_browser(self, site): 
#         """ process별로 브라우저를 따로 열어주면 오류가 안 난다 """ 
#         driver = webdriver.Chrome('./chromedriver.exe') 
#         driver.get(site) 
#     def multi_processing(self): 
#         sites = ['https://www.naver.com', 'https://www.daum.net', 'https://www.tistory.com'] 
#         Pool.map(open_browser, sites) 
# parser = Parser() 
# parser.multi_processing()
Pool
#%%
# %%
import threading
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import datetime as dt
import pandas as pd
import time


def crawling(startDate,untilDate,endDate) :
    driver = webdriver.Chrome()
    count = 0
    # 크롤링할 단어
    query = '코로나'
    totaltweets = []
    while not endDate == startDate and count < 50:
        # 인기글
        # url='https://twitter.com/search?q='+query+'%20since%3A'+str(startDate)+'%20until%3A'+str(untilDate)+'&amp;amp;amp;amp;amp;amp;lang=eg'
        # 최신글
        url = 'https://twitter.com/search?q='+query+'%20since%3A'+str(startDate)+'%20until%3A'+str(untilDate)+'&f=live'
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')

        lastHeight = driver.execute_script("return document.body.scrollHeight")

        # time.sleep(2)
        while True:
            print(startDate)
            tweets = str(soup.find_all("div", {"class": "css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}))
            tweets = re.sub('<.+?>', '', tweets, 0).strip()
            tweets = re.sub('\n', '', tweets, 0).strip()

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            time.sleep(1)

            newHeight = driver.execute_script("return document.body.scrollHeight")

            if newHeight != lastHeight:
                html = driver.page_source
                soup = BeautifulSoup(html,'html.parser')
                tweets = str(soup.find_all("div", {"class": "css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}))
                tweets = re.sub('<.+?>', '', tweets, 0).strip()
                tweets = re.sub('\n', '', tweets, 0).strip()
                # wordfreq =len(tweets)
                totaltweets.append(tweets)


            else:
                startDate = untilDate
                untilDate+= dt.timedelta(days=4)
                break

            lastHeight = newHeight
            count = count +1
            if count == 50:
                break
    driver.close()
    
if __name__ == '__main__':
    startDate = dt.date(year = 2021, month=1,day = 1)
    untilDate = dt.date(year = 2021, month=1,day = 2)
    endDate = dt.date(year = 2021, month=1,day = 10)
    for i in range(0,4):
        startDate += dt.timedelta(days=i)
        untilDate += dt.timedelta(days=i)
        my_thread = threading.Thread(target=crawling,args=(startDate,untilDate,endDate))
        my_thread.start()
#%%
len(totaltweets)

#%%
class crawling(threading.Thread):
    startDate =dt.date(year = 1, month=1,day = 1)
    untilDate =dt.date(year = 1, month=1,day = 1)
    endDate = dt.date(year = 1, month=1,day = 1)
    driver = webdriver.Chrome()
    count = 0
    

    def __init__(self,startDate,untilDate,endDate):
        threading.Thread.__init__(self) 
        self.startDate = startDate
        self.untilDate = untilDate
        self.endDate = endDate

    
    def run(self) :
        print(self.startDate,self.untilDate,self.endDate)
                
        # 크롤링할 단어
        query = '코로나'
        totaltweets = []
        while not endDate == startDate and count < 1000:
            # 인기글
            # url='https://twitter.com/search?q='+query+'%20since%3A'+str(startDate)+'%20until%3A'+str(untilDate)+'&amp;amp;amp;amp;amp;amp;lang=eg'
            # 최신글
            url = 'https://twitter.com/search?q='+query+'%20since%3A'+str(startDate)+'%20until%3A'+str(untilDate)+'&f=live'
            driver.get(url)
            html = driver.page_source
            soup = BeautifulSoup(html,'html.parser')

            lastHeight = driver.execute_script("return document.body.scrollHeight")

            # time.sleep(2)
            while True:
                tweets = str(soup.find_all("div", {"class": "css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}))
                tweets = re.sub('<.+?>', '', tweets, 0).strip()
                tweets = re.sub('\n', '', tweets, 0).strip()

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                time.sleep(1)

                newHeight = driver.execute_script("return document.body.scrollHeight")

                if newHeight != lastHeight:
                    html = driver.page_source
                    soup = BeautifulSoup(html,'html.parser')
                    tweets = str(soup.find_all("div", {"class": "css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}))
                    tweets = re.sub('<.+?>', '', tweets, 0).strip()
                    tweets = re.sub('\n', '', tweets, 0).strip()
                    # wordfreq =len(tweets)
                    totaltweets.append(tweets)


                else:
                    startDate = untilDate
                    untilDate+= dt.timedelta(days=4)
                    break

                lastHeight = newHeight
                count = count +1
                if count == 1000:
                    break


if __name__ == '__main__':
    startDate = dt.date(year = 2021, month=1,day = 1)
    untilDate = dt.date(year = 2021, month=1,day = 2)
    endDate = dt.date(year = 2021, month=1,day = 10)
    for i in range(0,4):
        startDate += dt.timedelta(days=i)
        untilDate += dt.timedelta(days=i)
        my_thread = crawling(startDate,untilDate,endDate)
        my_thread.start()
