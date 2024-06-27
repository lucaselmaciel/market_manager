from datetime import datetime
from app import db


class Sale(db.Model):
    __tablename__ = 'sales'

    id = db.Column(db.Integer, primary_key=True)
    sale_data = db.Column(db.DateTime, nullable=False, default=datetime.now())
    total_amount = db.Column(db.Float, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=True)

    sale_details = db.relationship("SaleDetail", backref="sale", lazy="dynamic")

    def __init__(self, total_amount, customer_id=None):
        self.total_amount = total_amount
        self.customer_id = customer_id

    def __repr__(self) -> str:
        return f'<Sale {self.id} on {self.sale_date}>'


class SaleDetail(db.Model):
    __tablename__ = 'sale_details'

    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_at_sale = db.Column(db.Float, nullable=False)

    def __init__(self, sale_id, product_id, quantity, price_at_sale):
        self.sale_id = sale_id
        self.product_id = product_id
        self.quantity = quantity
        self.price_at_sale = price_at_sale

    def __repr__(self) -> str:
        return f'<SaleDetail {self.product_id} x {self.quantity}>'
