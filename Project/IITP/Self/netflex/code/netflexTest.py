"""
파일출처 : Kaggle

파일 내용
show_id: unique id of each show (not much of a use for us in this notebook)

type: The category of a show, can be either a Movie or a TV Show

title: Name of the show

director: Name of the director(s) of the show

cast: Name of actors and other cast of the show

country: Name of countries the show is available to watch on Netflix

date_added: Date when the show was added on Netflix

release_year: Release year of the show

rating: Show rating on netflix
duration: Time duration of the show

listed_in: Genre of the show

description: Some text describing the show


"""

#%%
from numpy.core.fromnumeric import shape
from numpy.testing._private.utils import temppath
import pandas as pd
import numpy as np
import math 
import os
from pandas.io import json
from seaborn.relational import scatterplot
# sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.cluster import MiniBatchKMeans
# 시각화
import matplotlib.pyplot as plt
import networkx as nx


df = pd.read_csv("./NetflexData/netflix_titles.csv")
# df[df['country'] == 'South Korea']

# set(df['rating'])

corpus = df['description'][0]
tfidfv = TfidfVectorizer().fit(corpus)
print(tfidfv.transform(corpus).toarray())
print(tfidfv.vocabulary_)

#%%
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
corpus = [df['description'][0]]
vector = CountVectorizer()
print(vector.fit_transform(corpus).toarray()) # 코퍼스로부터 각 단어의 빈도 수를 기록한다.
print(vector.vocabulary_) # 각 단어의 인덱스가 어떻게 부여되었는지를 보여준다.

#%%
pd.read_csv('./NetflexData/raw/ratings.csv')
pd.read_csv('./NetflexData/raw/movies_metadata.csv')

#%%
pd.read_csv('./NetflexData/sampleData/ratings.csv')
pd.read_csv('./NetflexData/sampleData/movies.csv')

#%%
all = [var for var in globals() if var[0] != "_"]
for var in all:
    del globals()[var]
#%%
import pandas as pd
import numpy as np
from math import log
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer

df  = pd.read_csv('./NetflexData/raw/movies_metadata.csv')
# data = df.head(20000)
data = df
data = data[['original_title','overview']]
data['overview']=data['overview'].fillna('') # na값 제거
tfidf=TfidfVectorizer(stop_words='english')#불용어 제거 
tfidf_mat=tfidf.fit_transform(data['overview']).toarray()


# TF-IDF를 사용하여 추출한 단어를 기반으로 COS 유사도 측정
def cos_sim(X,Y):
    return np.dot(X,Y)/((norm(X)*norm(Y))+1e-7)

def top_match_ar2(data, name, rank=10,c_sim=cos_sim):
    similarity=[]
    for i in range(len(data)):
        if name != i:
            similarity.append((c_sim(data[i],data[name]),i))
    similarity.sort()
    similarity.reverse()
    return similarity[:rank]
# 유사한 영화 추출하기
movieList = [] 
for similarity, movie_id in top_match_ar2(tfidf_mat,data[data.original_title == 'Toy Story 3'].index[0],50):
    movieList.append(('Toy Story 3', data.loc[movie_id,'original_title'],similarity))
movieList[:10]

#%%
movieList
#%%
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import font_manager

font_path = "C:/Windows/Fonts/malgunbd.ttf" # 폰트 파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()

movieList = pd.DataFrame(movieList,columns=['from','to','weight'])
g = nx.from_pandas_edgelist(movieList,'from','to','weight',create_using=nx.DiGraph())
pos = nx.kamada_kawai_layout(g)
# edges,weights 리스트 만들기  
edges,weights = zip(*nx.get_edge_attributes(g,'weight').items())
# 간선의 너비 늘리기 ( corr를 이용해 구현해서 가중치 안 늘리면 너무 가늘게 나옴)
wMin = min(weights)
wMax = max(weights)
tmp = pd.DataFrame(weights)
weights = (tmp.apply(lambda x : (x-wMin)/(wMax-wMin))[0])

weights = tuple([(1+abs(x))**2/2 for x in weights])

plt.figure(figsize=(20,20))

# 노드 디자인
nx.draw_networkx_nodes(g,pos, node_size=200, alpha=0.9)
# 라벨 디자인
# nx.draw_networkx_labels(g, positions, font_size=10)

nx.draw_networkx(g,pos=pos,with_labels=True,font_family = font_name )
# labels = nx.get_edge_attributes(g,'weight')
# nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
nx.draw_networkx_edges(g, pos, edgelist=edges,style='solid',
                      width=weights, edge_color=weights ,edge_vmin = min(weights), edge_vmax=max(weights))
# plt.legend(g.nodes(),loc = 'upper right')
plt.title('Toy Story 3',fontdict={'family': font_name, 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 40})
plt.axis(False)
plt.show()
#%%
import ast
temp = pd.DataFrame(ast.literal_eval(df.genres[0]))
#%%
genres = temp.name
#%%

for i in df.genres:
    for genre in genres:
        if genre in i:
            True

#%%
import ast
tmp = df[['title','overview','genres']]
tmp = tmp[tmp.genres !='[]']
pd.DataFrame(ast.literal_eval(tmp.genres[0])).name[0]

#%%
# %%
###################################################################################################
import pandas as pd
import numpy as np
from math import log
import ast
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib import font_manager

# 유사한 영상을 TF-IDF 를 통해 찾기 전 같은 장르의 영화만 추출

def extract_genre(df,title):
    result = pd.DataFrame()
    idx = M_df[M_df.original_title == title].index
    for genre in pd.DataFrame(ast.literal_eval(df[df.original_title == title].genres[idx[0]])).name :
        result = result.append(df[df.genres.str.contains(genre)])
    return(result.drop_duplicates().reset_index(drop = True))

def film_tfdif(metadatas,filmName,extract_genre =extract_genre):
    films = extract_genre(metadatas,filmName)
    films = films[['original_title','overview']]
    films['overview']=films['overview'].fillna('') # na값 제거
    tfidf=TfidfVectorizer(stop_words='english')#불용어 제거 
    return films,tfidf.fit_transform(films['overview']).toarray() 

# TF-IDF를 사용하여 추출한 단어를 기반으로 COS 유사도 측정
def cos_sim(X,Y):
    # 만에하나라도  분모에 0이 들어갈 수 있음으로 1e-8을 더해줌
    return np.dot(X,Y)/((norm(X)*norm(Y))+1e-8)
def top_match(data, name, rank,c_sim=cos_sim):
    similarity=[]
    for i in range(len(data)):
        if name != i:
            similarity.append((c_sim(data[i],data[name]),i))
    similarity.sort()
    similarity.reverse()
    return similarity[:rank]

def extrasct_similar_Movie(data,tfidf_mat,title,rank = 10,match = top_match):
    movieList = [] 
    for similarity, movie_id in match(tfidf_mat,data[data.original_title == title].index[0],rank):
        movieList.append((title, data.loc[movie_id,'original_title'],similarity))
    return movieList

def newworkPlot(movieList,film_title):
    font_path = "C:/Windows/Fonts/malgunbd.ttf" # 폰트 파일 위치
    font_name = font_manager.FontProperties(fname=font_path).get_name()
        
    g = nx.from_pandas_edgelist(movieList,'from','to','weight',create_using=nx.Graph())
    pos = nx.kamada_kawai_layout(g)
    # edges,weights 리스트 만들기  
    edges,weights = zip(*nx.get_edge_attributes(g,'weight').items())
    # 간선의 너비 늘리기 ( corr를 이용해 구현해서 가중치 안 늘리면 너무 가늘게 나옴)
    wMin = min(weights)
    wMax = max(weights)
    tmp = pd.DataFrame(weights)
    weights = (tmp.apply(lambda x : (x-wMin)/(wMax-wMin))[0])

    weights = tuple([(1+abs(x))**2 for x in weights])

    plt.figure(figsize=(20,20))    

    # 노드 디자인
    nx.draw_networkx_nodes(g,pos, node_size=200, alpha=0.9)
    # 라벨 디자인
    nx.draw_networkx_labels(g, pos, font_size=18,font_family= font_name)

    # nx.draw_networkx(g,pos=pos,with_labels=True,font_family = font_name)
    # labels = nx.get_edge_attributes(g,'weight')
    # nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
    nx.draw_networkx_edges(g, pos, edgelist=edges,style='solid',
                          width=weights, edge_color=weights ,edge_vmin = min(weights), edge_vmax=max(weights))
    # plt.legend(g.nodes(),loc = 'upper right')
    plt.title(film_title,fontdict={'family': font_name, 
                        'color' : 'black',
                        'weight': 'bold',
                        'size': 40})
    plt.axis(False)
    plt.show()
def start(M_df,film_title,rank):    
    # M_df  = M_df.drop_duplicates(['original_title'], keep='first').reset_index(drop = True)
    data ,tfdidf_mat= film_tfdif(M_df,film_title)
    movieList = pd.DataFrame(extrasct_similar_Movie(data ,tfdidf_mat,film_title,rank),columns=['from','to','weight'])
    newworkPlot(movieList,film_title)


if __name__ =="__main__":
    M_df = pd.read_csv('./NetflexData/raw/movies_metadata.csv')
    start(M_df,'Iron Man',20)

