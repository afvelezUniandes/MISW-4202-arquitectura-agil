from flask import Blueprint, request, jsonify
import requests

orders_bp = Blueprint('orders', __name__)

baseUrl = 'http://orders-service:5002'


@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    response = requests.post(f'{baseUrl}/orders', json=data)
    return jsonify(response.json()), response.status_code

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    response = requests.get(f'{baseUrl}/orders')
    return jsonify(response.json()), response.status_code