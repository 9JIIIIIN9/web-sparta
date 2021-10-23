from flask import Flask, render_template, request, jsonify

# 계속 켜져 있음- 누가 새벽 3시에 들어올지 모르잖어-> 종료할 땐 오른쪽 위에 빨간 네모 클릭하기

app = Flask(__name__)


# hostname:5000 하면 저 index.html 을 불러옴

# route 이렇게 하는 건 get 방식임

@app.route('/')
def home():
    # render_template 은 html 안에 python 코드를 넣을 수 있게 해줌-> 해석을 해주는 거지
    return render_template('index.html')


# localhost:5000뒤에 /my_page 붙이면 이 함수 실행됨

# @app.route('/my_page')
# def my_page():
#     return 'my page!'

# method 를 직접 명시 http://localhost:5000/test 이렇게 치면 확인 가능
@app.route('/test', methods=['GET'])
def test_get():
    # 외우지 말구 계속 찾아서 쓰면 됨

    title_receive = request.args.get('title_give')
    print(title_receive)
    # 중괄호: 파이썬에서 딕셔너리 형태
    # json 형태로 변환해주는 코드
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})

@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form.get('title_give')
    # 둘 다 사용 가능
    #둘의 차이점 : ...은 잘 모르겠고 아래껄로 쓰는 게 낫대
    #title_receive = request.form.get('title_give')

    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
    # 포트 번호 5000에 띄워라
    # 주소를 local:5000 이라고 쳐봐도 나옴옴

# 내 컴퓨터에 웹 서버 실행한거 (요청했고) 실행해서 http 주소 눌러보면 hello world 로 응답 받은 걸 알 수 있어
