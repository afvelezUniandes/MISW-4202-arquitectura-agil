import logging
from flask import Flask

def create_app():
    app = Flask(__name__)

    logging.basicConfig(level=logging.INFO)
    
    with app.app_context():
        from .routes import orders_bp
        from .auth import auth_bp
        
        app.register_blueprint(orders_bp)
        app.register_blueprint(auth_bp, url_prefix='/')

    return app