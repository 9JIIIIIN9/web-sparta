#스크래핑 한다면 이렇게 따로 빼서 먼저 되는지 다 확인되면 기존 파일에 코드 추가하는 걸 추천@@@!!

import requests
from bs4 import BeautifulSoup

url = 'https://platum.kr/archives/120958'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


title = soup.select_one('meta[property="og:title"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
#contents 가 비어있지 않은 애들만 가져와라
#위에title, image 다 not 부분 추가해주는 게 좋아
desc = soup.select_one('meta[property="og:description"]:not([content=""])')['content']


print(title)
print(image)
# contents 가 비어있어서 안나올거야(url 사이트 참고) 그래서 위레 desc 코드에 :not 그 코드를 추가해준 것
print(desc)
# 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.