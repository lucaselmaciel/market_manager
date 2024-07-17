from flask import Blueprint, request, jsonify
from app.services.sale_service import SaleService
from app.schemas import SaleSchema

sale_bp = Blueprint("sale_bp", __name__)


@sale_bp.route("/sales", methods=["GET"])
def get_all_sales():
    sales = SaleService.get_all_sales()
    return jsonify([sale.to_dict() for sale in sales]), 200


@sale_bp.route("/sale/<int:sale_id>", methods=["GET"])
def get_sale(sale_id):
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
def delete_sale(sale_id):
    success = SaleService.delete_sale(sale_id)
    if success:
        return jsonify({"message": "Sale deleted"}), 200
    else:
        return jsonify({"error": "Sale not found"}), 404
