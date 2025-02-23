from flask import Flask
import logging

def create_app():
    app = Flask(__name__)
    logging.basicConfig(level=logging.INFO)
    with app.app_context():
        from .routes import control_bp
        app.register_blueprint(control_bp)

    return app