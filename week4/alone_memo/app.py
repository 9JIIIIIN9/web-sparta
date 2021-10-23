from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.

@app.route('/')
def home():
    return render_template('index.html')


#create 하는 거
@app.route('/memo', methods=['POST'])
def post_article():
    #스크래핑 코드 여기에 넣을 것-> meta_prac 에서 코드 다 작성하고 가져와
    # 안그러면 계속 여기서 돌려봐야 되잖아아
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # print(url_receive)
    # print(comment_receive)
    # 1. 클라이언트로부터 데이터를 받기
    # 2. meta tag를 스크래핑하기
    url = 'https://platum.kr/archives/120958'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')


    # contents 가 비어있지 않은 애들만 가져와라
    # 위에title, image 다 not 부분 추가해주는 게 좋아


    # 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.
    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_title = og_title['content']
    url_description = og_description['content']
    url_image = og_image['content']

    article = {'url': url_receive, 'title': url_title, 'desc': url_description, 'image': url_image,
               'comment': comment_receive}

    # 3. mongoDB에 데이터 넣기
    db.articles.insert_one(article)


    # doc ={
    #     "title":title,
    #     "image":image,
    #     "desc":desc,
    #     "url":url_receive,
    #     "comment":comment_receive
    # }
    # db.articles.insert_one(doc)


    return jsonify({'result': 'success'})


#메모 가져오는 ㄴ거
@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    result = list(db.articles.find({}, {'_id': 0}))

    # 2. articles라는 키 값으로 articles 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
