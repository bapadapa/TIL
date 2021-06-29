import bs4
import urllib.request
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.+?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

root_url = 'https://www.bbc.com'

url = urllib.request.urlopen(root_url+'/news')
bsObjs = bs4.BeautifulSoup(url)

crawl_urls = []

for bsObj in bsObjs.findAll('a',{'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'}):
    try:
        if ('www.bbc' not in str(bsObj)):
            href = root_url+bsObj['href']
            crawl_urls.append(href)
            print(href)
    except:
        print('ssss')

news = []
sport = []
for crawl_url in crawl_urls:
    if crawl_url[20:24] == "news":
        news.append(crawl_url)
    else:
        sport.append(crawl_url)

        

crawl_texts = []
for crawl_url in news:
    try:
        hdr = { 'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
                      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                      'Accept-Encoding': 'none',
                      'Accept-Language': 'en-US,en;q=0.8',
                      'Connection': 'keep-alive' }
        req = urllib.request.Request(crawl_url, headers=hdr)
        url = urllib.request.urlopen(req)
        bsObjs = bs4.BeautifulSoup(url,'html.parser')
        raw_html = str(bsObjs.findAll('p')).replace('\n','') 
        context = cleanhtml(raw_html)
        print(context)
        crawl_texts.append(context)
    except:
        print("crawl_url")
    
with open('bbc_crawl.txt', 'w') as f:
    for text in crawl_texts:
        f.write("%s\n" % text)    