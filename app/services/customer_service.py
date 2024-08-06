from typing import List
from app.repositories.customer_repository import CustomerRepository
from app.models.customer import Customer
from werkzeug.exceptions import NotFound


class CustomerService:
    @staticmethod
    def get_all_customers() -> List[Customer]:
        return CustomerRepository.get_all_customers()

    @staticmethod
    def get_customer_by_id(customer_id: int) -> Customer:
        return CustomerRepository.get_customer_by_id(customer_id)

    @staticmethod
    def create_customer(
        name: str, contact: str, address: str, email: str = None
    ) -> Customer:
        if CustomerRepository.get_customer_by_email(email) is None:
            return CustomerRepository.add_customer(name, contact, address, email)
        else:
            raise ValueError("A customer with the given email already exists.")

    @staticmethod
    def update_customer(
        customer_id: int,
        customer: Customer
    ) -> Customer:
        customer = CustomerRepository.get_customer_by_id(customer_id)
        if customer:
            return CustomerRepository.update_customer(customer)
        else:
            raise NotFound("Customer not found.")

    @staticmethod
    def delete_customer(customer_id: int) -> bool:
        return CustomerRepository.delete_customer(customer_id)
