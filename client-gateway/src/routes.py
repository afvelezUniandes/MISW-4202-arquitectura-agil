import requests
import logging
from flask import Blueprint, request, jsonify
from .decorators import authenticate
from .auth import auth_bp

orders_bp = Blueprint('orders', __name__)

baseUrl = 'http://orders-service:5002'

@orders_bp.route('/orders', methods=['POST'])
@authenticate
def create_order():
    print("Permissions:" + request.permissions)
    if not request.permissions.get('can_create'):
        return jsonify({"error": "Forbidden"}), 403

    data = request.json
    response = requests.post(f'{baseUrl}/orders', json=data)
    return jsonify(response.json()), response.status_code

@orders_bp.route('/orders', methods=['GET'])
@authenticate
def get_orders():
    if not request.permissions.get('can_read') or request.rol != 'director de compras':
        return jsonify({"error": "Forbidden"}), 403
    response = requests.get(f'{baseUrl}/orders')
    return jsonify(response.json()), response.status_code

@orders_bp.route('/orders/<int:id>', methods=['PATCH'])
@authenticate
def update_order(id):
    if not request.permissions.get('can_update'):
        return jsonify({"error": "Forbidden"}), 403

    data = request.json
    response = requests.patch(f'{baseUrl}/orders/{id}', json=data)
    return jsonify(response.json()), response.status_code

@orders_bp.route('/orders/<int:id>', methods=['DELETE'])
@authenticate
def delete_order(id):
    if not request.permissions.get('can_delete'):
        return jsonify({"error": "Forbidden"}), 403

    response = requests.delete(f'{baseUrl}/orders/{id}')
    return jsonify(response.json()), response.status_code