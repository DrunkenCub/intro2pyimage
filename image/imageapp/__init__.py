# third party imports
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# Initialize the app from Flask
imageapp = Flask(__name__)
imageapp.config.from_object('settings')

db = SQLAlchemy(imageapp)