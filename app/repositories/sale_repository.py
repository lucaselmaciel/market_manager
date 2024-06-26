from typing import List, Optional
from app.models.sale import Sale, db


class SaleRepository:
    @staticmethod
    def get_all_sales() -> List[Sale]:
        return Sale.query.all()

    @staticmethod
    def get_sale_by_id(sale_id: int) -> Optional[Sale]:
        return Sale.query.get(sale_id)

    @staticmethod
    def add_sale(total_amount: float, customer_id: Optional[int] = None) -> Sale:
        new_sale = Sale(total_amount=total_amount, customer_id=customer_id)
        db.session.add(new_sale)
        db.session.commit()
        return new_sale

    @staticmethod
    def update_sale(
        sale_id: int,
        total_amount: Optional[float] = None,
        customer_id: Optional[int] = None,
    ) -> Optional[Sale]:
        sale = Sale.query.get(sale_id)
        if sale:
            if total_amount is not None:
                sale.total_amount = total_amount
            if customer_id is not None:
                sale.customer_id = customer_id
            db.session.commit()
            return sale
        return None

    @staticmethod
    def delete_sale(sale_id: int) -> bool:
        sale = Sale.query.get(sale_id)
        if sale:
            db.session.delete(sale)
            db.session.commit()
            return True
        return False
