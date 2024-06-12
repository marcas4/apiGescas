# app/models.py
from app import db

class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    valor_unitario = db.Column(db.Integer, nullable=False)

class Pedidos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_productos = db.Column(db.Integer, nullable=False)
    id_mesa = db.Column(db.Integer, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    valor_pedido = db.Column(db.Integer, nullable=False)

class Mesa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_pedidos = db.Column(db.Integer, nullable=False)
    num_mesa = db.Column(db.Integer, nullable=False)