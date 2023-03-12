"""
This module defines Flask RESTful resources for handling Event objects.

Includes two classes:
    - SingleEventResource: handles GET, PUT, and DELETE operations for a single Event object
    - MultipleEventResource: handles GET operation for multiple Event objects
        and POST operation for creating new event.
"""
# pylint:disable=duplicate-code
# pylint:disable=W0718
from flask_restful import Resource
from flask import request
from event_wave_app.schemas.event import EventSchema
from event_wave_app.service.event_service import EventService
from event_wave_app.service.helpers import ServiceException
from event_wave_app.rest.api_messages import (
    NOT_FOUND_ERROR_MESSAGE,
    APPLICATION_ERROR_MESSAGE,
    SUCCESS_DELETE_MESSAGE,
    to_message,
)


class SingleEventResource(Resource):
    """
    Resource for managing a single event, identified by its ID.
    """

    def get(self, event_id):
        """
        Retrieve a single event by ID.

        :param event_id: The ID of the event to retrieve.
        :return: The requested event, serialized as JSON, with an HTTP status code of 200 or
             message and a status code 404 if the event was not found.
        :raises ServiceException: If an error occurred while retrieving the event.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while
            retrieving the event.
        """
        try:
            event = EventService.get_event(event_id)
            if event is None:
                return to_message(NOT_FOUND_ERROR_MESSAGE), 404
            return EventSchema().dump(event), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

    def put(self, event_id):
        """
        Update a single event by ID.

        :param event_id: The ID of the event to update.
        :return: The updated event, serialized as JSON, with an HTTP status code of 200.
        :raises ServiceException: If an error occurred while updating the event.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while updating the event.
        """
        try:
            event = EventService.update_event(event_id, request.json)
            return EventSchema().dump(event), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

    def delete(self, event_id):
        """
        Delete a single event by ID.

        :param event_id: The ID of the event to delete.
        :return: A success message, with an HTTP status code of 200.
        :raises ServiceException: If an error occurred while deleting the event.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while deleting the event.
        """
        try:
            EventService.delete_event(event_id)
            return to_message(SUCCESS_DELETE_MESSAGE), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500


class MultipleEventResource(Resource):
    """
    This resource defines the HTTP methods for retrieving multiple
    events or creating new event.
    """

    def get(self, from_date=None, to_date=None):
        """
        Retrieve a list of events.

        :param from_date (optional): A string representing the earliest date for events to include.
        :param to_date (optional): A string representing the latest date for events to include.
        :return: A list of events, serialized as JSON, with an HTTP status code of 200.
        :raises ServiceException: If an error occurred while retrieving the list of events.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while retrieving
            the list of customers.
        """
        try:
            from_date = request.args.get("from_date")
            to_date = request.args.get("to_date")
            if from_date or to_date:
                events = EventService.get_events(from_date=from_date, to_date=to_date)
            else:
                events = EventService.get_events()
            return EventSchema(exclude=["orders"]).dump(events, many=True), 200
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500

    def post(self):
        """
        Create a new event.

        :return: The newly created event.
        :raises ServiceException: If an error occurred while creating the new event.
        :raises APPLICATION_ERROR_MESSAGE: If there is an unexpected error while
            creating the new event.
        """
        try:
            event = EventService.add_event(request.json)
            return EventSchema().dump(event), 201
        except ServiceException as error:
            return to_message(str(error)), 400
        except Exception:
            return to_message(APPLICATION_ERROR_MESSAGE), 500
