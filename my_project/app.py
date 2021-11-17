from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from bs4 import BeautifulSoup

app = Flask(__name__)
# 네이버 지도 api

#https://m.map.naver.com/search2/search.naver?query==마포구%20술집&sm=hty&style=v5

#query=술집
##영화 : old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# mongodb


category_region = '지역';
category_type = '분위기 및 주종';

client = MongoClient('localhost', 27017)
db = client.dbsparta
url = 'https://openapi.naver.com/v1/search/local.json?=query{}'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#네이버 지도
#지역
#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > div.item_info_inn > div > a
#한식
#ct > div.search_listview._content._ctList > ul > li:nth-child(1) > div.item_info > a.a_item.a_item_distance._linkSiteview > div > em
items= soup.select('ct > div.search_listview._content._ctList > ul > li > div.item_info')
# 술집명 > a.a_item.a_item_distance._linkSiteview > div
# 주종 및 테마 > a.a_item.a_item_distance._linkSiteview > div > em


#네이버 api 를 사용하기 위함!
headers = {
    'X-Naver-Client-Id': 'PziqS0nkbZr4wh0nTBQ4',
    'X-Naver-Client-Secret': 'PziqS0nkbZr4wh0nTBQ4',
}

for pub in items:
    a_tag=pub.select_one('div.item_info_inn > div > a')
    if a_tag is None:
        pubName = pub.text
        print(a_tag.text)

result = data.json()

#html 주기
@app.route('/')
def home():
    return render_template('index.html');


#클라이언트로부터 데이터 받기




## API 역할을 하는 부분
@app.route('/test', methods=['GET'])
def test_get():
    category_region_receive = request.args.get('category_region_give')
    print(category_region_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})

## API 역할을 하는 부분
@app.route('/test', methods=['POST'])
def test_post():
    category_region_receive = request.form['category_region_give']
    print(category_region_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})



# 출력 잘 되는지 확인한 부분
def hello_world():
    return 'Hello World';

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


