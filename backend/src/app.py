import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from src.config.manager import setup_config
from src.config.modules.logger import setup_logger

API = Api()
DB = SQLAlchemy()


def register_blueprints(app, url_prefix):
    """
    Register all the blueprints
    :param app: Flask Object
    :param url_prefix: Prefix for all the backend url.
    :return: None
    """
    from src.resources.todo.controller.todo import TODO_API
    app.register_blueprint(TODO_API, url_prefix=url_prefix)
    pass


def create_app():
    """
    Main entry point for the flask app.
    :return: Flask Object
    """
    app = Flask(__name__)
    API.init_app(app)
    setup_config(app)
    # setup_logger(app)
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'hide_parameters': True, 'convert_unicode': False}
    DB.init_app(app)
    register_blueprints(app, os.getenv('ROUTE_PREFIX'))
    return app

