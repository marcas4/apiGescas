# app/routes.py
from app import app, db
from flask import request, jsonify
from app.models import Productos, Pedidos, Mesa
from app.schemas import ProductoSchema  # Agrega esta línea

producto_schema = ProductoSchema()  # Define el esquema para productos

# Rutas para la API
@app.route('/productos', methods=['GET'])
def get_productos():
    productos = Productos.query.all()
    return jsonify(producto_schema.dump(productos))  # Usa producto_schema en lugar de productos_schema

@app.route('/productos', methods=['POST'])
def add_producto():
    nombre = request.json['nombre']
    valor_unitario = request.json['valor_unitario']
    nuevo_producto = Productos(nombre=nombre, valor_unitario=valor_unitario)
    db.session.add(nuevo_producto)
    db.session.commit()
    return producto_schema.jsonify(nuevo_producto)  # Usa producto_schema en lugar de productos_schema

# Agrega rutas similares para Pedidos y Mesa (GET, POST, PUT, DELETE)
