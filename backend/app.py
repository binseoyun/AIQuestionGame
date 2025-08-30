from flask import Flask

# Flask 애플리케이션 생성
app = Flask(__name__)

# '/' 경로로 GET 요청이 오면, 이 함수를 실행
@app.route('/') #서버의 기본 주소로 접속하면 hello_world 함수가 실행됨
def hello_world():
    return "Hello, Backend World!"

# 이 파일이 직접 실행될 때, 개발 서버를 구동
if __name__ == '__main__':
    app.run(debug=True)