import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from flask_restful import Api
from event_wave_app import app
from event_wave_app.rest.event import (
    SingleEventResource,
    MultipleEventResource,
)
from event_wave_app.tests.test_data import *
from event_wave_app.schemas.event import EventSchema
from datetime import date, time
from event_wave_app.service.helpers import ServiceException


class TestSingleCustomerResource(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(SingleEventResource, "/events/<int:event_id>")
        self.client = self.app.test_client()

    @patch("event_wave_app.service.event_service.EventService.get_event")
    def test_get_event_success(self, mock_get_event):
        mock_event = event_1
        mock_get_event.return_value = mock_event
        response = self.client.get("/events/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, EventSchema().dump(event_1))

    @patch("event_wave_app.service.event_service.EventService.get_event")
    def test_get_event_not_found(self, mock_get_event):
        mock_get_event.return_value = None
        response = self.client.get("/events/1")
        self.assertEqual(response.status_code, 404)
        self.assertIn("message", response.json)

    @patch("event_wave_app.service.event_service.EventService.update_event")
    def test_update_event_success(self, mock_update_event):
        mock_event = event_3
        mock_event.date = date(2023, 3, 3)
        mock_event.time = time(0, 0, 0)
        mock_update_event.return_value = mock_event
        response = self.client.put("/events/3", json={"name": "John Doe"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, EventSchema().dump(event_3))

    @patch("event_wave_app.service.event_service.EventService.delete_event")
    def test_delete_event_success(self, mock_delete_event):
        response = self.client.delete("/events/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)

    def test_get_event_error(self):
        with patch(
            "event_wave_app.service.event_service.EventService.get_event"
        ) as mock_get_event:
            mock_get_event.side_effect = Exception("Test exception")
            response = self.client.get("/events/1")
            self.assertEqual(response.status_code, 500)
            self.assertIn("message", response.json)

    def test_get_event_error_message(self):
        with patch(
            "event_wave_app.service.event_service.EventService.get_event"
        ) as mock_get_event:
            mock_get_event.side_effect = ServiceException("Test exception")
            response = self.client.get("/events/1")
            self.assertEqual(response.status_code, 400)
            self.assertIn("message", response.json)

    def test_update_event_error(self):
        with patch(
            "event_wave_app.service.event_service.EventService.update_event"
        ) as mock_update_event:
            mock_update_event.side_effect = Exception("Test exception")
            response = self.client.put("/events/1", json={"name": "John Doe"})
            self.assertEqual(response.status_code, 500)
            self.assertIn("message", response.json)

    def test_update_event_error_with_message(self):
        with patch(
            "event_wave_app.service.event_service.EventService.update_event"
        ) as mock_update_event:
            mock_update_event.side_effect = ServiceException("Test exception")
            response = self.client.put("/events/1", json={"name": "John Doe"})
            self.assertEqual(response.status_code, 400)
            self.assertIn("message", response.json)

    def test_delete_event_error(self):
        with patch(
            "event_wave_app.service.event_service.EventService.delete_event"
        ) as mock_delete_event:
            mock_delete_event.side_effect = Exception("Test exception")
            response = self.client.delete("/events/1")
            self.assertEqual(response.status_code, 500)
            self.assertIn("message", response.json)

    def test_delete_event_error_message(self):
        with patch(
            "event_wave_app.service.event_service.EventService.delete_event"
        ) as mock_delete_event:
            mock_delete_event.side_effect = ServiceException("Customer exists")
            response = self.client.delete("/events/1")
            self.assertEqual(response.status_code, 400)
            self.assertIn("message", response.json)


class TestMultipleCustomerResource(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(MultipleEventResource, "/events")
        self.client = self.app.test_client()

    @patch("event_wave_app.service.event_service.EventService.get_events")
    def test_get_events_success(self, mock_get_events):
        mock_events = [event_1]
        mock_get_events.return_value = mock_events
        response = self.client.get("/events")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            EventSchema(exclude=["orders"]).dump(mock_events, many=True),
        )

    @patch("event_wave_app.service.event_service.EventService.get_events")
    def test_get_events_with_filter_success(self, mock_get_events):
        mock_events = [event_1]
        mock_get_events.return_value = mock_events
        response = self.client.get("/events?from_date=2023-03-03&to_date=2023-03-04")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json,
            EventSchema(exclude=["orders"]).dump(mock_events, many=True),
        )

    @patch("event_wave_app.service.event_service.EventService.get_events")
    def test_get_events_error_message(self, mock_get_events):
        mock_get_events.side_effect = ServiceException("bla blabl ")
        response = self.client.get("/events")
        self.assertEqual(response.status_code, 400)
        self.assertIn("message", response.json)

    @patch("event_wave_app.service.event_service.EventService.get_events")
    def test_get_events_error_general(self, mock_get_events):
        mock_get_events.side_effect = Exception("bla blabl ")
        response = self.client.get("/events")
        self.assertEqual(response.status_code, 500)
        self.assertIn("message", response.json)

    @patch("event_wave_app.service.event_service.EventService.add_event")
    def test_add_event_success(self, mock_add_event):
        mock_event = event_1
        mock_event.date = date(2023, 5, 10)
        mock_event.time = time(0, 0, 0)
        mock_add_event.return_value = mock_event
        response = self.client.post("/events", json={"name": "John Doe"})
        self.assertEqual(response.status_code, 201)

    @patch("event_wave_app.service.event_service.EventService.add_event")
    def test_add_event_error_general(self, mock_add_event):
        mock_add_event.side_effect = Exception("blablablabl")
        response = self.client.post("/events", json={"name": "John Doe"})
        self.assertEqual(response.status_code, 500)
        self.assertIn("message", response.json)

    @patch("event_wave_app.service.event_service.EventService.add_event")
    def test_add_event_error_message(self, mock_add_event):
        mock_add_event.side_effect = ServiceException("blablablabl")
        response = self.client.post("/events", json={"name": "John Doe"})
        self.assertEqual(response.status_code, 400)
        self.assertIn("message", response.json)
