from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    migrate = Migrate(app, db)
    dbURI = 'sqlite:///local.db'
    app.config["SQLALCHEMY_DATABASE_URI"] = dbURI

    db.init_app(app)
    with app.app_context():
        # Imports
        import application.routes

        # Create tables for our models
        db.create_all()
        return app

def create_test_app():
    """Construct the core application for test."""
    app = Flask(__name__)
    dbURI = 'sqlite:///test.db'
    app.config["SQLALCHEMY_DATABASE_URI"] = dbURI
    
    db.init_app(app)

    with app.app_context():
        # Imports

        # Create tables for our models
        db.create_all()

        return app

if __name__ == '__main__':
    create_app()