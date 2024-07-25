from typing import List, Optional
from app.models.product import Product, db
from werkzeug.exceptions import NotFound


class ProductRepository:
    @staticmethod
    def get_all_products() -> List[Product]:
        return Product.query.all()

    @staticmethod
    def get_product_by_id(product_id) -> Product:
        product = Product.query.get(product_id)
        if not product:
            raise NotFound("Product not found")
        return product

    @staticmethod
    def add_product(name, price, stock_quantity, description, barcode) -> Product:
        new_product = Product(
            name=name,
            price=price,
            stock_quantity=stock_quantity,
            description=description,
            barcode=barcode
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def update_product(
        product: Product,
    ) -> Optional[Product]:
        db.session.merge(product)
        db.session.commit()
        return product

    @staticmethod
    def delete_product(product_id) -> bool:
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False
