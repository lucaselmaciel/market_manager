from typing import Dict, List, Optional
from app.models.sale import Sale, SaleDetail, db


class SaleRepository:
    @staticmethod
    def get_all_sales() -> List[Sale]:
        return Sale.query.all()

    @staticmethod
    def get_sale_by_id(sale_id: int) -> Optional[Sale]:
        return Sale.query.get(sale_id)

    @staticmethod
    def add_sale(
        sale_details: Dict, total_amount: float, customer_id: Optional[int] = None
    ) -> Sale:
        sale_details_instances = []
        for detail in sale_details:
            new_detail = SaleDetail(
                product_id=detail["product_id"],
                quantity=detail["quantity"],
                price_at_sale=detail["price_at_sale"],
            )
            sale_details_instances.append(new_detail)
        new_sale = Sale(
            total_amount=total_amount,
            customer_id=customer_id,
            sale_details=sale_details_instances,
        )
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
