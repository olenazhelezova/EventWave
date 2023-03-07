"""
This module consists of the CRUD operations to work with `customers` table.
"""
import re
from typing import List
from event_wave_app import db
from event_wave_app.models.customer import Customer
from .helpers import ServiceException


class CustomerService:
    """A class that provides CRUD operations for customers."""
    @staticmethod
    def get_customers() -> List[Customer]:
        """       
        Retrieve a list of customers.

        :return: List of Customer objects.
        """
        return Customer.query.all()

    @staticmethod
    def get_customer(customer_id) -> Customer:
        """
        Retrieve a customer by ID.

        :param id: Customer ID.
        :return: The Customer object matching the ID, or None if no match is found.
        """
        return Customer.query.filter_by(id=customer_id).first()

    @staticmethod
    def add_customer(data: dict) -> Customer:
        """
        Adds a new customer to the database.

        :param data: A dictionary containing the customer's name, phone number, and email.
        :return: The newly created Customer object.
        """
        CustomerService.__validate_data(data)
        customer_exists = (
            Customer.query.filter_by(email=data["email"]).first() is not None
        )
        if customer_exists:
            raise ServiceException("Customer with same email already exists!")
        customer = Customer(data["name"], data["phone_number"], data["email"])
        db.session.add(customer)
        db.session.commit()
        return customer

    @staticmethod
    def update_customer(customer_id, data: dict) -> Customer:
        """
        Updates a customer with the given id in the database.

        :param id: The id of the customer to update.
        :param data: A dictionary containing the updated customer data.
        :return: The updated Customer object.
        """
        CustomerService.__validate_data(data)
        customer = Customer.query.filter_by(id=customer_id).first()
        if customer is None:
            raise ServiceException("Customer doesn't exist.")
        customer.name = data["name"]
        customer.phone_number = data["phone_number"]
        customer.email = data["email"]
        db.session.add(customer)
        db.session.commit()
        return customer

    @staticmethod
    def delete_customer(customer_id) -> None:
        """
        Deletes a customer with the given id from the database.

        :param id: The id of the customer to delete.
        :raises ServiceException: If the customer doesn't exist.
        """
        customer = Customer.query.filter_by(id=customer_id).first()
        if customer:
            db.session.delete(customer)
            db.session.commit()
        else:
            raise ServiceException("This customer doesn't exist.")

    @staticmethod
    def __validate_data(data: dict) -> None:
        """
        Validates the customer data.

        :param data: A dictionary containing the customer's name, phone number, and email.
        :raises ServiceException: If the data is invalid.
        """
        if not all(key in data for key in ("name", "phone_number", "email")):
            raise ServiceException("Missing required fields.")
        if not 3 <= len(data["name"]) <= 50:
            raise ServiceException("Invalid name.")
        if re.fullmatch(r"^\+\d{10,12}$", data["phone_number"]) is None:
            raise ServiceException("Invalid phone number.")
        if re.fullmatch(
            r"^[\w\.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", data["email"]
        ) is None or not 6 <= len(data["email"]) <= 50:
            raise ServiceException("Invalid e-mail adress.")
