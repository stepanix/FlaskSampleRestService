from sqlalchemy import Column, Integer, String, Float
from app import db

class ProductModel(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable = False)
    title = Column(String(50), nullable = False)
    description = Column(String(100), nullable = False)    
    
    
    def __init__(self, price, title, description):
        self.price = price
        self.title = title
        self.description = description