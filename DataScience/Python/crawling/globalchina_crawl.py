import bs4
import urllib.request
import re

def cleanhtml(raw_html):
    cleanr = re.compile('<.+?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

base_url = 'http://www.globaltimes.cn'
sub_menu = {'china':['politics','society','diplomacy'],'business':['comments','Eye-on-The-Economy']}

sub_menu_urls = []
for key in sub_menu:
    for i in range(len(sub_menu[key])):
        url = base_url+'/'+key+'/'+sub_menu[key][i]
        sub_menu_urls.append(url)

target_urls = []
for sub_menu_url in sub_menu_urls:
    for i in range(2,11):
        x = sub_menu_url+'/index'+str(i)+'.html'
        target_urls.append(x)
target_urls.extend(sub_menu_urls)
        

crawl_urls = []
for target_url in target_urls:
    try:
        url = urllib.request.urlopen(target_url)
        bsObjs = bs4.BeautifulSoup(url,"html.parser")
        
        for bsObj in bsObjs.findAll('a'):
            href = bsObj['href']
            if ('shtml' in href):
                crawl_urls.append(href)
    except:
        print(crawl_url)
        
crawl_text = []
for crawl_url in crawl_urls:
    try:
        hdr = { 'User-Agent' : 'foobar' }
        req = urllib.request.Request(crawl_url, headers=hdr)
        crawl = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(crawl,"html.parser")
        raw_html = str(bsObj.find('div',{'class':'span12 row-content'})).replace("\n","")
        text = cleanhtml(raw_html)
        crawl_text.append(text)
    except:
        print(crawl_url)

with open('globalchina_crawl.txt', 'w') as f:
    for text in crawl_text:
        f.write("%s\n" % text)     