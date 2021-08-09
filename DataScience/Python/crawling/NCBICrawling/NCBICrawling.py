#%%

#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
import json

from time import sleep
import os

import pandas as pd
import json

# Json 읽기
with open("config.json", 'r', encoding = 'utf-8') as common:
        config = json.load(common)
save_path = os.path.join(os.getcwd(),"New_NCBI_metadata")
# Path 에 디렉토리가 없으면 생성해줌
if not os.path.isdir(save_path):
        os.mkdir(save_path)

# 크롬브라우저를 백그라운드로 실행하게 해줌
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

options.add_experimental_option("prefs", {
    ## "excludeSwitches":["enable-logging"],
    "download.default_directory": save_path
})

browser = webdriver.Chrome(executable_path=config['driver_path'],chrome_options=options)
# 최종적으로 다운로드 여부 확인하기위해 생성
result = pd.DataFrame(columns=['MGnify_ID','S_ID','Download'])
# ERP 가져오기
for target in config['MGnify_ID']:
    try:
        browser.get(config['analysis_path']+target)
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "ebi_ena_links"))
        )
        sleep(1)
        # 파일명 가져오기
        target_name = browser.find_element_by_id('ebi_ena_links').text.split(' ')[-1][1:-1]
        print(browser.find_element_by_id('ebi_ena_links').text.split(' ')[-1][1:-1])
        # 해당 파일 검색
        browser.get(config['data_path']+target_name)
        try:            
            check = True
            print(f"{target} 로딩 중")
            # 파일이 없는 페이지 혹은 있는페이지 2가지 경우가 있어 아래와 같이 while문을 돌림
            while True:
                if EC.presence_of_element_located((By.ID, "t-rit-all")) :
                    print(f"{target} 로딩 완료")
                    sleep(3) 
                    break
                elif EC.presence_of_element_located((By.CLASS_NAME, "ui warning icon message")):                    
                    check = False
                    break
            # Warning페이지 접속시 종료
            if not check :
                print(f"{target} 파일이 없습니다.")
                result = result.append({'MGnify_ID':target,'S_ID':target_name,'Download':'N'}, ignore_index=True)
                pass
            # 다운로드 버튼 클릭
            browser.find_element(By.ID,'t-rit-all').click()            
            print(f"{target} 다운로드중")
            sleep(1)
            # 다운로드 다 될때까지 대기
            while True:                
                sleep(1)
                if os.path.isfile(save_path+'/SraRunTable.txt'):
                    fileName = max([save_path+ r'/'+ i for i in os.listdir(save_path)],key=os.path.getctime)
                    print(fileName)
                    if fileName == save_path+'/SraRunTable.txt':
                        os.rename(os.path.join(save_path,fileName),os.path.join(save_path,target+'.txt'))
                        print(f"{target} 파일명 변경")
                        print(max([save_path+ r'/'+ i for i in os.listdir(save_path)],key=os.path.getctime))
                        result = result.append({'MGnify_ID':target,'S_ID':target_name,'Download':'Y'}, ignore_index=True)
                        break
            print(f"{target} 다운로드 완료")

        except:
            print(f'{target_name} 파일없는 것 같습니다.')
            result = result.append({'MGnify_ID':target,'S_ID':target_name,'Download':'N'}, ignore_index=True)
            pass
    except:
        print('fail')
browser.close()
result.to_csv('./result.csv',encoding="utf-8-sig")
#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
import json

from time import sleep
import os

import pandas as pd
import json
# df = pd.read_csv("result.csv")
# print(result[result.Download == 'N'])
# df=  df[result.Download == 'N']
# df = df[['MGnify_ID','S_ID','Download']]
# df.reset_index(drop=True)

df = pd.read_csv("result.csv")
df = df[['MGnify_ID','S_ID','Download']]
print(df)
result = pd.DataFrame(columns=['MGnify_ID','S_ID','Download'])

with open("config.json", 'r', encoding = 'utf-8') as common:
        config = json.load(common)
save_path = os.path.join(os.getcwd(),"New_NCBI_metadata")
# Path 에 디렉토리가 없으면 생성해줌
if not os.path.isdir(save_path):
        os.mkdir(save_path)

result[result.Download == 'N']
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_experimental_option("prefs", {
    ## "excludeSwitches":["enable-logging"],
    "download.default_directory": save_path
})

browser = webdriver.Chrome(executable_path=config['driver_path'],chrome_options=options)
# ERP 가져오기

# 
cnt,s_cnt ,f_cnt =0,0,0
for target in df.itertuples(index=False):
    # 크롬으로 돌릴 때 메모리가 부족한 경우가 많은 것 같아서 50회마다 크롬을 재시작해줌
    if cnt%50 == 49:
        browser.close()
        browser = webdriver.Chrome(executable_path=config['driver_path'],chrome_options=options)
        sleep(2)
        
    cnt +=1
    print(f"{cnt}/560")
    
    browser.get(config['data_path']+target[1])
    try:
        check = True
        print(f"{target[0]} 로딩 중")
        while True:
            
            if EC.presence_of_element_located((By.ID, "t-rit-all")) :
                print(f"{target[0]} 로딩 완료")
                sleep(3) 
                break
            elif EC.presence_of_element_located((By.CLASS_NAME, "ui warning icon message")):                    
                check = False
                break
        if not check :
            print(f"{target[0]} 파일이 없습니다.")
            result = result.append({'MGnify_ID':target[0],'S_ID':target[1],'Download':'N'}, ignore_index=True)
            f_cnt+=1
            print(f"{cnt}개 중 , 성공 : {s_cnt} 실패 :  {f_cnt}")
            print('------------------------------------------')
            pass        
        browser.find_element(By.ID,'t-rit-all').click()            
        print(f"{target[0]} 다운로드중")
        sleep(1)
        # 다운로드 다 될때까지 대기
        while True:                
            sleep(1)
            if os.path.isfile(save_path+'/SraRunTable.txt'):
                fileName = max([save_path+ r'/'+ i for i in os.listdir(save_path)],key=os.path.getctime)
                print(fileName)
                if fileName == save_path+'/SraRunTable.txt':
                    os.rename(os.path.join(save_path,fileName),os.path.join(save_path,target[0]+'.txt'))
                    print(f"{target[0]} 파일명 변경 성공")
                    print(max([save_path+ r'/'+ i for i in os.listdir(save_path)],key=os.path.getctime))
                    result = result.append({'MGnify_ID':target[0],'S_ID':target[1],'Download':'Y'}, ignore_index=True)
                    s_cnt+=1
                    print(f"{cnt}개 중 , 성공 : {s_cnt} 실패 :  {f_cnt}")
                    print('------------------------------------------')

                    break
        print(f"{target[0]} 다운로드 완료")
    except:
        print(f'{target[1]} 파일없는 것 같습니다.')
        result = result.append({'MGnify_ID':target[0],'S_ID':target[1],'Download':'N'}, ignore_index=True)        
        f_cnt+=1
        print(f"{cnt}개 중 , 성공 : {s_cnt} 실패 :  {f_cnt}")
        print('------------------------------------------')
        pass

browser.close()
result.to_csv('./result2.csv',encoding="utf-8-sig")
#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options
import os
# 대상 URL
webPath = "https://www.ncbi.nlm.nih.gov/Traces/study/?acc="
config = read_json()
# 검색할 파일명
user = config['MGnify_ID']
# 설치할 경로
filePath= os.getcwd() + r'\Datas'
# 경로에 디렉토리 없을시 생성
if not os.path.isdir(filePath):
    os.mkdir(filePath)
    
# 크롬 설치 경로 설정
prefs = {'download.default_directory':filePath}
chrome_option = Options()
chrome_option.add_experimental_option('prefs',prefs)
# 웹드라이버 생성
driver = webdriver.Chrome(config['driver_path'],options=chrome_option)
driver.implicitly_wait(10) 

for target in user:  
    driver.get(webPath+target)
    # sleep(5)
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(((By.ID,'t-rit-all'))))
        sleep(2) 
        driver.find_element(By.ID,'t-rit-all').click()
        sleep(2)       
        # 대상디렉토리의 모든 파일명 확인 후 가장 최근파일 조회
        fileName = max([filePath+ r'/'+ i for i in os.listdir(filePath)],key=os.path.getctime)
        # 파일명 변경
        if fileName == filePath+'/SraRunTable.txt':
            os.rename(os.path.join(filePath,fileName),os.path.join(filePath,target+'.txt'))
    except:
        pass
    # driver.find_element_by_xpath('//*[@id="t-rit-all"]')
    
sleep(2)
driver.close()
#------------------------------------------------------------------
#%%
# -*- coding: utf-8 -*- 
# -*- coding: euc-kr -*- 
from posixpath import join
from typing import ValuesView
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
from time import sleep
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

print("====================================================================================================")

driver_path=r"C:\Users\painc\Anaconda3\bin\chromedriver"

def check_path(Path):
    if not os.path.isdir(Path):
        os.mkdir(Path)
check_path(os.path.join(os.getcwd(),"New_NCBI_metadata"))
save_path = os.path.join(os.getcwd(),"New_NCBI_metadata")
check_path(os.path.join(os.getcwd(),"MGnify_metadata"))
meta_path = os.path.join(os.getcwd(),"MGnify_metadata")

meta_file_list = os.listdir(meta_path)

search = "_metadata.txt"


for i, word in enumerate(meta_file_list):
    if search in word: 
        meta_file_list[i] = word.strip(search)

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

options.add_experimental_option("prefs", {
  ## "excludeSwitches":["enable-logging"],
  "download.default_directory": save_path
})

browser = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
wait = WebDriverWait(browser, 30)

meta_len = len(meta_file_list)

print("Start Crawling! \n")

for target in meta_file_list:
  print("Start", target,"Read table!")
  
  MGnify_metadata = pd.read_table(os.path.join(meta_path,target+'_metadata.txt'),sep ="\t",index_col=0)
  
  print("Start to find",target,"sample ID")

  SRA_column_name_t = MGnify_metadata.filter(regex='study_attributes.secondary-accession')
  if (SRA_column_name_t.empty):
    SRA_column_name_t = MGnify_metadata.filter(regex='study_attributes.bioproject')

  SRA_column_name = list(SRA_column_name_t)
  SRA_ID = MGnify_metadata[SRA_column_name].value_counts()
  SRAID = list(SRA_ID.index)
  temp = SRAID[0][0]

  print("ID is",temp, "and download that!")

  new_file_name = os.path.join(save_path,target+'_SraRunTable.txt')

  if os.path.exists(new_file_name):
    print("File exists!! \n")
    continue

  browser.get("https://www.ncbi.nlm.nih.gov/Traces/study/")

  browser.implicitly_wait(10) #10초대기 설정

  
  browser.find_element_by_xpath('.//*[@id="id-search-form"]/div[2]/input').send_keys(temp)
  
  
  try:
    
    wait.until(EC.presence_of_element_located(((By.XPATH,'.//*[@id="id-search-form"]/div[2]/button'))))
    wait.until(EC.element_to_be_clickable(((By.XPATH,'.//*[@id="id-search-form"]/div[2]/button'))))

    browser.find_element_by_xpath('.//*[@id="id-search-form"]/div[2]/button').click()

    wait.until(EC.element_to_be_clickable(((By.ID,'t-rit-all'))))

    browser.find_element(By.ID, 't-rit-all').click()
    
    # if(os.path.isfile(os.path.join(save_path,'SraRunTable.txt'))):
    #   print("Download done SraRunTable")
    # else:
    #   print("Not yet download.....sleep 60 second....")
    #   sleep(60)
    #   if(os.path.isfile(os.path.join(save_path,'SraRunTable.txt'))):
    #     print("Download done SraRunTable")
    #   else:
    #     print("Not yet download.....sleep 60 second....")
    #     sleep(120)
    #     if(os.path.isfile(os.path.join(save_path,'SraRunTable.txt'))):
    #       print("Download done SraRunTable")
    #     else:
    #       print("Not yet download.....sleep 60 second....")
    #       sleep(180)
    

    if(not(os.path.isfile(os.path.join(save_path,'SraRunTable.txt')))):
        print("...........Not yet.......")

    while 1:
      if(os.path.isfile(os.path.join(save_path,'SraRunTable.txt'))):
        print("Download done SraRunTable")
        break


      
    os.rename(os.path.join(save_path,'SraRunTable.txt'), os.path.join(save_path,target+'_SraRunTable.txt'))
    print("Done!! Do check this table!! \n")
  
  except Exception as e:
    print("ERROR : "+str(e))
    print(f"ERROR : {+str(e)}")


    print(target,"NCBI metadata Download fail!! \n")
    continue
    
  
