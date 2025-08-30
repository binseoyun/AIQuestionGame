from flask import Flask, request, jsonify
# 비밀번호를 안전하게 암호화하기 위한 라이브러리
from werkzeug.security import generate_password_hash, check_password_hash
#Flask를 설치할 때 함께 설치되는 라이브러리로, 비밀번호를 안전한 해시(hash) 값으로 변환하고, 나중에 입력된 비밀번호가 해시 값과 일치하는지 검증하는 기능을 제공합니다.
app = Flask(__name__)

# --- 데이터베이스 대용 (임시) ---
# 실제로는 PostgreSQL 같은 DB를 사용해야 합니다.
users = {} # 사용자 정보를 저장할 딕셔너리
next_user_id = 1 # 다음 사용자에게 부여할 ID
# --------------------------------

@app.route('/')
def hello_world():
    return "Hello, Backend World! The server is running."

# 이 아래에 회원가입 코드를 추가할 예정입니다.

if __name__ == '__main__':
    app.run(debug=True)