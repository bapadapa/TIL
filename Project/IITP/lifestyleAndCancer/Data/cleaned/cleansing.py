#%%
import numpy as np
import pandas as pd
import os

from pandas.core.reshape.merge import merge
from pandas.io.parsers import read_csv
cancerCase = pd.read_csv('../cancerCases_index.csv')
cancerDeath = pd.read_csv('../cancerDeath_index.csv')
Drink = pd.read_csv('../DrinkPerPerson_khealth.csv')
smoking = pd.read_csv('../smoking2_nosmokeguide.csv')
# %%
# cleansing
cancerCase = cancerCase[cancerCase['종류']=='사망자수' ]

def cleanCancer(df):
    years = df.columns[2:]
    result = pd.DataFrame()
    for i in range(len(years)):
        tmp= pd.DataFrame(df[years[i]]).rename(columns={years[i] : 'occur'})
        tmp['year'] = years[i] 
        tmp['type'] = df[df.columns[0]]
        result = result.append(tmp)
    return result
# cleanCancer(cancerCase).to_csv('./Data/cleaned/cancerCase.csv',encoding='utf-8-sig',index=False)

years = smoking.columns[2:]
result = pd.DataFrame()
for i in range(len(years)):
    tmp = pd.DataFrame(smoking['성별']).rename(columns={'성별':'sex'})
    tmp['year'] = years[i][:4]
    tmp['smokingRate'] = smoking[years[i]]
    result = result.append(tmp)
# result.to_csv('./Data/cleaned/smoking.csv',encoding='utf-8-sig',index=False)

#%%
files =  os.listdir('../aa')
files = files[:len(files)//2]
files[0][:-4]
pd.read_csv('../aa/'+files[0])
#%%


for i in range(len(files)):
    result = pd.DataFrame()
    df = pd.read_csv('../aa/'+files[i])
    print(df)
    years = df.columns[1:]
    for year in years:        
        tmp = pd.DataFrame([df[df.columns[0]],df[year]]).T.rename(columns = {df.columns[0] : 'type',year : files[i][:-4]})            
        tmp['year'] = year
        result = result.append(tmp)
    result.loc[(result.type == '남자')|(result.type == '전체')|(result.type == '여자')|(result.type == '총배출량(백만 톤 CO2eq.)') ].to_csv('./'+files[i],encoding='utf-8-sig',index=False)

#%%


df = pd.read_csv('../aa/employmentrate.csv')
df  = df.loc[:2]
years = df.columns[2:] 
result = pd.DataFrame()
for year in years:
    tmp = pd.DataFrame([df[df.columns[0]], df[year]]).T.rename(columns={df.columns[0] : 'type', year : 'employmentrate'})
    tmp['year'] = year
    result = result.append(tmp)
result.to_csv('./employmentrate.csv',encoding='utf-8-sig',index=False)







