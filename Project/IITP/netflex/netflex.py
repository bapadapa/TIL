#%%
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
    idx = M_df[M_df.title == title].index    
    for genre in pd.DataFrame(ast.literal_eval(df[df.title == title].genres[idx[0]])).name :
        result = result.append(df[df.genres.str.contains(genre)])
    return(result.drop_duplicates().reset_index(drop = True))

def film_tfdif(metadatas,filmName,extract_genre =extract_genre):
    films = extract_genre(metadatas,filmName)
    films = films[['title','overview']]
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
    for similarity, movie_id in match(tfidf_mat,data[data.title == title].index[0],rank):
        movieList.append((title, data.loc[movie_id,'title'],similarity))
    return movieList

def networkPlot(movieList,film_title,rank):
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

    nx.draw_networkx_edges(g, pos, edgelist=edges,style='solid',
                          width=weights, edge_color=weights ,edge_vmin = min(weights), edge_vmax=max(weights))
    # plt.legend(g.nodes(),loc = 'upper right')
    plt.title(film_title,fontdict={'family': font_name, 
                        'color' : 'black',
                        'weight': 'bold',
                        'size': 40})
    plt.axis(False)
    plt.savefig('./NetflexData/output/'+film_title+'_'+str(rank)+'.png')
    plt.show()
def start(M_df,film_title,rank):    
    # M_df  = M_df.drop_duplicates(['title'], keep='first').reset_index(drop = True)
    data ,tfdidf_mat= film_tfdif(M_df,film_title)
    movieList = pd.DataFrame(extrasct_similar_Movie(data ,tfdidf_mat,film_title,rank),columns=['from','to','weight'])
    networkPlot(movieList,film_title,rank)


if __name__ =="__main__":
    M_df = pd.read_csv('./NetflexData/raw/movies_metadata.csv')
    start(M_df,'Lucifer',20)
