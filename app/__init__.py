from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#initialize the database
db = SQLAlchemy()

# Application factory
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    db.init_app(app)
    
    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.uploads import uploads
    
    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(uploads)
    
    return app
