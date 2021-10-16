import pymongo
from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
#5000실행했을 때
@app.route('/')
def home():
    return render_template('index.html')


# API 역할을 하는 부분
#http://localhost:5000/api/list
#json 형식으로 나타나있는 걸 볼 수 있음


#현업에서는 개당 고유 id 값을 지정해서 함. 영화배우 이름 겹칠 수도 있으니까-> 이건 꿀팁자료에 있음 (mongoDB objectID 사용법)
@app.route('/api/list', methods=['GET'])
def show_stars():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    #이거 하고 localhost/api/list 이거 실행해보면 json 형식으로 정보 쭉 나옴
    # _id =false 해야
    #mongoDB 에서 정렬해서 웹에 보낼 때 정렬이 되어있는 상태ㅣㅁ
    # 보내면서 조회할 때 정렬을 해도 된대 근데 우리는 DB에서 먼저 정렬을 해서 보낼거야
    #pymongo.ASCENDING inport 하기
    data = list(db.mystar.find({},{'_id' : False}).sort('like',pymongo.DESCENDING))
    #pymongo.DESCENDING 대신 -1 로 써도 됨 ASCENDING 은 1임('like',-1) 이런 식으로
    print(data)
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success', 'stars_list': data})


@app.route('/api/like', methods=['POST'])
def like_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form.get('name_give')

    #like 를 1만큼 증가시켜줘라 - 밑에 세줄 요약된 한 줄임
    db.mystar.update_one({'name':name_receive},{'$inc':{'like':1}})

    # print(name_receive)

    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    # star=db.mystar.find_one({'name':name_receive})
    # # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    # new_like=star['like']+1
    # # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    # # 참고: '$set' 활용하기!
    # db.mystar.update_one({'name':name_receive},{'$set':{'like':new_like}})

    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': f'{name_receive}like 완료'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form.get('name_give')
    print(name_receive)
    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    db.mystar.delete_one({'name':name_receive})
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': f'{name_receive} 삭제완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)