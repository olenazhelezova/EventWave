from unittest.mock import patch
from event_wave_app.service.customer_service import CustomerService
from event_wave_app.models.customer import Customer
from event_wave_app.tests.test_data import customer_1, customer_2, customer_3
from event_wave_app.service.helpers import ServiceException
from event_wave_app.tests.test_case_base import TestCaseBase


class TestCustomerService(TestCaseBase):
    @patch("event_wave_app.models.customer.Customer.query")
    def test_get_customers(self, query_mock):
        customers = [customer_1, customer_2, customer_3]
        query_mock.all.return_value = customers
        results = CustomerService.get_customers()
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), len(customers))

        for customer_result, customer_obj in zip(results, customers):
            self.assertIsInstance(customer_result, Customer)
            self.assertDictEqual(customer_result.to_dict(), customer_obj.to_dict())

    @patch("event_wave_app.models.customer.Customer.query")
    def test_get_customer(self, query_mock):
        customer = customer_1
        query_mock.filter_by.return_value.first.return_value = customer
        result = CustomerService.get_customer(customer.id)
        self.assertIsInstance(result, Customer)

    @patch("event_wave_app.db.session")
    @patch("event_wave_app.models.customer.Customer.query")
    def test_add_customer_success(self, query_mock, db_session_mock):
        query_mock.filter_by.return_value.first.return_value = None
        customer_data = customer_1.to_dict()
        result = CustomerService.add_customer(customer_data)
        db_session_mock.add.assert_called_once_with(result)
        db_session_mock.commit.assert_called_once()

    @patch("event_wave_app.models.customer.Customer.query")
    def test_add_customer_duplicate(self, query_mock):
        query_mock.filter_by.return_value.first.return_value = customer_1
        with self.assertRaises(ServiceException):
            CustomerService.add_customer(customer_1.to_dict())

    def test_add_customer_failed_validation(self):
        with self.assertRaises(ServiceException):
            CustomerService.add_customer({})
        with self.assertRaises(ServiceException):
            CustomerService.add_customer(
                {"name": "a", "phone_number": "123123123", "email": "hello"}
            )
        with self.assertRaises(ServiceException):
            CustomerService.add_customer(
                {
                    "name": "Alfred Pennyworth",
                    "phone_number": "123123123",
                    "email": "hello",
                }
            )
        with self.assertRaises(ServiceException):
            CustomerService.add_customer(
                {
                    "name": "Alfred Pennyworth",
                    "phone_number": "+12312312223",
                    "email": "@hello",
                }
            )

    @patch("event_wave_app.db.session")
    @patch("event_wave_app.models.customer.Customer.query")
    def test_update_customer_success(self, query_mock, db_session_mock):
        query_mock.filter_by.return_value.first.return_value = customer_1
        customer_data = customer_2.to_dict()
        result = CustomerService.update_customer(customer_1.id, customer_data)
        db_session_mock.add.assert_called_once_with(result)
        db_session_mock.commit.assert_called_once()
        self.assertIsInstance(result, Customer)

    @patch("event_wave_app.models.customer.Customer.query")
    def test_update_customer_failure(self, query_mock):
        query_mock.filter_by.return_value.first.return_value = None
        with self.assertRaises(ServiceException):
            CustomerService.update_customer(123, customer_1.to_dict())

    @patch("event_wave_app.db.session")
    @patch("event_wave_app.models.customer.Customer.query")
    def test_delete_customer_success(self, query_mock, db_session_mock):
        query_mock.filter_by.return_value.first.return_value = customer_1
        CustomerService.delete_customer(customer_1.id)
        db_session_mock.delete.assert_called_once_with(customer_1)
        db_session_mock.commit.assert_called_once()

    @patch("event_wave_app.models.customer.Customer.query")
    def test_delete_customer_failure(self, query_mock):
        query_mock.filter_by.return_value.first.return_value = None
        with self.assertRaises(ServiceException):
            CustomerService.delete_customer(666)
