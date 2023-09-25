from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.app_context().push()

app.config['SECRET_KEY']='c0bfe4a2b6583bd23646694f26ebf8ae'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
from pythonblog import routes