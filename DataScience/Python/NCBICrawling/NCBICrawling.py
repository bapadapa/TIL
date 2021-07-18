#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# 대상 URL
webPath = "https://www.ncbi.nlm.nih.gov/Traces/study/?acc="
# 검색할 파일명
user = ['SRP000003','GSE12578']
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
driver = webdriver.Chrome(options=chrome_option)
driver.implicitly_wait(10)

for target in user:
    driver.get(webPath+target)
    # sleep(5)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable(((By.ID,'t-rit-all'))))
    # driver.find_element_by_xpath('//*[@id="t-rit-all"]')
    sleep(2) 
    driver.find_element(By.ID,'t-rit-all').click()
    sleep(2)       
    fileName = max([filePath+ r'/'+ i for i in os.listdir(filePath)],key=os.path.getctime)
    if fileName == filePath+'/SraRunTable.txt':
        os.rename(os.path.join(filePath,fileName),os.path.join(filePath,target+'.txt'))
sleep(2)
driver.close()

