import logging
import datetime
import requests
from flask import request, jsonify, Blueprint
import jwt


AUTH_SERVICE_URL = 'http://auth-service:5001/auth'
PERMISSIONS_SERVICE_URL = 'http://auth-service:5001/permissions'
SECRET_KEY = 'your_secret_key'

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['POST'])
def login():
    data = request.json
    auth_response = requests.post(AUTH_SERVICE_URL, json={"username": data['username'], "password": data['password']})
    logging.info(f"Auth response: {auth_response}")
    if auth_response.status_code != 200:
        return jsonify({"error": "Unauthorized"}), 401

    user_id = auth_response.json().get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    # Obtener permisos del usuario
    permissions_response = requests.get(f"{PERMISSIONS_SERVICE_URL}/{user_id}")
    if permissions_response.status_code != 200:
        return jsonify({"error": "Unauthorized"}), 401

    rol = auth_response.json().get('rol')

    permissions = permissions_response.json()

    # Generar JWT
    token = jwt.encode({
        'user_id': user_id,
        'rol': rol,
        'permissions': permissions,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
    }, SECRET_KEY, algorithm='HS256')

    return jsonify({"token": token}), 200