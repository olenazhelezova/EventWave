"""
This module defines Flask RESTful resources for handling Customer objects.

Includes two classes:
    - SingleCustomerResource: handles GET, PUT, and DELETE operations for a single Customer object.
    - MultipleCustomerResource: handles GET operation for multiple Customer objects
         and POST operation for creating new customer.
"""
# pylint:disable=duplicate-code
# pylint:disable=W0718
from flask_restful import Resource
from flask import request
from event_wave_app.schemas.customer import CustomerSchema
from event_wave_app.service.customer_service import CustomerService
from event_wave_app.service.helpers import ServiceException
from event_wave_app.rest.api_messages import (
    NOT_FOUND_ERROR_MESSAGE,
    APPLICATION_ERROR_MESSAGE,
    SUCCESS_DELETE_MESSAGE,
    to_message,
)


class SingleCustomerResource(Resource):
    """
    This resource defines the HTTP methods for retrieving, updating, and deleting a
    single customer by customer ID.
    """

    def get(self, customer_id):
        """
        Retrieve a single customer by ID.

        :param customer_id: The ID of the customer to retrieve.
        :return: A tuple containing the serialized customer data and a status code of 200 if
            the customer was found or message and a status code 404 if the customer was not found.
        :raises ServiceException: If an error occurred while retrieving
            the customer.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while
            retrieving the customer.
        """
        try:
            customer = CustomerService.get_customer(customer_id)
            if customer is None:
                return to_message(NOT_FOUND_ERROR_MESSAGE), 404
            return CustomerSchema().dump(customer), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

    def put(self, customer_id):
        """
        Update a single customer by ID.

        :param customer_id: The ID of the customer to update.
        :returns: A tuple containing the serialized customer data and a status code of 200 if
            the customer was updated successfully.
        :raises ServiceException: If an error occurred while updating the customer.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error
            while updating the customer.
        """
        try:
            customer = CustomerService.update_customer(customer_id, request.json)
            return CustomerSchema().dump(customer), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

    def delete(self, customer_id):
        """
        Delete a single customer by ID.

        :param customer_id: The ID of the customer to delete.
        :returns: A tuple containing a success message and a status code of 200 if the
            customer was deleted successfully.
        :raises ServiceException: If an error occurred while deleting the customer.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error
            while deleting the customer.
        """
        try:
            CustomerService.delete_customer(customer_id)
            return to_message(SUCCESS_DELETE_MESSAGE), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500


class MultipleCustomerResource(Resource):
    """
    This resource defines the HTTP methods for retrieving multiple
    customers or creating new customer.
    """

    def get(self):
        """
        Retrieve a list of customers.

        :return: A list of customers.
        :raises ServiceException: If an error occurred while retrieving the list of customers.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error
            while retrieving the list of customers.
        """
        try:
            customers = CustomerService.get_customers()
            return CustomerSchema().dump(customers, many=True), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

    def post(self):
        """
        Create a new customer.

        :return: The newly created customer.
        :raises ServiceException: If an error occurred while creating the new customer.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while
            creating the new customer.
        """
        try:
            customer = CustomerService.add_customer(request.json)
            return CustomerSchema().dump(customer), 201
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500
