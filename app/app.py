from flask import Flask
from app.config import Config, DevelopmentConfig
from flask_migrate import Migrate
from app.routes.customer_routes import customer_bp
from app.routes.product_routes import product_bp
from app.routes.sale_routes import sale_bp
from app import db
import logging
logging.basicConfig(level=logging.DEBUG)


def register_blueprints(app):
    app.register_blueprint(customer_bp, url_prefix="/api")
    app.register_blueprint(product_bp, url_prefix="/api")
    app.register_blueprint(sale_bp, url_prefix="/api")


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate = Migrate(app, db)
    register_blueprints(app)

    return app


if __name__ == "__main__":
    app = create_app(DevelopmentConfig)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(debug=True)
