from typing import List, Optional
from app.models.customer import Customer, db


class CustomerRepository:
    @staticmethod
    def get_all_customers() -> List[Customer]:
        return Customer.query.all()

    @staticmethod
    def get_customer_by_id(customer_id: int) -> Optional[Customer]:
        return Customer.query.get(customer_id)

    @staticmethod
    def add_customer(
        name: str, contact: str, address: str, email: Optional[str] = None
    ) -> Customer:
        new_customer = Customer(
            name=name, contact=contact, address=address, email=email
        )
        db.session.add(new_customer)
        db.session.commit()
        return new_customer

    @staticmethod
    def update_customer(customer: Customer) -> Optional[Customer]:
        db.session.merge(customer)
        db.session.commit()
        return customer

    @staticmethod
    def delete_customer(customer_id: int) -> bool:
        customer = Customer.query.get(customer_id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_customer_by_email(email: str) -> Optional[Customer]:
        customer = Customer.query.filter(Customer.email == email).one_or_none()
        return customer
