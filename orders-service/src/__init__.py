import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .tasks import celery

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('src.config.Config')

    db.init_app(app)

    logging.basicConfig(level=logging.INFO)
    
    with app.app_context():
        from .routes import orders_bp
        app.register_blueprint(orders_bp)

        # Crear tablas si no existen
        db.create_all()

    return app