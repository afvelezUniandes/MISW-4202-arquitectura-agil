from flask import Blueprint, request, jsonify
import requests

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    # Forward the request to the orders service
    response = requests.post('http://orders-service:5001/orders', json=data)
    return jsonify(response.json()), response.status_code

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    # Forward the request to the orders service
    response = requests.get('http://orders-service:5001/orders')
    return jsonify(response.json()), response.status_code