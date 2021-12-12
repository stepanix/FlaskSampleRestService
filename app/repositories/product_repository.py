from app import db

class ProductRepository(object):         

    def insert(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def get(self, entity, id):
        result = db.session.query(entity).get(id)
        return result
    
    def update(self, entity, payload, id):
        product_to_update = db.session.query(entity).get(id)
        product_to_update.price = payload['price']
        product_to_update.title = payload['title']
        product_to_update.description = payload['description']    
        db.session.commit()
        return product_to_update
    
    