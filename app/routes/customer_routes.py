from flask import Blueprint, request, jsonify
from app.services.customer_service import CustomerService
from app.schemas import CustomerSchema

customer_bp = Blueprint("customer_bp", __name__)


@customer_bp.route("/customers", methods=["GET"])
def get_all_customers():
    customers = CustomerService.get_all_customers()
    return jsonify([customer.to_dict() for customer in customers]), 200


@customer_bp.route("/customer/<int:customer_id>", methods=["GET"])
def get_customer(customer_id: int):
    customer = CustomerService.get_customer_by_id(customer_id)
    if customer:
        return jsonify(customer.to_dict()), 200
    else:
        return jsonify({"error": "Customer not found"}), 404


@customer_bp.route("/customer", methods=["POST"])
def create_customer():
    data = request.json
    try:
        customer = CustomerService.create_customer(**data)
        return jsonify(customer.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@customer_bp.route("/customer/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id: int):
    data = request.json
    schema = CustomerSchema()
    try:
        customer = schema.load(data)
        persisted_customer = CustomerService.update_customer(customer_id, customer)
        if persisted_customer:
            return jsonify(customer.to_dict()), 200
        else:
            return jsonify({"error": "Customer not found"}), 404
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@customer_bp.route("/customer/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    success = CustomerService.delete_customer(customer_id)
    if success:
        return jsonify({"message": "Customer deleted"}), 200
    else:
        return jsonify({"error": "Customer not found"}), 404
