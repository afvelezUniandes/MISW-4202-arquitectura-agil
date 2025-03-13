import logging
import requests
import jwt
from flask import request, jsonify
from functools import wraps

SECRET_KEY = 'your_secret_key' 

def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        logging.info(f"Auth header: {auth_header}")
        if not auth_header:
            return jsonify({"error": "Unauthorized"}), 401

        token = auth_header.split(" ")[1]
        logging.info(f"Token: {token}")
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            logging.info(f"Data: {data}")
        except jwt.ExpiredSignatureError:
            logging.error("Token expired")
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            logging.error("Invalid token")
            return jsonify({"error": "Invalid token"}), 401

        request.user_id = data['user_id']
        request.rol = data['rol']
        request.permissions = data['permissions']
        return f(*args, **kwargs)
    return wrapper