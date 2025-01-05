"""
The flask application package.
"""
import os
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config.from_object(Config)
#app.secret_key = os.getenv('SECRET_KEY', '')
app.secret_key=os.getenv("CLIENT_SECRET")
#app.secret_key = b'\xa2\xd3\xfb\xe5\x13\x18\xccA\xd5k\xd7\xb0\xfcH\xe3\xb9\xa0A\xdc#~\x9f\xe5'

csrf = CSRFProtect(app)
# TODO: Add any logging levels and handlers with app.logger
streamHandler=logging.StreamHandler()
streamHandler.setLevel(logging.WARNING)
app.logger.setLevel(logging.WARNING)
app.logger.addHandler(streamHandler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'


import FlaskWebProject.views
