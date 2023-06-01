from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app(app):
    """Link the database to current app"""
    db.init_app(app)
    app.db = db
    Migrate(app, db)
