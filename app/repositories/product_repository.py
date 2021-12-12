from app import db

class ProductRepository(object):
   
        

    def insert(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def get(self, entity, id):
        result = db.session.query(entity).get(id)
        return result
    
    