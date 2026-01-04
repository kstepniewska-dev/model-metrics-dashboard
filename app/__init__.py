from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

#initialize the database
db = SQLAlchemy()

# Application factory
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.DevelopmentConfig')
    db.init_app(app)
    
    from app.routes.main import main
    from app.routes.auth import auth
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    
    return app

def init_db():
    """Initialize the database (create tables)."""
    with app.app_context():
        db.create_all()
        print("Database initialized successfully!")
