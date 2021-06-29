import bs4
import urllib.request
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.+?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

base_url = 'http://www.koreaherald.com'
sub_menues = ['ct=020100000000','ct=020200000000','ct=020300000000','ct=020400000000','ct=020500000000',
            'ct=020600000000','ct=021200000000']

target_urls = []
for sub_menu in sub_menues:
    for i in range(1,2000):
        x = base_url+'/list.php?'+sub_menu+'ctv=0&np='+str(i)
        target_urls.append(x)

crawl_urls = []
for target_url in target_urls[0:10]:
    try:
        url = urllib.request.urlopen(target_url)
        bsObjs = bs4.BeautifulSoup(url,'html.parser')
        for bsObj in bsObjs.find('ul',{'class':'rollingList'}).findAll('li'):
            x = bsObj.find('a')['href']
            href = base_url+x
            crawl_urls.append(href)
            print(target_url)
    except:
        print(crawl_url)

crawl_texts = []
for crawl_url in crawl_urls[0:20]:
    try:
        url = urllib.request.urlopen(crawl_url)
        bsObjs = bs4.BeautifulSoup(url,'html.parser')
        raw_html = str(bsObjs.find('div',{'class':'content_view'})).replace("\n","").replace('\t','')
        content = cleanhtml(raw_html)
        crawl_texts.append(content)
    except:
        print(crawl_url)    

with open('koreaherald_crawl.txt', 'w') as f:
    for text in crawl_texts:
        f.write("%s\n" % text)Å