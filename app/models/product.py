from app import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(128), unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(256))

    def __init__(
        self,
        name: str,
        price: float,
        stock_quantity: int,
        barcode: str,
        id: int = None,
        description: str = None,
    ):
        self.id = id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.description = description
        self.barcode = barcode

    def __repr__(self):
        return f"<Product {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock_quantity": self.stock_quantity,
            "description": self.description or "",
            "barcode": self.barcode,
        }
