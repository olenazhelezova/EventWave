import unittest
from event_wave_app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_orders_route(self):
        response = self.app.get('/orders')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ticket orders', response.data)
