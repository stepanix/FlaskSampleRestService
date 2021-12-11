
from app.domain.models.product import ProductModel
from app.domain.schemas.product_schema import product_schema
from app.repositories.product_repository import ProductRepository


class ProductService(object):
    
    
    def insert(self, payload):
        repository = ProductRepository()
        new_product = ProductModel(payload['price'], payload['title'], payload['description'])
        product_created = repository.insert(new_product)  
        result = product_schema.dump(product_created)
        return result
    
    