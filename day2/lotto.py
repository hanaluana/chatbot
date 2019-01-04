import random
import json
import requests
from bs4 import BeautifulSoup

print(sorted(random.sample(range(1,46),6)))

# 1. 나눔로또 api를 통해 우승 번호를 가져온다.
url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=837'
response = requests.get(url)

data = json.loads(response.read())
#doc = BeautifulSoup(response, 'json')
print(data)

#lottonumber = json.dumps(doc)
#print(lottonumber)
# 2. random으로 생성된 번호와 우승 번호를 비교해서 나의 등수를 알려준다.
# 1등 : 6개 번호 다 맞는거
# 2등: 5개 맞고, bonus 번호랑 맞음
# 3등: 5개 
# 4등: 4개
# 5등: 3개

dict_phonenumber = json.load(json_phonenumber) # json 파일을 dict타입으로 바꿔줌