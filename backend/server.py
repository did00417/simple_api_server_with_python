# app.py
# 가장 심플한 파이썬 API 서버 (Flask)
# 실행하면: http://localhost:5000/ 로 접속 시 "Hello, World!" 반환

from flask import Flask , jsonify, request

app = Flask(__name__)

@app.get("/")
def hello():
    return "Hello, World!"

@app.get("/ping")
def ping():
    return jsonify({"status": "test successful"})

@app.get("/users")
def get_users():
    return jsonify([
        {"id": 1, "username": "test1"},
        {"id": 2, "username": "test2"},
    ])

@app.get("/users/<int:user_id>")
def get_user(user_id):
    if user_id == 1:
        return jsonify({"id": 1, "username": "test1"})
    return jsonify({"message": "유저 없음"}), 404

@app.post("/users")
def create_user():
    data = request.json
    return jsonify({
        "message": "회원가입 완료",
        "username": data.get("username")
    }), 201

if __name__ == "__main__":
    # host=0.0.0.0 : 외부(다른 PC/컨테이너)에서도 접근 가능하게 열고 싶을 때
    # 로컬에서만이면 기본값(127.0.0.1) 써도 됨
    app.run(host="0.0.0.0", port=5000, debug=True)
