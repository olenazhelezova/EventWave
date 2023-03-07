from unittest.mock import patch
from event_wave_app.service.event_service import EventService
from event_wave_app.models.event import Event
from event_wave_app.tests.test_data import event_1, event_2, event_3
from event_wave_app.tests.test_case_base import TestCaseBase
from event_wave_app.service.helpers import ServiceException


class TestEventService(TestCaseBase):
    @patch("event_wave_app.models.event.Event.query")
    def test_get_events(self, query_mock):
        events = [event_1, event_2, event_3]
        query_mock.order_by.return_value.all.return_value = events
        results = EventService.get_events()
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), len(events))
        for event_result, event_obj in zip(results, events):
            self.assertIsInstance(event_result, Event)
            self.assertDictEqual(event_result.to_dict(), event_obj.to_dict())

    @patch("event_wave_app.models.event.Event.query")
    def test_get_events_filtering_by_date(self, query_mock):
        events = [event_1, event_2, event_3]
        query_mock.filter.return_value.filter.return_value.order_by.return_value.all.return_value = (
            events
        )
        results = EventService.get_events("2020-02-02", "2022-02-02")
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), len(events))
        for event_result, event_obj in zip(results, events):
            self.assertIsInstance(event_result, Event)
            self.assertDictEqual(event_result.to_dict(), event_obj.to_dict())

    @patch("event_wave_app.models.event.Event.query")
    def test_get_event(self, query_mock):
        event = event_1
        query_mock.filter_by.return_value.first.return_value = event
        result = EventService.get_event(event.id)
        self.assertIsInstance(result, Event)

    @patch("event_wave_app.db.session")
    @patch("event_wave_app.models.event.Event.query")
    def test_add_event_success(self, query_mock, db_session_mock):
        query_mock.filter_by.return_value.first.return_value = None
        event_data = event_1.to_dict()
        result = EventService.add_event(event_data)
        db_session_mock.add.assert_called_once_with(result)
        db_session_mock.commit.assert_called_once()

    def test_add_event_failed_validation(self):
        with self.assertRaises(ServiceException):
            EventService.add_event({})
        with self.assertRaises(ServiceException):
            EventService.add_event(
                {
                    "name": "T",
                    "date": "2023-32-10",
                    "time": "25:00:00",
                    "city": "La",
                    "location": "Ba",
                    "availability": "-3",
                }
            )
        with self.assertRaises(ServiceException):
            EventService.add_event(
                {
                    "name": "The National",
                    "date": "2023-13-32",
                    "time": "25:00:00",
                    "city": "La",
                    "location": "Ba",
                    "availability": "-3",
                }
            )
        with self.assertRaises(ServiceException):
            EventService.add_event(
                {
                    "name": "The National",
                    "date": "2023-10-01",
                    "time": "25:00:00",
                    "city": "La",
                    "location": "Ba",
                    "availability": "-3",
                }
            )
        with self.assertRaises(ServiceException):
            EventService.add_event(
                {
                    "name": "The National",
                    "date": "2023-10-01",
                    "time": "19:00:00",
                    "city": "La",
                    "location": "Ba",
                    "availability": "-3",
                }
            )
        with self.assertRaises(ServiceException):
            EventService.add_event(
                {
                    "name": "The National",
                    "date": "2023-10-01",
                    "time": "19:00:00",
                    "city": "Liverpool",
                    "location": "Ba",
                    "availability": "-3",
                }
            )
        with self.assertRaises(ServiceException):
            EventService.add_event(
                {
                    "name": "The National",
                    "date": "2023-10-01",
                    "time": "19:00:00",
                    "city": "Liverpool",
                    "location": "M&S Bank Arena",
                    "availability": "-3",
                }
            )

    @patch("event_wave_app.models.event.Event.query")
    def test_add_event_duplicate(self, query_mock):
        query_mock.filter_by.return_value.first.return_value = event_1
        with self.assertRaises(ServiceException):
            EventService.add_event(event_1.to_dict())

    @patch("event_wave_app.db.session")
    @patch("event_wave_app.models.event.Event.query")
    def test_update_event_success(self, query_mock, db_session_mock):
        query_mock.filter_by.return_value.first.return_value = event_1
        event_data = event_2.to_dict()
        result = EventService.update_event(event_1.id, event_data)
        db_session_mock.add.assert_called_once_with(result)
        db_session_mock.commit.assert_called_once()
        self.assertIsInstance(result, Event)

    @patch("event_wave_app.models.event.Event.query")
    def test_update_event_failure(self, query_mock):
        query_mock.filter_by.return_value.first.return_value = None
        with self.assertRaises(ServiceException):
            EventService.update_event(123, event_1.to_dict())

    @patch("event_wave_app.db.session")
    @patch("event_wave_app.models.event.Event.query")
    def test_delete_event_success(self, query_mock, db_session_mock):
        query_mock.filter_by.return_value.first.return_value = event_1
        EventService.delete_event(event_1.id)
        db_session_mock.delete.assert_called_once_with(event_1)
        db_session_mock.commit.assert_called_once()

    @patch("event_wave_app.models.customer.Customer.query")
    def test_delete_event_failure(self, query_mock):
        query_mock.filter_by.return_value.first.return_value = None
        with self.assertRaises(ServiceException):
            EventService.delete_event(666)
