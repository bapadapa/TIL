#%%
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
# 스크래핑
searchQ = "유동인구" # keyword input
startYear = 2000     # startyear input
endYear = 2021       # endyear input

print("start crawling..")

# path = 'C:/chromedriver.exe'
driver = webdriver.Chrome()
xpath = driver.find_element_by_xpath

#스타트업 검색
driver.get('https://www.dbpia.co.kr/')
keyword = driver.find_element_by_id('keyword')
keyword.clear()
keyword.send_keys(searchQ)
serach_click_btn = xpath("//*[@id='header']/div[5]/div[6]/div[2]/div[1]/a")
driver.execute_script("arguments[0].click();",serach_click_btn)

#날짜 지정 및 체크박스 설정
xpath("//*[@id='dev_sartYY']").send_keys(startYear)
xpath("//*[@id='dev_endYY']").send_keys(endYear)
click_btn = xpath("//*[@id='sidebar']/form/div[3]/div/div[1]/ul/li[4]/p/button")
driver.execute_script("arguments[0].click();",click_btn)

for i in range(1):
    time.sleep(0.5)
    try:
        btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pub_check_sort3_0']")))
        driver.execute_script("arguments[0].click()",btn)
        btn2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='pub_check_sort3_1']")))
        driver.execute_script("arguments[0].click()",btn2)
    except:
        print('retry')
        time.sleep(1)

# base_url = 'https://www.dbpia.co.kr/search/topSearch#none'
# test_list = []
# driver.get(base_url)

# 더보기
wCount = 0
while(True):
    time.sleep(1)
    try:
        more = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='contents']/div[2]/div[3]/div[3]/div[3]/div/a")))
        driver.execute_script("arguments[0].click()",more)
    except:
        print('retry')
        break
    wCount += 1
    print(" + page [{}]".format(wCount))


items_source = driver.page_source
soup = BeautifulSoup(items_source, 'html.parser')


items = soup.find('div','searchListArea').find('div','listBody').find('ul').find_all('li', 'item')

# 논문제목, 저자, 퍼블리셔, 저널명,볼륨,날짜, 초록
titleL = []
authorL = []
# authorsL = []
publisherL = []
journalL = []
volumeL = []
dateL = []
#keywordsL = []
use_countL = []
quotation_countL = []
abstractL = []
tLen = len(items)
print("start parsing")

iCount = 0
for item in items :
    iCount += 1
    if iCount % 20 == 0:
        print(" parsing.. [{}/{}]".format(iCount, tLen))

    title = ''
    try : title = item.find('div','titWrap').find('a').text
    except : title = ''

    author = ''
    try : author = item.find('li','author').text
    except : author = ''

    authors = ''
    try : authors = item.find('li','author').find('input')['value']
    except : authors = ''

    publisher = ''
    try : publisher = item.find('li','publisher').text
    except : publisher = ''

    journal = ''
    try : journal = item.find('li','journal').text
    except : journal = ''

    volume = ''
    try : volume = item.find('li','volume').text
    except : volume = ''

    date = ''
    try : date = item.find('li','date').text
    except : date = ''

    # 문제가 있어요...
    #keywords = ''
    #try : keywords = str(soup.find_all("dd", {"class": "word"}))
    #except : keywords = ''

    use_count = ''
    try : use_count = xpath('//*[@id="#pub_modalUsageChart"]/span').text
    except : use_count = ''

    quotation_count = ''
    try : quotation_count = xpath('//*[@id="#pub_modalQuoteChart"]/span').text
    except : quotation_count = ''

    abstract = ''
    baseDetailUrl = "https://www.dbpia.co.kr"
    pUrl = ''
    try : pUrl = item.find('div','titWrap').find('a')['href']
    except : pUrl = ''
    if (pUrl != ''):
        pUrl = baseDetailUrl + pUrl
        driver.get(pUrl)
        try : driver.find_element_by_xpath('//*[@id="#pub_modalOrganPop"]').click()
        except : pass
        time.sleep(0.1)
        try : driver.find_element_by_xpath('//*[@id="#pub_modalLoginPop"]').click()
        except : pass

        try :
            driver.find_element_by_xpath('//*[@id="pub_abstract"]/div[2]/div/div[1]/div[2]/a').click()
            eachPage = driver.page_source
            ePsoup = BeautifulSoup(eachPage, 'html.parser')
            abstract = ePsoup.find('div','abstFull').find('p','article').text
        except : abstract = ''

    titleL.append(title)
    authorL.append(author)
    # authorsL.append(authors)
    publisherL.append(publisher)
    journalL.append(journal)
    volumeL.append(volume)
    dateL.append(date)
    #keywordsL.append(keywords)
    use_countL.append(use_count)
    quotation_countL.append(quotation_count)
    abstractL.append(abstract)

print("date to .csv file")

resultDict = dict(title = titleL,
              author = authorL,
              publisher = publisherL,
              journal = journalL,
              volume = volumeL,
              date = dateL,
              #keywords = keywordsL,
              use_count = use_countL,
              quotation_count = quotation_countL,
              abstract = abstractL)
              
fName = "{}_{}_{}.csv".format(searchQ, startYear, endYear)

DB = pd.DataFrame(resultDict)

# 유동인구가 들어가지 않는 행 제거
DB_contains = DB['title'].str.contains("유동인구")
DB = DB[DB_contains]


# csv로 저장
DB.to_csv(fName)