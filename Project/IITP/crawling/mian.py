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
from typing import Tuple
from numpy.core.fromnumeric import shape
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

#############################################################################
#
# 1. 트위치 크롤링
# 2. 크롤링한 데이터 cvs로 저장
# 3. 크롤링한 데이터 정제후 csv로 저장
# 4. 저장된 데이터 Load 후 Counter 변수로 변경
# 5. 시각화
#       -  Wordcloud
#############################################################################

import threading
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
import datetime as dt
import pandas as pd
import numpy as np
import time

# 크롤링 ( 1회전만함 , 함수 외부에서 for문을 돌리는중)
def crawling(query,startD,untilD,endDate,totaltweets,cnt) :
    driver = webdriver.Chrome()
    count = 0 

    if(endDate<startD):
        time.sleep(60)
        driver.close()        
        return
    # 인기글
    # url='https://twitter.com/search?q='+query+'%20since%3A'+str(startDate)+'%20until%3A'+str(untilDate)+'&amp;amp;amp;amp;amp;amp;lang=eg'
    # 최신글
    url = 'https://twitter.com/search?q='+query+'%20since%3A'+str(startD)+'%20until%3A'+str(untilD)+'&f=live'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')        
    lastHeight = driver.execute_script("return document.body.scrollHeight")

    count = 0 
    time.sleep(1)
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        tweets = str(soup.find_all("div", {"class": "css-901oao r-1fmj7o5 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"}))
        # 테그 제거
        tweets = re.sub('<[^>]*>', '', tweets, 0).strip()
        # \n|\r 제거
        tweets = re.sub('[\n|\r]', '', tweets, 0).strip()
        if newHeight != lastHeight:
            html = driver.page_source
            soup = BeautifulSoup(html,'html.parser') 
            totaltweets.append(tweets)
        else:
            break
        lastHeight = newHeight
        count += 1
        if count  >= 100:
            break
    driver.close()
    return totaltweets

# 스레드를 이용한 셀레니움 크롤링
def crawlStart (query,threads,_year,_month,_day):
    startDate = dt.date(year = _year, month=_month,day = 1)
    untilDate = dt.date(year = _year, month=_month,day = 2)
    endDate = dt.date(year = _year, month=_month,day = _day)

    totaltweets = []   
    repetitions = (endDate-startDate).days//threads
    for i in range(repetitions+1):
        for j in range(i*threads,i*threads+threads):
            startD = startDate+ dt.timedelta(days=j)
            untilD = untilDate+ dt.timedelta(days=j)
            my_thread = threading.Thread(target=crawling,args=(query,startD,untilD,endDate,totaltweets,threads))
            my_thread.start()
        my_thread.join()
    return totaltweets

# 혹시 모르니 정제 이전의 데이터도 저 장
def saveRaw(tweets_data,_year,_month):
    crawled_data = pd.DataFrame(tweets_data, columns=['message']).drop_duplicates(['message'],keep='last')
    crawled_data = crawled_data.reset_index().rename(columns={"index" : 'number'})
    crawled_data.number = crawled_data.number.apply(lambda x : x+1)
    # crawled_data.to_csv('../Data/scrapedData/'+str(_year)+'_'+str(_month)+'_covid_twitter.csv',index=False)
    crawled_data.to_csv('../Data/scrapedData/'+str(_year)+'_'+str(_month)+'_hos_twitter.csv',index=False)

# 스크랩핑한 데이터의 단어들 정제 후 저장
def crawlClean(tweets_data,_year,_month):
    crawled_data = pd.DataFrame(tweets_data, columns=['message']).drop_duplicates(['message'],keep='last')
    crawled_data = cleanStr(crawled_data)
    # 인덱스 부여하기 (그런데 필요없을듯.. )
    crawled_data = crawled_data.reset_index().rename(columns={"index" : 'number'})
    crawled_data.number = crawled_data.number.apply(lambda x : x+1)
    # crawled_data.to_csv('../Data/scrapedData/'+str(_year)+'_'+str(_month)+'_covid_twitter_removed.csv',index=False)
    crawled_data.to_csv('../Data/scrapedData/'+str(_year)+'_'+str(_month)+'_hos_twitter_removed.csv',index=False)

# 스크랩핑한 데이터의 단어들 정제
def cleanStr (crawled_df):    
    # URL 삭제
    crawled_df['message'] = crawled_df['message'].str.replace(r'[(bit|youtube|m|coupa|bitsonic|n|naver|news|yna)].(?:[-\w.\0-9\.]|(?:\da-fA-F{2}))+',repl = r'', regex=True)  
    crawled_df['message'] = crawled_df['message'].str.replace(r'[(http|https|ftp)]://(?:[-\w.\0-9\.]|(?:\da-fA-F{2}))+',repl = r'', regex=True)  
    # 이메일 삭제
    crawled_df['message'] = crawled_df['message'].str.replace(r'\[a-zA-Z0-9\_.+-\]+@\[a-zA-Z0-9-\]+.\[a-zA-Z0-9-.\]+',repl = r'', regex=True)  
    # 한글 자음모음 삭제
    crawled_df['message'] = crawled_df['message'].str.replace(r'[ㄱ-ㅎㅏ-ㅣ]+',repl = r'', regex=True)  
    # 특수문자 및 2중 스페이스 삭제 
    crawled_df["message"] = crawled_df["message"].str.replace(pat=r'[^\w\s+]', repl=r'', regex=True)
    # crawled_df["message"] = crawled_df["message"].str.replace(pat=r'[^\w\s]', repl=r'', regex=True)    
    # 빈값 삭제
    crawled_df['message'].replace('',np.NaN,inplace=True)
    crawled_df.dropna(subset=['message'],inplace=True)
    return crawled_df

if __name__ == '__main__':
    months = [1,2,3,4,5,6]
    days  = [31,28,31,30,31,30]
    for i in range(6):
        query,threads,_year,_month,_day = '병원',5,2021,6,30
        tweets_data = crawlStart(query,threads,_year,months[i],days[i])
        saveRaw(tweets_data,_year,months[i])
        crawlClean(tweets_data,_year,months[i])
    # query,threads,_year,_month,_day = '병원',5,2021,6,30
    # tweets_data = crawlStart(query,threads,_year,_month,_day)
    # saveRaw(tweets_data,_year,_month)
    # crawlClean(tweets_data,_year,_month)
#%%
tweets_data
#%%
# 중복제거 및 빈값삭제 후 csv 저장
import numpy as np
crawled_data = pd.DataFrame(list(set(totaltweets)), columns=['message'])
crawled_data['message'].replace('[]',np.NaN,inplace=True)
crawled_data.dropna(subset=['message'],inplace=True)
crawled_data = crawled_data.reset_index().rename(columns={"index" : 'number'})
crawled_data.number = crawled_data.number.apply(lambda x : x+1)
crawled_data.to_csv('./2101_covid_twitter.csv',index=False)

#%%

#특수문자 삭제
# 중복 제거 후 message의 마지막 것만 살리겠다는 의미
crawled_data = pd.DataFrame(totaltweets, columns=['message']).drop_duplicates(['message'],keep='last')
# cleansing string
# 한글 및 공백만 남기기
def cleanStr (crawled_df):        
    crawled_df['message'] = [re.sub('[^가-힣\s]', '', s) for s in crawled_df['message']]
    crawled_df['message'].replace('',np.NaN,inplace=True)
    crawled_df.dropna(subset=['message'],inplace=True)
    return crawled_df

def cleanStrVer2 (crawled_df):    
    # URL 삭제
    crawled_df['message'] = crawled_df['message'].str.replace(r'[(http|https|ftp)]://(?:[-\w.\0-9\.]|(?:\da-fA-F{2}))+',repl = r'', regex=True)  
    # 이메일 삭제
    crawled_df['message'] = crawled_df['message'].str.replace(r'\[a-zA-Z0-9\_.+-\]+@\[a-zA-Z0-9-\]+.\[a-zA-Z0-9-.\]+',repl = r'', regex=True)  
    # 한글 자음모음 삭제
    crawled_df['message'] = crawled_df['message'].str.replace(r'[ㄱ-ㅎㅏ-ㅣ]+',repl = r'', regex=True)  
    # 특수문자 및 2중 스페이스 삭제 
    crawled_df["message"] = crawled_df["message"].str.replace(pat=r'[^\w\s]', repl=r'', regex=True)
    # crawled_df["message"] = crawled_df["message"].str.replace(pat=r'[^\w\s]', repl=r'', regex=True)    
    # 빈값 삭제
    crawled_df['message'].replace('',np.NaN,inplace=True)
    crawled_df.dropna(subset=['message'],inplace=True)
    return crawled_df
crawled_data = cleanStr(crawled_data)  

# 인덱스 부여하기 (그런데 필요없을듯.. )
crawled_data = crawled_data.reset_index().rename(columns={"index" : 'number'})
crawled_data.number = crawled_data.number.apply(lambda x : x+1)
crawled_data.to_csv('./2101_covid_twitter_removed.csv',index=False)
#%%
## 형태소 분석
def morpheme (crawled_data,crawledName):
    from konlpy.tag import Kkma, Okt
    from konlpy.utils import pprint
    from collections import Counter
    okt = Okt()
    result = []
    for i in crawled_data['message']:
        # 어절 추출
        print(df[df.message == i].index)
        result = result +okt.nouns(i)
    ## 빈도수 분석
    count = Counter(result)
    # count = count.most_common(500)
    pd.DataFrame(count,index=[0]).to_csv('./'+crawledName+'_twitter_count.csv.csv',index= False)
    return count

#%%
# 크롤링 데이터 병합
import pandas as pd
df = pd.DataFrame(pd.read_csv('../Data/scrapedData/2021_1_hos_twitter.csv'))
for i in range(2,7):
    df= pd.concat([df,pd.read_csv('../Data/scrapedData/2021_'+str(i)+'_hos_twitter.csv')])
df.to_csv('./hos_twitter_NonCleaned_morphemed.csv')

####################################################################################################

#%%
# 파일읽고, Counter변수로 전환

from collections import Counter
import pandas as pd
def readCount(FileName):
    tmp = pd.read_csv(FileName)
    tmp = pd.DataFrame(tmp.T)
    
    # 1글자 단어 삭제        
    return Counter(dict({key: value for key, value in tmp[0].to_dict().items() if len(key) != 1 }))

#%%
targetWords = readCount('hos_twitter_count_ver2.csv')
#%%
# 불용어 처리
stopwords = pd.read_csv('../Data/stopwords.csv')

for key in stopwords.stopwords:
    if key in targetWords:
        del targetWords[key] 
targetWords.most_common(20)
#%%
## 워드 클라우드

from wordcloud import WordCloud
from wordcloud import STOPWORDS
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Cough = Image.open('Cough.png')

mask = np.array(Image.open('./Cough.png'))

NGwords = ['네이버']
stopwords = set(STOPWORDS)
for NGword in NGwords:
    stopwords.add(NGword)

wordcloud = WordCloud(
            font_path='C:/Windows/Fonts/HMKMRHD.ttf',
            background_color= 'white',
            stopwords= stopwords,
            mask = mask,
            max_font_size=100,            
            )
            
wordcloud.generate_from_frequencies(dict(targetWords.most_common(1000)))
# wordcloud.generate(text)
wordcloud.recolor(color_func=ImageColorGenerator(mask))
import pandas as pd # 데이터프레임 사용을 위해
from math import log # IDF 계산을 위해
fig=plt.figure(figsize=(22,22)) #이미지 사이즈 지정
plt.imshow(wordcloud, interpolation='lanczos') #이미지의 부드럽기 정도
plt.axis('off') #x y 축 숫자 제거
plt.show()
fig.savefig('./hos_wordCloud.png')

#%%
targetWords.most_common(20)
#%%
# IF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
targetWords = pd.read_csv('../Data/scrapedData/2021_1_hos_twitter.csv').message
rfidfVector =  TfidfVectorizer().fit(targetWords)
print(rfidfVector.transform(targetWords).toarray())
print(rfidfVector.vocabulary_)

a = rfidfVector.vocabulary_
stopwords = pd.read_csv('../Data/stopwords.csv')

for key in stopwords.stopwords:
    if key in targetWords:
        del a [key] 
Counter(a).most_common(100)

#%%
from sklearn.feature_extraction.text import CountVectorizer
targetWords = pd.read_csv('../Data/scrapedData/2021_1_hos_twitter.csv').message
# total['TITLE2'] = [re.sub('[^A-Za-z0-9가-힣]', '', s) for s in total['제목']]

vector = CountVectorizer()
print(vector.fit_transform(targetWords).toarray()) # 코퍼스로부터 각 단어의 빈도 수를 기록한다.
print(vector.vocabulary_) 
Counter(vector.vocabulary_).most_common(100)

#%%
import re
targetWords = pd.read_csv('../Data/scrapedData/2021_1_hos_twitter.csv').message
# re.sub('[^가-힣]','',targetWords)
targetWords = pd.DataFrame(targetWords)
targetWords['message'] = [re.sub('[^가-힣\s]', '', s) for s in targetWords['message']]
targetWords['message'].replace('',np.NaN,inplace=True)
targetWords.dropna(subset=['message'],inplace=True)
targetWords





# %%
# 다시 형태소 분석########
from konlpy.tag import Kkma, Okt
from konlpy.utils import pprint
from collections import Counter
okt = Okt()
result = []
targetWords = cleanStr(pd.read_csv('./hos_twitter_NonCleaned_morphemed.csv'))

for i in targetWords['message']:
    # 어절 추출
    print(targetWords[targetWords.message == i].index)
    result = result +okt.nouns(i)
## 빈도수 분석
count = Counter(result)
# count = count.most_common(500)
pd.DataFrame(count,index=[0]).to_csv('./hos_twitter_count_ver2.csv',index= False)

####################  잠시 함수만들기 귀찮아서 이렇게 해봄 ########

targetWords = cleanStr(pd.read_csv('./covid_twitter_NonCleaned_morphemed.csv'))

result = []
for i in targetWords['message']:
    # 어절 추출
    print(targetWords[targetWords.message == i].index)
    result = result +okt.nouns(i)
## 빈도수 분석
count = Counter(result)
# count = count.most_common(500)
pd.DataFrame(count,index=[0]).to_csv('./covid_twitter_count_ver2.csv',index= False)
