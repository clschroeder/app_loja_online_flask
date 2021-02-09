from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from application.models import db
from application.views import product_blueprint

def create_app(config_filename):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_filename)
    db.init_app(app)
    app.register_blueprint(product_blueprint)
    migrate = Migrate(app, db)
    return app


app = create_app('config')


