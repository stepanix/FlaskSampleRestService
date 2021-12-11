from flask import request, jsonify, make_response
from app import app
from app.services.product_service import ProductService

@app.route("/product", methods=["POST"])
def post():
    payload = request.json
    service = ProductService()
    result = service.insert(payload)
    return make_response(jsonify(result))
    