import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    db.init_app(app)

    logging.basicConfig(level=logging.INFO)
    
    with app.app_context():
        from .routes import auth_bp
        app.register_blueprint(auth_bp)

        # Crear tablas si no existen
        db.create_all()

    return app