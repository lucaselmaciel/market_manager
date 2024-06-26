from typing import List, Optional
from app.models.product import Product, db


class ProductRepository:
    @staticmethod
    def get_all_products() -> List[Product]:
        return Product.query.all()

    @staticmethod
    def get_product_by_id(product_id) -> Product:
        return Product.query.get(product_id)

    @staticmethod
    def add_product(name, price, stock_quantity, description) -> Product:
        new_product = Product(
            name=name,
            price=price,
            stock_quantity=stock_quantity,
            description=description,
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def update_product(
        product_id, name=None, price=None, stock_quantity=None, description=None
    ) -> Optional[Product]:
        product = Product.query.get(product_id)
        if product:
            if name:
                product.name = name
            if price:
                product.price = price
            if stock_quantity is not None:
                product.stock_quantity = stock_quantity
            if description:
                product.description = description
            db.session.commit()
            return product
        return None

    @staticmethod
    def delete_product(product_id) -> bool:
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False
