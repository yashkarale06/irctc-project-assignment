from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from flask_jwt_extended import JWTManager
from config import Config

# Initialize database and JWT manager
db = SQLAlchemy()
migrate = Migrate() 
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db) 

    from .routes import routes_bp
    app.register_blueprint(routes_bp)

    return app
