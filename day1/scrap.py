# kospi 정보를 스크랩한다.

import requests
from bs4 import BeautifulSoup

url = 'http://finance.daum.net/'
response = requests.get(url).text
doc = BeautifulSoup(response,'html.parser')
result=doc.select_one('#boxIndexTabs > span > h4').text
print(result)

#print(response.status_code)
#print(response.text)

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
doc = BeautifulSoup(response,'html.parser')
result=doc.select_one('#KOSPI_now').text
print(result)






