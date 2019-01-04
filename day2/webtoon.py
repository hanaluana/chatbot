import requests
from bs4 import BeautifulSoup
import webbrowser

url = 'https://m.comic.naver.com/webtoon/weekday.nhn?week='
weekdays=['mon','tue','wed','thu','fri','sat','sun']


for i in weekdays:
    names=[]
    imagess=[]
    urls = url+i
    response = requests.get(urls).text
    doc = BeautifulSoup(response, 'html.parser')
    for webtoons in doc.findAll('span',{'class': 'toon_name'}):
#       score = webtoons.select_one('.txt_score').text
        names.append(webtoons.text)
        #print(i,': ',webtoons.text)
    for images in doc.findAll('span',{'class':'im_br'}):
        links = images.findAll('img')
        for link in links:
            print(link['src'])
            imagess.append(link['src'])
            #webbrowser.open_new(link['src'])
    for j in range(len(names)):
        print(names[j],': ',imagess[j])
    for webs in doc.findAll('li'):
        webs2 = webs.findAll('a')
        for web in webs2:
            print(web['href'])
