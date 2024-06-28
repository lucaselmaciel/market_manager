from app import db


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

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'stock_quantity': self.stock_quantity,
            'description': self.description or ""
        }