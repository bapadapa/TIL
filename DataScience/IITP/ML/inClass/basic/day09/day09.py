#%%
from datetime import datetime
import pandas as pd
import numpy as np

#%%
date = datetime(year = 2021, month = 6 , day = 30)
date = []
for year in range(2000,2022):
    for month in range(1,13):
        for day in range(1,31):
            try:
                date.append(datetime(year = year,month=month,day = day))
            except:
                pass
#strftime => 날짜/시간 -> String
# date[0].strftime('%A')
# 아래는 에러~~ series 에는 strftime함수가 없다~
# pd.Series(date).strftime('%A')
pd.Series(date).apply(lambda x : x.strftime('%A'))
# %%
# np.array('year-month-day hour:min:sec',dtype=np.datetime64)
# np.array('2021-06-22y 10:07:00',dtype=np.datetime64)
date = np.array('2019-10-01',dtype=np.datetime64)
date

# %%
# vector 연산
date = date+ np.array(12)
date

# %%
date + pd.to_timedelta(np.arange(12),'D')

# %%
# 시간 범위
data['2018-01-01':'2018-12-31']
# %%
# 구간으로 날짜 지정, 구간도 지정할 수 있다!
data = pd.date_range('2021-01-01','2021-12-31')
print(date)
# 갯수 지정
date = pd.date_range('2021-01-01',periods=12,freq='D')
date
# %%
## 2021 1월 1일부터 현재까지 date생성
pd.date_range('2021-01-01',datetime.now() ,freq='H')
## 강사님 답
(pd.to_datetime('2021-06-22') - pd.to_datetime('2021-01-01') ).astype('str').str.replace()


# %%
# install 할 것
# pip install finance-datareader
# pip install beautifulsoup4

# %%
import FinanceDataReader as fdr
google = fdr.DataReader('GOOGL', '2010-01-01', '2018-12-31')
google.head()


# %%
%matplotlib inline
google['Close'].plot()
# %%
import matplotlib.pyplot as plt
goog = google['Close']
goog.plot(alpha=0.5, style='-')
goog.resample('BA').mean().plot(style=':')  # 시간간격 재조정, business year의 마지막 날의 평균
goog.asfreq('BA').plot(style='--'); # 시간간격 재조정
plt.legend(['input', 'resample', 'asfreq'],
           loc='upper left');
# %%
fig, ax = plt.subplots(1, sharex=True)
data = goog.iloc[:10] 
print(data)
data.asfreq('D').plot(ax=ax, marker='o') # 일간격으로 했을 떄 중간에 비어있는 데이터 존재
# %%
goog.plot(alpha = 0.5, style = '-')
goog.re
# %%
# 데이터 채워넣기
fig, ax = plt.subplots(1, sharex=True)
data = goog.iloc[:10]
data.asfreq('D', method='bfill').plot(ax=ax, style='-o')
# 아래 2개는 동일함!
# data.asfreq('D', method='ffill').plot(ax=ax, style='--o')
data.asfreq('D').fillna(method='ffill').plot(ax=ax, style='--o')
ax.legend(["back-fill", "forward-fill"]);

# %%
fig, ax = plt.subplots(3, sharey=True)

# apply a frequency to the data
goog = goog.asfreq('D', method='pad')

goog.plot(ax=ax[0])
goog.shift(900).plot(ax=ax[1])
goog.tshift(900).plot(ax=ax[2])

# legends and annotations
local_max = pd.to_datetime('2013-11-05')
offset = pd.Timedelta(900, 'D')

ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[2].set(weight='heavy', color='red')
ax[0].axvline(local_max, alpha=0.3, color='red')

ax[1].legend(['shift(900)'], loc=2)
ax[1].get_xticklabels()[2].set(weight='heavy', color='red')
ax[1].axvline(local_max + offset, alpha=0.3, color='red')

ax[2].legend(['tshift(900)'], loc=2)
ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
ax[2].axvline(local_max + offset, alpha=0.3, color='red');
# %%
## 수익률

ROI = 100 * (goog.tshift(-365) / goog - 1)
ROI.plot()
plt.ylabel('% Return on Investment');

# %%
print(goog[0].goog.tshift(-365)[0],(goog -1)[0])

# %%
## Matplotlib-basic
import matplotlib as mpl
import numpy as np
%matplotlib inline
plt.style.use('classic')
# %%
x = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');
fig.savefig('plot1.png')
# %%
# 이미지 불러오기
from IPython.display import Image
Image('plot1.png')
# %%
# 원그리기
x = np.linspace(0,1,100)
y = np.sqrt(0.5**2 - x**2)
plt.plot(x,y)

# %%
plt.figure()  # create a plot figure

# create the first of two panels and set current axis
plt.subplot(3, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))

# create the second panel and set current axis
plt.subplot(3, 1, 2)
plt.plot(x, np.cos(x));

plt.subplot(3,1,3)
plt.plot(x, np.exp(x))
# %%
funcs = [np.sin(x),np.cos(x),np.tan(x), np.tanh(x), np.log(x),np.exp(x)]
fig ,ax = plt.subplot(len(funcs))
for i in range(len(funcs)):
    ax[i].plot(x,funcs[i]) 



# %%
import numpy as np
x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--')
plt.title('한글 제목');
# %%
# Seaborn
import matplotlib.pyplot as plt
plt.style.use('classic')
%matplotlib inline
import numpy as np
import pandas as pd

# %%
rng = np.random.RandomState(0)
x = np.linspace(0, 10, 500)
y = np.cumsum(rng.randn(500, 6), 0)
y
# %%
z = np.cumsum(np.arange(10))
# Matplotlib
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
# %%
# seaborn style 적용
import seaborn as sns
sns.set()

plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left');
# %%    
# histogram

data = np.random.multivariate_normal([0, 0], [[5, 2], [2, 2]], size=2000)
data = pd.DataFrame(data, columns=['x', 'y'])

for col in 'xy':
    plt.hist(data[col], density=True, alpha=0.5)

#%%
tips = sns.load_dataset('tips')
tips.head()
tips['tip_pct'] = 100 * tips['tip'] / tips['total_bill']
tips.head()
# %%
# kind = 'box'
with sns.axes_style(style='ticks'):
    g = sns.catplot("day", "total_bill", "sex", data=tips, kind="box")
    g.set_axis_labels("Day", "Total Bill");
# %%
x  = np.random.randint(10,15,100)
x = np.concatenate([x,np.array([100,13])])
x = list(x)
x.pop(100)
plt.boxplot(x)
# %%
with sns.axes_style('white'):
    # sns.jointplot("total_bill", "tip", data=tips, kind='hex')    
    sns.jointplot("total_bill", "tip", data=tips)
# %%
planets = sns.load_dataset('planets')
planets.head()
# kind = 'count'

with sns.axes_style('white'):
    g = sns.catplot("year", data=planets, aspect=2,kind="count", color='steelblue')
    g.set_xticklabels(step=5)

# %%
planets.groupby(['year']).sum()
# %%
with sns.axes_style("white"):
    g = sns.catplot("year",data = planets, aspect= 4.0 ,kind = "count", hue = "method",order=range(2001,2015))
    g.set_ylabels('nubmer of planets Discovered')
# %%

import pandas as pd
import io
import requests

content=requests.get('https://raw.githubusercontent.com/jakevdp/marathon-data/master/marathon-data.csv').content
data = pd.read_csv(io.StringIO(content.decode('utf-8')))
data.head()

data = pd.read_clipboard(sep = ',')
data.head()
# %%
import datetime

def convert_time(s):
    h, m, s = map(int, s.split(':'))
    return h*60*60 + m*60 + s

data['split'] = data['split'].apply(convert_time)
data['final'] = data['final'].apply(convert_time)
data.head()
# %%
