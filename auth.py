import jwt
import datetime
from flask import request, jsonify


SECRET_KEY = "secret_key" 


USER_DATA = {
    "username": "admin",
    "password": "1234"
}

def generate_token(username):
   
    payload = {
        "username": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def login():
   
    data = request.json
    if not data or data.get("username") != USER_DATA["username"] or data.get("password") != USER_DATA["password"]:
        return jsonify({"error": "Invalid Credentials"}), 401
    
    token = generate_token(USER_DATA["username"])
    return {"token": token}, 200

def verify_token():
   
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        return None

    
    
    try:
        token = auth_header.split(" ")[1]
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return decoded_token  # Correção
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
    