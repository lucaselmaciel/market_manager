from app.models.product import Product
from app.repositories.sale_repository import SaleRepository
from app.models.sale import Sale, SaleDetail
from typing import Dict, List


class SaleService:
    @staticmethod
    def get_all_sales() -> List[Sale]:
        return SaleRepository.get_all_sales()

    @staticmethod
    def get_sale_by_id(sale_id: int) -> Sale:
        return SaleRepository.get_sale_by_id(sale_id)

    @staticmethod
    def create_sale(
        sale: Sale,
    ) -> Sale:
        calculated_total = sum(detail.quantity * detail.price_at_sale for detail in sale.sale_details)

        if not round(calculated_total, 2) == round(sale.total_amount, 2):
            raise ValueError("The total_amount is different from the sum of each product value.")

        new_sale = Sale(total_amount=sale.total_amount, customer_id=sale.customer_id)
        for detail in sale.sale_details:
            product = Product.query.get(detail.product_id)
            if not product:
                raise ValueError(f"Product with the ID {detail.product_id} not found.")
            if detail.quantity > product.stock_quantity:
                raise ValueError(f"insufficient stock of {product.name}")
            new_detail = SaleDetail(
                product_id=detail.product_id,
                quantity=detail.quantity,
                price_at_sale=detail.price_at_sale
            )
            new_sale.sale_details.append(new_detail)
            product.stock_quantity -= detail.quantity

        SaleRepository.add_sale(new_sale)
        return new_sale

    @staticmethod
    def update_sale(
        sale_id: int, total_amount: float = None, customer_id: int = None
    ) -> Sale:
        sale = SaleRepository.get_sale_by_id(sale_id)
        if sale:
            updated_sale = SaleRepository.update_sale(
                sale_id, total_amount, customer_id
            )
            return updated_sale
        else:
            raise ValueError("Sale not found.")

    @staticmethod
    def delete_sale(sale_id: int) -> bool:
        return SaleRepository.delete_sale(sale_id)
