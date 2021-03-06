from flask import request, jsonify, make_response
from app import app
from app.services.product_service import ProductService

@app.route("/product", methods=["POST"])
def post():
    payload = request.json
    service = ProductService()
    result = service.insert(payload)
    return make_response(jsonify(result))

@app.route("/product/<int:id>", methods=["GET"])
def get(id):
    service = ProductService()
    result = service.get(id)
    return make_response(jsonify(result))

@app.route("/product/<int:id>", methods=["PUT"])
def update(id):
    payload = request.json
    service = ProductService()    
    result = service.update(payload,id)
    return make_response(jsonify(result))


@app.route("/product/<int:id>", methods=["DELETE"])
def delete(id):
    service = ProductService()    
    result = service.delete(id)
    return make_response(jsonify(result))
    