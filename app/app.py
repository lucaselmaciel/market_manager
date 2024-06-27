from flask import Flask
from app.config import Config
from app.routes import register_blueprints
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .routes.customer_routes import customer_bp
from .routes.product_routes import product_bp
from .routes.sale_routes import sale_bp

def register_blueprints(app):
    app.register_blueprint(customer_bp, url_prefix='/api')
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(sale_bp, url_prefix='/api')

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db = SQLAlchemy(app)
    db.init_app(app)
    migrate = Migrate(app, db)
    register_blueprints(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
