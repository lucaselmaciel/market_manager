from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(256))

    def __init__(self, name, price, stock_quantity, description=None):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.description = description

    def __repr__(self):
        return f'<Product {self.name}>'
