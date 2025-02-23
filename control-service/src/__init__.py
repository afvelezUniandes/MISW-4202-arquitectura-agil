from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .routes import control_bp
        app.register_blueprint(control_bp)

    return app