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

# --- 1. 사용자 인증 API ---

# [POST] /auth/register : 새로운 사용자 계정 생성
@app.route('/auth/register', methods=['POST'])
def register():
    global next_user_id # 전역 변수인 next_user_id를 수정하겠다고 선언

    # 1. 프론트엔드로부터 username과 password 받기
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # 2. 필수 정보가 누락되었는지 확인
    if not username or not password:
        return jsonify({"error": "사용자 이름과 비밀번호는 필수입니다."}), 400

    # 3. 이미 존재하는 사용자 이름인지 확인
    for user in users.values():
        if user['username'] == username:
            return jsonify({"error": "이미 존재하는 사용자 이름입니다."}), 409 # 409: Conflict

    # 4. 비밀번호를 해시(hash) 값으로 암호화
    password_hash = generate_password_hash(password)

    # 5. 새로운 사용자 정보 생성 및 저장
    new_user = {
        "id": next_user_id,
        "username": username,
        "password_hash": password_hash
    }
    users[next_user_id] = new_user
    next_user_id += 1
    
    print("새로운 사용자 등록:", new_user)
    print("현재 사용자 목록:", users)

    # 6. 프론트엔드에 성공 응답 보내기
    return jsonify({
        "user_id": new_user['id'],
        "username": new_user['username'],
        "message": "회원가입이 완료되었습니다."
    }), 201 # 201: Created

if __name__ == '__main__':
    app.run(debug=True)