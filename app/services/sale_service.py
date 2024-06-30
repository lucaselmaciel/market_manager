from app.repositories.sale_repository import SaleRepository
from app.models.sale import Sale
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
        sale_details: Dict, total_amount: float, customer_id: int = None
    ) -> Sale:
        new_sale = SaleRepository.add_sale(sale_details, total_amount, customer_id)
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
