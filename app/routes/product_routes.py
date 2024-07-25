from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.schemas import ProductSchema
from werkzeug.exceptions import NotFound

product_bp = Blueprint("product_bp", __name__)


@product_bp.route("/products", methods=["GET"])
def get_all_products():
    products = ProductService.get_all_products()
    return jsonify([product.to_dict() for product in products]), 200


@product_bp.route("/product/<int:product_id>", methods=["GET"])
def get_product(product_id: int):
    product = ProductService.get_product_by_id(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    else:
        return jsonify({"error": "Product not found"}), 404


@product_bp.route("/product", methods=["POST"])
def create_product():
    data = request.json
    try:
        product = ProductService.create_product(**data)
        return jsonify(product.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@product_bp.route("/product/<int:product_id>", methods=["PUT"])
def update_product(product_id: int):
    data = request.json
    data["id"] = product_id
    schema = ProductSchema()
    try:
        product = schema.load(data)
        product = ProductService.update_product(product_id, product)
        return jsonify(product.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except NotFound as e:
        return jsonify({"error": str(e)}), 404


@product_bp.route("/product/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    success = ProductService.delete_product(product_id)
    if success:
        return jsonify({"message": "Product deleted"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404
