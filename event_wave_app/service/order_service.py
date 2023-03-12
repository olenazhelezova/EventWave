"""
This module consists of the CRUD operations to work with `orders` table.
"""
import re
from typing import List

from event_wave_app import db
from event_wave_app.models import Order
from event_wave_app.service.customer_service import CustomerService
from event_wave_app.service.event_service import EventService
from .helpers import ServiceException, validate_date


class OrderService:
    """A class that provides CRUD operations for orders."""

    @staticmethod
    def get_orders(from_date=None, to_date=None) -> List[Order]:
        """
        Retrieve orders filtered by date range.

        :param from_date (optional): Start date in format 'YYYY-MM-DD'.
        :param to_date (optional): End date in format 'YYYY-MM-DD'.
        :returns: A list of Order objects that match the search criteria.
        :raises ServiceException: If either date is not in the correct format.
        """
        query = Order.query
        if from_date:
            validate_date(from_date)
            query = query.filter(Order.order_date >= from_date)
        if to_date:
            validate_date(to_date)
            query = query.filter(Order.order_date <= to_date)
        query = query.order_by(Order.order_date.asc())
        return query.all()

    @staticmethod
    def get_order(order_id) -> Order:
        """
        Retrieve a specific order by ID.

        :param id: The ID of the order to retrieve.
        :return: The Order object that matches the given ID, or None if no match is found.
        """
        return Order.query.filter_by(id=order_id).first()

    @staticmethod
    def add_order(data: dict) -> Order:
        """
        Add a new order to the database.

        :param data: A dictionary containing the data for the new order. Must include keys for
             "event_id", "price", "qty", "order_date", and "customer_id".
        :return: The Order object that was added to the database.
        :raises ServiceException: If any of the required fields are missing or in the wrong format,
             or if the associated event or customer does not exist.
        """
        OrderService.__validate_data(data)
        order = Order(
            data["event_id"],
            data["price"],
            data["qty"],
            data["order_date"],
            data["customer_id"],
        )
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def update_order(order_id, data: dict) -> Order:
        """
        Update an existing order in the database.

        :param id: The ID of the order to update.
        :param data: A dictionary containing the updated data for the order. Must include keys for
             "event_id", "price", "qty", "order_date", and "customer_id".
        :return: The Order object that was updated in the database.
        :raises ServiceException: If any of the required fields are missing or in the wrong format,
            if the order does not exist, or if the associated event or customer does not exist.
        """
        OrderService.__validate_data(data)
        order = Order.query.filter_by(id=order_id).first()
        if order is None:
            raise ServiceException("Order doesn't exist.")
        if str(order.event_id) != str(data["event_id"]):
            raise ServiceException("You can not change event.")
        order.price = data["price"]
        order.qty = data["qty"]
        order.order_date = data["order_date"]
        order.customer_id = data["customer_id"]
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def delete_order(order_id) -> None:
        """
        Deletes an order with the given ID.

        :param id: The ID of the order to delete.
        :raises ServiceException: If the order with the given ID doesn't exist.
        """
        order = Order.query.filter_by(id=order_id).first()
        if order:
            db.session.delete(order)
            db.session.commit()
        else:
            raise ServiceException("This order doesn't exist.")

    @staticmethod
    def __validate_data(data: dict) -> None:
        """
        Validates the data for creating or updating an order.

        :param data: A dictionary containing the data to validate.
        :raises ServiceException: If any of the required fields are missing or invalid.
        """
        if not all(
            key in data
            for key in ("event_id", "price", "qty", "order_date", "customer_id")
        ):
            raise ServiceException("Missing required fields.")
        if re.fullmatch(r"^\d+(\.\d{1,2})?$", str(data["price"])) is None:
            raise ServiceException("Invalid price format.")
        if re.fullmatch(r"^[0-9]*$", str(data["qty"])) is None:
            raise ServiceException("Invalid quantity.")
        validate_date(data["order_date"])
        event = EventService.get_event(event_id=data["event_id"])
        if event is None:
            raise ServiceException("Event doesn't exist.")
        if (event.availability - event.sold) < int(data["qty"]):
            raise ServiceException("Not enough tickets.")
        if CustomerService.get_customer(customer_id=data["customer_id"]) is None:
            raise ServiceException("Customer doesn't exist.")
