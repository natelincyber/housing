# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_caching import Cache
from flask_bootstrap import Bootstrap
from .config import Config

from dotenv import load_dotenv

load_dotenv()

# Initialize extensions without binding to the app yet
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'main.login'  # Endpoint for login
cache = Cache()
bootstrap = Bootstrap()

def create_app(config_class=Config):
    """
    Application factory function.
    
    Args:
        config_class (class): Configuration class to use.
        
    Returns:
        Flask app instance
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    cache.init_app(app)
    bootstrap.init_app(app)

    # Register blueprints
    from app.views.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.views.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # Register additional blueprints if necessary
    # from app.views.auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # Error handlers
    from app.errors import errors as errors_blueprint
    app.register_blueprint(errors_blueprint)

    from app.models import User

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
