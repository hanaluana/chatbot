import requests
from bs4 import BeautifulSoup
import webbrowser

url = 'https://www.bithumb.com'
response = requests.get(url).text

doc = BeautifulSoup(response, 'html.parser')

tbody=doc.select_one('.coin_list')
#print(tbody)

name=[]
price=[]
coin={}

for ts in tbody.findAll('span',{'class':'blind'}):
    name.append(ts.text)
for ts in tbody.findAll('strong',{'class':'sort_real'}):
    price.append(ts.text)

for i in range(len(name)):
    coin[name[i]]=price[i]
    print('{:<20} : {:<10}'.format(name[i],coin[name[i]]))