from flask import Flask
from flask_login import LoginManager
from .config import Config
from .db import db
from .routes import main as main_blueprint

login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)

    # Initialize Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'  # Redirect to login if not logged in

    # Register blueprints
    app.register_blueprint(main_blueprint)

    return app
