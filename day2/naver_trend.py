import requests
from bs4 import BeautifulSoup
import webbrowser

# 1. python에게 naver.com 요청을 보내서
url = 'https://www.naver.com'

# 2. 응답 받은 문서를 저장하고
response = requests.get(url).text

# 3. BeautifulSoup 정보를 찾기 좋게 만들고
doc = BeautifulSoup(response, 'html.parser')
#print(dir(doc))

# 4. 우리가 원하는 정보를 뽑아온다.

# result=doc.select_one('.ah_k').text
# print(result)
# url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='
# webbrowser.open_new(url+result)

for trend in doc.findAll('span',{'class': 'ah_k'})[:5]:
    print(trend.text)
    url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query='
    #webbrowser.open_new(url+trend.text)