"""
Entry point of app
"""

# flask packages
from flask import Flask, app
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# local packages
from api.routes import create_routes

# external packages
import os

# default mongodb configuration
default_config = {
    'MONGODB_SETTINGS': {
        # 'host': 'mongodb://fabri:7WibFkS6LTwu@ds133077.mlab.com:33077/fabrisongs?authSource=fabrisongs&readPreference=primary&retryWrites=false',
        'db': 'pymongo',
        'host': 'localhost',
        'port': 27017,
        'username': 'admin',
        'password': 'password',
        'authentication_source': 'admin'
    },
    'JWT_SECRET_KEY': 'changeMe'
}


def get_flask_app(config: dict = None) -> app.Flask:
    """
    Initializes Flask app with given configuration.
    Main entry point for wsgi (gunicorn) server.
    :param config: Configuration dictionary
    :return: app
    """
    # init flask
    flask_app = Flask(__name__)
    CORS(flask_app)

    # configure app
    config = default_config if config is None else config
    flask_app.config.update(config)

    # load config variables
    if 'MONGODB_URI' in os.environ:
        flask_app.config['MONGODB_SETTINGS'] = {'host': os.environ['MONGODB_URI'],
                                                'retryWrites': False}
    if 'JWT_SECRET_KEY' in os.environ:
        flask_app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']

    # init api and routes
    api = Api(app=flask_app)
    create_routes(api=api)

    # init mongoengine
    db = MongoEngine(app=flask_app)

    # init jwt manager
    jwt = JWTManager(app=flask_app)

    return flask_app


if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app = get_flask_app()
    app.run(debug=True)
