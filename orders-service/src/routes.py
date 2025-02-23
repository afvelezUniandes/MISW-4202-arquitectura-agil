from flask import Blueprint, request, jsonify
from .models import Order, db

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
    orders = Order.query.all()
    return jsonify([{"id": order.id, "description": order.description, "status": order.status} for order in orders]), 200