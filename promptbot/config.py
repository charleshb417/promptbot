from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('PROMPTBOT_DB_URI') or 'sqlite:///../promptbot.db'
app.config['SECRET_KEY'] = os.environ.get('PROMPTBOT_SECRET_KEY') or 'keyyyy'
db = SQLAlchemy(app)