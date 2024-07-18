from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.services.sale_service import SaleService
from app.schemas import SaleSchema, SalesListFiltersSchema

sale_bp = Blueprint("sale_bp", __name__)


@sale_bp.route("/sales", methods=["POST"])
def get_all_sales():
    try:
        filters_schema = SalesListFiltersSchema()
        filters = filters_schema.load(request.json)
        sales = SaleService.get_sales(filters)
    except ValidationError as e:
        return jsonify(e.messages), 422

    return jsonify([sale.to_dict() for sale in sales]), 200


@sale_bp.route("/sale/<int:sale_id>", methods=["GET"])
def get_sale(sale_id: int):
    sale = SaleService.get_sale_by_id(sale_id)
    if sale:
        return jsonify(sale.to_dict()), 200
    else:
        return jsonify({"error": "Sale not found"}), 404


@sale_bp.route("/sale", methods=["POST"])
def create_sale():
    data = request.json
    try:
        schema = SaleSchema()
        sale = schema.load(data)
        sale = SaleService.create_sale(sale)
        return jsonify(sale.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@sale_bp.route("/sale/<int:sale_id>", methods=["DELETE"])
def delete_sale(sale_id: int):
    success = SaleService.delete_sale(sale_id)
    if success:
        return jsonify({"message": "Sale deleted"}), 200
    else:
        return jsonify({"error": "Sale not found"}), 404
