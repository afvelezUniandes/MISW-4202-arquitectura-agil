from flask import Blueprint, request

control_bp = Blueprint('control', __name__)

@control_bp.route('/status', methods=['POST'])
def receive_status():
    data = request.json
    print(f"Received status from orders service: {data}")
    return {"message": "Status received"}, 200