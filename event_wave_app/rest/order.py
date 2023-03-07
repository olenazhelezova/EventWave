"""
This module defines Flask RESTful resources for handling Order objects.

Includes two classes:
    - SingleCustomerResource: handles GET, PUT, and DELETE operations for a single Order object.
    - MultipleCustomerResource: handles GET operation for multiple Order objects
        and POST operation for creating new order.
"""
# pylint:disable=W0718
from flask_restful import Resource
from flask import request
from event_wave_app.schemas.order import OrderSchema
from event_wave_app.service.order_service import OrderService
from event_wave_app.service.helpers import ServiceException
from event_wave_app.rest.api_messages import (
    NOT_FOUND_ERROR_MESSAGE,
    APPLICATION_ERROR_MESSAGE,
    SUCCESS_DELETE_MESSAGE,
    to_message)

class SingleOrderResource(Resource):
    """
    Resource for managing a single order, identified by its ID.
    """
    def get(self, order_id):
        """
        Retrieve a single order by ID.

        :param event_id: The ID of the order to retrieve.
        :return: The requested order, serialized as JSON, with an HTTP status code of 200 or
             message and a status code 404 if the order was not found.
        :raises ServiceException: If an error occurred while retrieving the order.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while
            retrieving the order.
        """
        try:
            order = OrderService.get_order(order_id)
            if order is None:
                return to_message(NOT_FOUND_ERROR_MESSAGE), 404
            return OrderSchema().dump(order), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

    def put(self, order_id):
        """
        Update a single order by ID.

        :param event_id: The ID of the order to update.
        :return: The updated order, serialized as JSON, with an HTTP status code of 200.
        :raises ServiceException: If an error occurred while updating the order.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while updating the order.
        """
        try:
            order = OrderService.update_order(order_id, request.json)
            return OrderSchema().dump(order), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

    def delete(self, order_id):
        """
        Delete a single order by ID.

        :param event_id: The ID of the order to delete.
        :return: A success message, with an HTTP status code of 200.
        :raises ServiceException: If an error occurred while deleting the order.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while deleting the order.
        """
        try:
            OrderService.delete_order(order_id)
            return to_message(SUCCESS_DELETE_MESSAGE), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

class MultipleOrderResource(Resource):
    """
    This resource defines the HTTP methods for retrieving multiple
    orders or creating new order.
    """
    def get(self, from_date = None, to_date = None):
        """
        Retrieve a list of events.

        :param from_date (optional): A string representing the earliest date for orders to include.
        :param to_date (optional): A string representing the latest date for orders to include.
        :return: A list of orders, serialized as JSON, with an HTTP status code of 200.
        :raises ServiceException: If an error occurred while retrieving the list of orders.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while retrieving
            the list of orders.
        """
        try:
            from_date = request.args.get('from_date')
            to_date = request.args.get('to_date')
            if from_date or to_date:
                orders = OrderService.get_orders(from_date=from_date, to_date=to_date)
            else:
                orders = OrderService.get_orders()
            return OrderSchema().dump(orders, many=True), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

    def post(self):
        """
        Create a new order.

        :return: The newly created order.
        :raises ServiceException: If an error occurred while creating the new order.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while
            creating the new order.
        """
        try:
            order = OrderService.add_order(request.json)
            return OrderSchema().dump(order), 201
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500
