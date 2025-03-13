import logging
from flask import Blueprint, request, jsonify
from .models import User, Permission, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth', methods=['POST'])
def authenticate():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({
            "authenticated": True, 
            "user_id": user.id, 
            "rol": user.rol
        }), 200
    return jsonify({"authenticated": False}), 401

@auth_bp.route('/permissions/<int:user_id>', methods=['GET'])
def get_permissions(user_id):
    user = User.query.get(user_id)
    if user:
        permission = Permission.query.filter_by(user_id=user_id).first()
        if permission:
            return jsonify({
                "can_create": permission.can_create,
                "can_read": permission.can_read,
                "can_update": permission.can_update,
                "can_delete": permission.can_delete
            }), 200
    return jsonify({"error": "User or permissions not found"}), 404