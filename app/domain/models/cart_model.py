from sqlalchemy import Column, Integer, Float,ForeignKey
from app import db

class CartModel(db.Model):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable = False)
    qty = Column(Integer, nullable = False)
    total = Column(Float, nullable = False)