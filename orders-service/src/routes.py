from flask import Blueprint, request, jsonify
from .models import Order, db
import requests

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    new_order = Order(description=data['description'], status='pending')
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order created"}), 201

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    user_id = request.headers.get('User-ID')

    orders = Order.query.all()
    return jsonify([{"id": order.id, "description": order.description, "status": order.status} for order in orders]), 200

@orders_bp.route('/orders/<int:id>', methods=['PATCH'])
def update_order(id):
    data = request.json
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    order.description = data.get('description', order.description)
    order.status = data.get('status', order.status)
    db.session.commit()
    return jsonify({"message": "Order updated"}), 200

@orders_bp.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted"}), 200