#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__version__ = '1.0.0'
__license__ = 'MIT'
__author__ = 'Josh Welchez'
__email__ = 'jshwelz09@gmail.com'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from globals import config, db
from commands import register_commands
from flask_cors import CORS
import routes


def init_app():
    app = Flask(__name__)
    CORS(app, resources={r"*": {"origins": "*"}})
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config['SECRET_KEY'] = config.SECRET
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_URL

    @app.route('/')
    def root_func():
        return 'Movies Api'

    db.init_app(app)
    routes.initialize_routes(app)
    register_commands(app)
    return app


app = init_app()

if __name__ == '__main__':
    app.run()
