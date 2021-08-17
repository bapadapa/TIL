#%%
import numpy as np
import pandas as pd
from pandas.core.reshape.merge import merge
from pandas.core.tools.datetimes import Scalar
from seaborn.relational import scatterplot
from sklearn.base import TransformerMixin

merged = pd.read_csv('../Data/cleaned/merged.csv')
cancerMerged = pd.read_csv('../Data/cleaned/cancerMerge.csv')

# %%
# 데이터 가져오기
tmp = merged[merged.type=='남자']
tmp = tmp[tmp.columns[1:]]
# 암데이터 가져오기
cancer =cancerMerged[cancerMerged.type==cancerMerged.loc[0].type]
cancer = cancer.rename(columns = {"type":"cancerType"})
cancer = cancer.astype({'year':int})
cancer = cancer[['year','occur','Death']]

#%%
# 암환자 및 요소들 병합 및 String 을 int로 변환
joined = pd.merge(tmp,cancer,left_on='year', right_on='year', how='inner')
joined = joined.set_index('year')
joined= joined[joined.columns[::-1]]
joined = joined.drop('삶의 만족도',axis=1)

joined = joined.dropna()
for colName in joined.columns[:2]:
    for i in range(len(joined[colName])):
        joined[colName].iloc[i] = float(joined[colName].iloc[i].replace(',',''))

# 정규화
def normalization(x):
    min_value = min(x)
    max_value = max(x) 
    return list(map(lambda x: (x-min_value)/(max_value-min_value), x))
# DF의 모든 값 정규화   
for i in joined.columns:
    joined = joined.apply(lambda x : normalization(x))
joined = joined.rename(columns={'Death' : '암사망자','occur':'암발생율'})
joined.corr()

#%%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import networkx as nx

# font_path = "C:/Users/admin/AppData/Local/Microsoft/Windows/Fonts/NanumGothicCoding-Bold.ttf" # 폰트 파일 위치
font_path = "C:/Windows/Fonts/malgunbd.ttf" # 폰트 파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
df= joined.corr(method='pearson')
# 그림 사이즈 지정
fig, ax = plt.subplots( figsize=(7,7) )

# 삼각형 마스크를 만든다(위 쪽 삼각형에 True, 아래 삼각형에 False)
mask = np.zeros_like(df, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# 히트맵을 그린다
sns.heatmap(joined.corr(method='pearson'), 
            cmap = 'RdYlBu_r', 
            annot = True,   # 실제 값을 표시한다
            mask=mask,      # 표시하지 않을 마스크 부분을 지정한다
            linewidths=.5,  # 경계면 실선으로 구분하기
            cbar_kws={"shrink": .5},# 컬러바 크기 절반으로 줄이기
            vmin = -1,vmax = 1   # 컬러바 범위 -1 ~ 1
           ) 

plt.savefig("../Data/pictures/corrPlot_남자_" +  ".png", format="PNG")
plt.show()

               

def corr_network(G, corr_dir, min_corr):
    font_path = "C:/Windows/Fonts/malgunbd.ttf" # 폰트 파일 위치
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    H = G.copy()    
    # 상관관계에 따라 값 변경 ( 긍정 ,부정 )
    for stock1, stock2, weight in G.edges(data=True):
        # 양의 상관계수일때
        if corr_dir == "positive":
            # 양의 상관관계만 보기 위해 weight["weight"] <0 를 이용하고,
            # weight["weight"] < min_corr 를 이용하여 최소 weight을 볼 수 있다.
            if weight["weight"] <0 or weight["weight"] < min_corr:
                H.remove_edge(stock1, stock2)
        # 음의 상관계수일 때
        else:
            # 양의 상관관계만 보기 위해 weight["weight"] <0 를 이용하고,
            # weight["weight"] < min_corr 를 이용하여 최소 weight을 볼 수 있다.
            if weight["weight"] >=0 or weight["weight"] > min_corr:
                H.remove_edge(stock1, stock2)
                
    
    # edges,weights 리스트 만들기  
    edges,weights = zip(*nx.get_edge_attributes(H,'weight').items())
    
    # 간선의 너비 늘리기 ( corr를 이용해 구현해서 가중치 안 늘리면 너무 가늘게 나옴)
    weights = tuple([(1+abs(x))**2 for x in weights])

    #positions
    positions=nx.circular_layout(H)
    
    plt.figure(figsize=(15,15))
    # 노드 디자인
    nx.draw_networkx_nodes(H,positions, node_color='#BB78FF', node_size=300, alpha=0.9)
    # 라벨 디자인
    nx.draw_networkx_labels(H, positions,font_color='white', font_size=30, font_family=font_name)
    # 들어온 값이 긍정이라면 
    if corr_dir == "positive":
        e_color = plt.cm.GnBu 
    else:
        e_color = plt.cm.PuRd
        
    # 엣지 그리기
    nx.draw_networkx_edges(H, positions, edgelist=edges,style='solid',
                          width=weights, edge_color = weights, edge_cmap = e_color,
                          edge_vmin = min(weights), edge_vmax=max(weights))

    # 겉에 틀? 지우기
    plt.axis('off')
    #saves image
    
    plt.legend(loc='center')
    plt.title('남자',fontdict={'family': font_name, 
                    'color' : 'white',
                    'weight': 'bold',
                    'size': 40})
    plt.savefig("../Data/pictures/newwork_Plot_남자_" + corr_dir + ".png", format="PNG")
    plt.show()

from matplotlib import font_manager, rc
# font_path = "C:/Users/admin/AppData/Local/Microsoft/Windows/Fonts/NanumGothicCoding-Bold.ttf" # 폰트 파일 위치
font_path = "C:/Windows/Fonts/malgunbd.ttf" # 폰트 파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
#extracts the indices from the correlation matrix, which are the stocks
# 상관계수들의 값(이름) 저장
stocks = joined.corr().index.values

# 각 상관계수 값 메트릭스로 추출  후 그래프 생성
corr_Graph = nx.from_numpy_matrix(np.asmatrix(joined.corr()))

# 각 노드에 이름 부여
corr_Graph = nx.relabel_nodes(corr_Graph,lambda x: stocks[x])

# 각 엣지에 상관계수를 weight으로 부여
corr_Graph.edges(data = True)

corr_network(corr_Graph,corr_dir="negative",min_corr = -0.5)
corr_network(corr_Graph,corr_dir="positive",min_corr = 0.5)

#%%
