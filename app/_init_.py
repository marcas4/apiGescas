# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://gescas:oOu5gVJ746zOjOgaKmiAJDtOy2b955b2@dpg-cpjnge821fec73a109u0-a.oregon-postgres.render.com/products_kt0r'
db = SQLAlchemy(app)