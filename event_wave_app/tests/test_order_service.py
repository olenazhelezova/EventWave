from unittest.mock import patch
from event_wave_app.service.order_service import OrderService
from event_wave_app.models.order import Order
from event_wave_app.service.helpers import ServiceException
from event_wave_app.tests.test_case_base import TestCaseBase
from event_wave_app.tests.test_data import order_1, order_2, order_3, event_1, order_1_upd, order_with_ref, customer_1

class TestOrderService(TestCaseBase):
    @patch("event_wave_app.models.order.Order.query")
    def test_get_orders(self, query_mock):
        orders = [order_1, order_2, order_3]
        query_mock.order_by.return_value.all.return_value = orders
        results = OrderService.get_orders()
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), len(orders))
        for order_result, order_obj in zip(results, orders):
            self.assertIsInstance(order_result, Order)
            self.assertDictEqual(order_result.to_dict(), order_obj.to_dict())

    @patch("event_wave_app.models.order.Order.query")
    def test_get_orders_filtering_by_date(self, query_mock):
        orders = [order_1, order_2, order_3]
        query_mock.filter.return_value.filter.return_value.order_by.return_value.all.return_value = orders
        results = OrderService.get_orders("2020-02-02", "2022-02-02")
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), len(orders))
        for order_result, order_obj in zip(results, orders):
            self.assertIsInstance(order_result, Order)
            self.assertDictEqual(order_result.to_dict(), order_obj.to_dict())

    @patch("event_wave_app.models.order.Order.query")
    def test_get_order(self, query_mock):
        order = order_1
        query_mock.filter_by.return_value.first.return_value = order
        result = OrderService.get_order(order.id)
        self.assertIsInstance(result, Order)

    @patch("event_wave_app.db.session")
    @patch("event_wave_app.models.order.Order.query")
    def test_add_order_success(self, query_mock, db_session_mock):
        query_mock.filter_by.return_value.first.return_value = None
        order_data = order_1.to_dict()
        result = OrderService.add_order(order_data)
        db_session_mock.add.assert_called_once_with(result)
        db_session_mock.commit.assert_called_once()

    @patch("event_wave_app.service.customer_service.CustomerService.get_customer")
    def test_add_order_failed_validation(self, missing_customer_mock):
        missing_customer_mock.return_value = None
        with self.assertRaises(ServiceException):
            OrderService.add_order({})
        with self.assertRaises(ServiceException):
            OrderService.add_order(
                {
                    "event_id": 3,
                    "price": -200.00,
                    "qty": 2,
                    "order_date": "2023-02-05",
                    "customer_id": 12,
                }
            )
        with self.assertRaises(ServiceException):
            OrderService.add_order(
                {
                    "event_id": 3,
                    "price": 200.00,
                    "qty": -3,
                    "order_date": "2023-02-05",
                    "customer_id": 12,
                }
            )
        with self.assertRaises(ServiceException):
            OrderService.add_order(
                {
                    "event_id": None,
                    "price": 200.00,
                    "qty": 2,
                    "order_date": "2023",
                    "customer_id": 12,
                }
            )
        with patch(
            "event_wave_app.service.event_service.EventService.get_event"
        ) as missing_event_mock:
            missing_event_mock.return_value = None
            with self.assertRaises(ServiceException):
                OrderService.add_order(
                    {
                        "event_id": None,
                        "price": 200.00,
                        "qty": 2,
                        "order_date": "2023-02-05",
                        "customer_id": "666",
                    }
                )
        with patch(
            "event_wave_app.service.event_service.EventService.get_event"
        ) as existing_event_mock:
            existing_event_mock.return_value = event_1
            with self.assertRaises(ServiceException):
                OrderService.add_order(
                    {
                        "event_id": event_1.id,
                        "price": 200.00,
                        "qty": 2,
                        "order_date": "2023-02-05",
                        "customer_id": "666",
                    }
                )

    @patch("event_wave_app.db.session")
    @patch("event_wave_app.models.order.Order.query")
    def test_update_order_success(self, query_mock, db_session_mock):
        query_mock.filter_by.return_value.first.return_value = order_1
        order_data = order_1_upd.to_dict()
        result = OrderService.update_order(event_1.id, order_data)
        db_session_mock.add.assert_called_once_with(result)
        db_session_mock.commit.assert_called_once()
        self.assertIsInstance(result, Order)

    @patch("event_wave_app.models.order.Order.query")
    @patch("event_wave_app.service.customer_service.CustomerService.get_customer")
    @patch("event_wave_app.service.event_service.EventService.get_event")
    def test_update_order_non_existing_order(
        self, event_query_mock, customer_query_mock, order_query_mock
    ):
        order_query_mock.filter_by.return_value.first.return_value = None
        event_query_mock.return_value = event_1
        customer_query_mock.return_value = customer_1
        with self.assertRaises(ServiceException):
            OrderService.update_order(123, order_1.to_dict())

    @patch("event_wave_app.models.order.Order.query")
    @patch("event_wave_app.service.customer_service.CustomerService.get_customer")
    @patch("event_wave_app.service.event_service.EventService.get_event")
    def test_update_order_change_event_forbidden(
        self, event_query_mock, customer_query_mock, order_query_mock):
        order_query_mock.filter_by.return_value.first.return_value = order_with_ref
        event_query_mock.return_value = event_1
        customer_query_mock.return_value = customer_1
        with self.assertRaises(ServiceException):
            OrderService.update_order(555, order_2.to_dict())

    @patch("event_wave_app.db.session")
    @patch("event_wave_app.models.order.Order.query")
    def test_delete_order_success(self, query_mock, db_session_mock):
        query_mock.filter_by.return_value.first.return_value = order_1
        OrderService.delete_order(order_1.id)
        db_session_mock.delete.assert_called_once_with(order_1)
        db_session_mock.commit.assert_called_once()

    @patch("event_wave_app.models.order.Order.query")
    def test_delete_order_failure(self, query_mock):
        query_mock.filter_by.return_value.first.return_value = None
        with self.assertRaises(ServiceException):
            OrderService.delete_order(666)
