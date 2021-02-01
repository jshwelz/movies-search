from apispec import APISpec
from config import Config
from db import SQLAlchemy
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask_sqlalchemy import SQLAlchemy

# Compute enviroment variables
config = Config

# Connect to database
db = SQLAlchemy()

# Define API spec
spec = APISpec(
	host=config.URL,
	plugins=[FlaskPlugin(), MarshmallowPlugin()],
	schemes='https',
	title=config.APP_NAME,
	openapi_version="3.0.2",
	version='1.0',
)

