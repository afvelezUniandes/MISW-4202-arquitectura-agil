from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes import orders_bp
        app.register_blueprint(orders_bp)

    return app