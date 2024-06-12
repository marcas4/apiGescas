# app/schemas.py
from app import ma
from app.models import Productos, Pedidos, Mesa

class ProductoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'valor_unitario')

# Define esquemas similares para Pedidos y Mesa
