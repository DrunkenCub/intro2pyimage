# third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import server
from jinja2 import Environment, PackageLoader
from sqlalchemy import create_engine

# Initialize the app from Flask
imageapp = Flask(__name__)
imageapp.config.from_object('settings')

imageapp.register_blueprint(server.bp, url_prefix='/server')

db = SQLAlchemy(imageapp)