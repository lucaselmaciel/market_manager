from typing import List
from app.repositories.product_repository import ProductRepository
from app.models.product import Product


class ProductService:
    @staticmethod
    def get_all_products() -> List[Product]:
        return ProductRepository.get_all_products()

    @staticmethod
    def get_product_by_id(product_id: int) -> Product:
        return ProductRepository.get_product_by_id(product_id)

    @staticmethod
    def create_product(
        name: str,
        price: float,
        stock_quantity: int,
        description: str = None,
        barcode: str = None,
    ) -> Product:
        new_product = ProductRepository.add_product(
            name, price, stock_quantity, description, barcode
        )
        return new_product

    @staticmethod
    def update_product(
        product_id: int,
        name: str = None,
        price: float = None,
        stock_quantity: int = None,
        description: str = None,
    ) -> Product:
        product = ProductRepository.get_product_by_id(product_id)
        if product:
            updated_product = ProductRepository.update_product(
                product_id, name, price, stock_quantity, description
            )
            return updated_product
        else:
            raise ValueError("Product not found.")

    @staticmethod
    def delete_product(product_id: int) -> bool:
        return ProductRepository.delete_product(product_id)
