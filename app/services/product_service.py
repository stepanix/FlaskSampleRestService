

from app.domain.models.product_model import ProductModel
from app.domain.schemas.product_schema import product_schema
from app.repositories.product_repository import ProductRepository


class ProductService(object):
    
    
    def insert(self, payload):        
        repository = ProductRepository()
        new_product = ProductModel(payload['price'], payload['title'], payload['description'])
        product_created = repository.insert(new_product)  
        result = product_schema.dump(product_created)
        return result
    
    def get(self, id):
        repository = ProductRepository()        
        product_retrieved = repository.get(ProductModel, id)
        result = product_schema.dump(product_retrieved)
        return result
    
    def update(self, payload, id):
        repository = ProductRepository()
        existing_product = repository.get(ProductModel, id) 
        payload_to_update = self.__build_valid_payload(payload, existing_product)
        
        product_updated = repository.update(ProductModel, payload_to_update, id)
        result = product_schema.dump(product_updated)
        return result
    
    def delete(self, id):
        repository = ProductRepository()
        result = repository.delete(ProductModel, id)
        return result
    
    def __build_valid_payload(self, payload, product):
        payload_to_update = {
                            "price": product.price,
                            "title": product.title,
                            "description": product.description
                          }
        
        if 'price' in payload:
            if payload['price'] != None and payload['price'] != "" and payload['price'] > 0:
                payload_to_update['price'] = payload['price']
            
                
        if 'description' in payload:    
            if payload['description'] != None and payload['description'] != "":
                payload_to_update['description'] = payload['description']
            
        
        if 'title' in payload:     
            if payload['title'] != None and payload['title'] != "":
                payload_to_update.title = payload['title']  
                
        return payload_to_update                
        
    