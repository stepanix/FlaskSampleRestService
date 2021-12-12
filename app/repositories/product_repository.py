from app import db

class ProductRepository(object):    
   

    def insert(self, model):
        db.session.add(model)
        db.session.commit()
        return model
    
    def get(self, model, id):
        result = db.session.query(model).get(id)
        return result
    
    def update(self, model, payload, id):
        product_to_update = db.session.query(model).get(id)
        product_to_update.price = payload['price']
        product_to_update.title = payload['title']
        product_to_update.description = payload['description']    
        db.session.commit()
        return product_to_update
    
    def delete(self, model, id):
        product_to_delete = db.session.query(model).get(id)
        db.session.delete(product_to_delete)
        return "delete successful"
    
    