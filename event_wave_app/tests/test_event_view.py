import unittest
from event_wave_app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_event_route(self):
        response = self.app.get('/events')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'List of events', response.data)
