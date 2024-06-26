from flask import Flask
from config import Config
from app.models import db
from app.routes import register_blueprints
from flask_migrate import Migrate

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa o banco de dados com o Flask
    db.init_app(app)
    migrate = Migrate(app, db)

    # Registra os blueprints
    register_blueprints(app)

    # Configurações adicionais podem ser adicionadas aqui, como loggers, ferramentas de monitoramento, etc.

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)  # Lembre-se de desativar o modo debug em produção
