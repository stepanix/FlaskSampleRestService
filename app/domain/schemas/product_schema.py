
from flask_marshmallow import Marshmallow

import app
from app.domain.models.product_model import ProductModel


ma = Marshmallow(app)

class ProductSchema(ma.ModelSchema):
    class Meta:
        model = ProductModel
        fields = ('id', 'price', 'title', 'description') # fields to expose

product_schema = ProductSchema()
