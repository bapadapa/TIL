# %%
from matplotlib import markers
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%
# bar Plot
width = 0.35
man = 30 
woman = 50
plt.bar([1,2],[man,woman] , width=width)
plt.show()
# %%
# iris 데이터 sepal_length 평균 막대그래프
iris = sns.load_dataset('iris')
y_length = iris.groupby('species').mean().sepal_length
plt.bar([0,1,2],y_length, width = 0.1)
# %%
# iris 데이터 종별로 sepal_length 와 sepal_width 막대그래프
x = np.array([0,1,2])
y1 = iris.groupby('species').mean().sepal_length
y2 = iris.groupby('species').mean().sepal_width
plt.bar(x,y1,width=0.2)
plt.bar(x+0.2,y2,width=0.2)
# %%
data = np.random.randint(1000)
x = np.linspace(np.min(data),np.max(data),1000)


# %%
# histgram
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)
#아래 2개 같은 의미
# kwargs = {'histtype':'stepfilled','alpha':0.3,'bins':40}
kwargs = dict(histtype='stepfilled', alpha=0.3, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)

# %%
# 지도데이터
cities = pd.read_csv('https://raw.githubusercontent.com/jakevdp/PythonDataScienceHandbook/master/notebooks/data/california_cities.csv')
lat,lon = cities['latd'],cities['longd']
plt.scatter(lon,lat, label = None, )
cities
# %%
import folium 
center = [36.60987638239402, 127.29005456137222]
m = folium.Map(
    location = center,
    zoom_start = 15
)
m
# %%
lati = lat.mean()
loni = lon.mean()
center = lati,loni

m = folium.Map(location=center, zoom_start=7)

for i in cities.index:
    folium.Circle(
        x,y = cities.values(['latd','longd']),
        location  = cities.loc[i,],        
        tooltip  = cities.loc[i,'city'],
        radius  = 200
    ).add_to(m)
m
# %%
cities.head()
# %%
birth = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/births.csv')
birth
# %%

# %%
