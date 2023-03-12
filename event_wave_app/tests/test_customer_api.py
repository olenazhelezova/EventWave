import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_restful import Api
from event_wave_app import app
from event_wave_app.rest.customer import (
    SingleCustomerResource,
    MultipleCustomerResource,
)
from event_wave_app.tests.test_data import *
from event_wave_app.schemas.customer import CustomerSchema
from datetime import date
from event_wave_app.service.helpers import ServiceException


class TestSingleCustomerResource(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(SingleCustomerResource, "/customers/<int:customer_id>")
        self.client = self.app.test_client()

    @patch("event_wave_app.service.customer_service.CustomerService.get_customer")
    def test_get_customer_success(self, mock_get_customer):
        mock_customer = customer_1
        mock_get_customer.return_value = mock_customer
        response = self.client.get("/customers/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, CustomerSchema().dump(customer_1))

    @patch("event_wave_app.service.customer_service.CustomerService.get_customer")
    def test_get_customer_not_found(self, mock_get_customer):
        mock_get_customer.return_value = None
        response = self.client.get("/customers/1")
        self.assertEqual(response.status_code, 404)
        self.assertIn("message", response.json)

    @patch("event_wave_app.service.customer_service.CustomerService.update_customer")
    def test_update_customer_success(self, mock_update_customer):
        mock_customer = customer_3
        mock_update_customer.return_value = mock_customer
        response = self.client.put("/customers/3", json={"name": "John Doe"})
        self.assertEqual(response.status_code, 200)
        # customer_3.name = "John Doe"
        self.assertEqual(response.json, CustomerSchema().dump(customer_3))

    @patch("event_wave_app.service.customer_service.CustomerService.delete_customer")
    def test_delete_customer_success(self, mock_delete_customer):
        response = self.client.delete("/customers/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)

    def test_get_customer_error(self):
        with patch(
            "event_wave_app.service.customer_service.CustomerService.get_customer"
        ) as mock_get_customer:
            mock_get_customer.side_effect = Exception("Test exception")
            response = self.client.get("/customers/1")
            self.assertEqual(response.status_code, 500)
            self.assertIn("message", response.json)

    def test_get_customer_error_message(self):
        with patch(
            "event_wave_app.service.customer_service.CustomerService.get_customer"
        ) as mock_get_customer:
            mock_get_customer.side_effect = ServiceException("Test exception")
            response = self.client.get("/customers/1")
            self.assertEqual(response.status_code, 400)
            self.assertIn("message", response.json)

    def test_update_customer_error(self):
        with patch(
            "event_wave_app.service.customer_service.CustomerService.update_customer"
        ) as mock_update_customer:
            mock_update_customer.side_effect = Exception("Test exception")
            response = self.client.put("/customers/1", json={"name": "John Doe"})
            self.assertEqual(response.status_code, 500)
            self.assertIn("message", response.json)

    def test_update_customer_error_with_message(self):
        with patch(
            "event_wave_app.service.customer_service.CustomerService.update_customer"
        ) as mock_update_customer:
            mock_update_customer.side_effect = ServiceException("Test exception")
            response = self.client.put("/customers/1", json={"name": "John Doe"})
            self.assertEqual(response.status_code, 400)
            self.assertIn("message", response.json)

    def test_delete_customer_error(self):
        with patch(
            "event_wave_app.service.customer_service.CustomerService.delete_customer"
        ) as mock_delete_customer:
            mock_delete_customer.side_effect = Exception("Test exception")
            response = self.client.delete("/customers/1")
            self.assertEqual(response.status_code, 500)
            self.assertIn("message", response.json)

    def test_delete_customer_error_message(self):
        with patch(
            "event_wave_app.service.customer_service.CustomerService.delete_customer"
        ) as mock_delete_customer:
            mock_delete_customer.side_effect = ServiceException("Customer exists")
            response = self.client.delete("/customers/1")
            self.assertEqual(response.status_code, 400)
            self.assertIn("message", response.json)


class TestMultipleCustomerResource(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(MultipleCustomerResource, "/customers")
        self.client = self.app.test_client()

    @patch("event_wave_app.service.customer_service.CustomerService.get_customers")
    def test_get_customers_success(self, mock_get_customers):
        mock_customers = [customer_1, customer_2]
        mock_get_customers.return_value = mock_customers
        response = self.client.get("/customers")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json, CustomerSchema().dump(mock_customers, many=True)
        )

    @patch("event_wave_app.service.customer_service.CustomerService.get_customers")
    def test_get_customers_error_message(self, mock_get_customers):
        mock_get_customers.side_effect = ServiceException("bla blabl ")
        response = self.client.get("/customers")
        self.assertEqual(response.status_code, 400)
        self.assertIn("message", response.json)

    @patch("event_wave_app.service.customer_service.CustomerService.get_customers")
    def test_get_customers_error_general(self, mock_get_customers):
        mock_get_customers.side_effect = Exception("bla blabl ")
        response = self.client.get("/customers")
        self.assertEqual(response.status_code, 500)
        self.assertIn("message", response.json)

    @patch("event_wave_app.service.customer_service.CustomerService.add_customer")
    def test_add_customer_success(self, mock_add_customer):
        mock_customer = MagicMock()
        mock_add_customer.return_value = mock_customer
        response = self.client.post("/customers", json={"name": "John Doe"})
        self.assertEqual(response.status_code, 201)

    @patch("event_wave_app.service.customer_service.CustomerService.add_customer")
    def test_add_customer_error_general(self, mock_add_customer):
        mock_add_customer.side_effect = Exception("blablablabl")
        response = self.client.post("/customers", json={"name": "John Doe"})
        self.assertEqual(response.status_code, 500)
        self.assertIn("message", response.json)

    @patch("event_wave_app.service.customer_service.CustomerService.add_customer")
    def test_add_customer_error_message(self, mock_add_customer):
        mock_add_customer.side_effect = ServiceException("blablablabl")
        response = self.client.post("/customers", json={"name": "John Doe"})
        self.assertEqual(response.status_code, 400)
        self.assertIn("message", response.json)
