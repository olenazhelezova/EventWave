import unittest
from event_wave_app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @unittest.mock.patch(
        "event_wave_app.service.customer_service.CustomerService.get_customers"
    )
    def test_orders_route(self, get_customers_mock):
        get_customers_mock.return_value = []
        response = self.app.get("/orders")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Ticket orders", response.data)
