from typing import Dict, List, Optional
from app.models.sale import Sale, SaleDetail, db


class SaleRepository:
    @staticmethod
    def get_all_sales() -> List[Sale]:
        return Sale.query.all()

    @staticmethod
    def get_sale_by_id(sale_id: int) -> Optional[Sale]:
        sale = Sale.query.get(sale_id)
        if sale:
            return sale
        else:
            raise ValueError("Sale not found")

    @staticmethod
    def add_sale(
        new_sale: Sale,
    ) -> Sale:
        db.session.add(new_sale)
        db.session.commit()
        return new_sale

    @staticmethod
    def delete_sale(sale_id: int) -> bool:
        sale = Sale.query.get(sale_id)
        if sale:
            db.session.delete(sale)
            db.session.commit()
            return True
        return False
