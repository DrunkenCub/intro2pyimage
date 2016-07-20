import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['contact@chathuranga.com'])
SECRET_KEY = 'MY_LOVELY_KEY'

# Define the path of our database inside the root application, where 'app.db' is the database's name
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTION = {}