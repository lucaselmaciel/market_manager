from app import db


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=True)

    sales = db.relationship("Sale", backref="customer", lazy="dynamic")

    def __init__(self, name: str, contact: str, address: str, email: str = None):
        self.name = name
        self.contact = contact
        self.address = address
        self.email = email

    def __repr__(self) -> str:
        return f"<Customer {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "contact": self.contact,
            "address": self.address,
            "email": self.email or "",
        }
