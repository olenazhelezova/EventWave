"""
This module consists of the CRUD operations to work with `events` table.
"""
import re
from typing import List
from event_wave_app import db
from event_wave_app.models import Event
from .helpers import ServiceException, validate_date


class EventService:
    """A class that provides CRUD operations for events."""

    @staticmethod
    def get_events(from_date=None, to_date=None) -> List[Event]:
        """
        Retrieve a list of events filtered by date range.

        :param from_date (optional): Start date in format 'YYYY-MM-DD'.
        :param to_date (optional): End date in format 'YYYY-MM-DD'.
        :return: List of Event objects.
        :raises ServiceException: If either date argument is invalid.
        """
        query = Event.query
        if from_date:
            validate_date(from_date)
            query = query.filter(Event.date >= from_date)
        if to_date:
            validate_date(to_date)
            query = query.filter(Event.date <= to_date)
        query = query.order_by(Event.date.asc())
        return query.all()

    @staticmethod
    def get_event(event_id) -> Event:
        """
        Retrieve an event by ID.

        :param id: Event ID.
        :return: The Event object matching the ID, or None if no match is found.
        """
        return Event.query.filter_by(id=event_id).first()

    @staticmethod
    def add_event(data: dict) -> Event:
        """
        Adds a new Event object to the database.

        :param data: A dictionary containing the fields of the Event object.
        :return: The new Event object.
        """
        EventService.__validate_data(data)
        event_exists = (
            Event.query.filter_by(name=data["name"], date=data["date"]).first()
            is not None
        )
        if event_exists:
            raise ServiceException("Event with the same name and date already exists!")
        event = Event(
            data["name"],
            data["date"],
            data["time"],
            data["city"],
            data["location"],
            data["availability"],
        )
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def update_event(event_id, data: dict) -> Event:
        """
        Updates the Event object with the specified ID in the database.

        :param id: The ID of the Event.
        :param data: A dictionary containing the updated fields of the Event object.
        :return: The updated Event object.
        """
        EventService.__validate_data(data)
        event = Event.query.filter_by(id=event_id).first()
        if event is None:
            raise ServiceException("Event doesn't exist.")
        event.name = data["name"]
        event.date = data["date"]
        event.time = data["time"]
        event.city = data["city"]
        event.location = data["location"]
        event.availability = data["availability"]
        db.session.add(event)
        db.session.commit()
        return event

    @staticmethod
    def delete_event(event_id) -> None:
        """
        Deletes the Event object with the specified ID from the database.

        :param id: The ID of the Event.
        :raises ServiceException: If the Event object with the specified ID does not exist
            in the database.
        """
        event = Event.query.filter_by(id=event_id).first()
        if event:
            if len(event.orders) > 0:
                raise ServiceException("You can not delete this event.")
            db.session.delete(event)
            db.session.commit()
        else:
            raise ServiceException("This event doesn't exist.")

    @staticmethod
    def __validate_data(data: dict) -> None:
        """
        Validates if the data dictionary contains all the required keys and if the values
        for those keys are in the correct format.

        :param data: A dictionary representing the data to be validated.
        :raises ServiceException: If the data is missing any required fields or if the values for
            any of the fields are invalid.
        """
        if not all(
            key in data
            for key in ("name", "date", "time", "city", "location", "availability")
        ):
            raise ServiceException("Missing required fields.")
        if not 3 <= len(data["name"]) <= 50:
            raise ServiceException("Invalid name.")
        validate_date(data["date"])
        if (
            re.fullmatch(r"^([01]\d|2[0-3]):([0-5]\d(:00)?)$", str(data["time"]))
            is None
        ):
            raise ServiceException("Invalid time format.")
        if not 3 <= len(data["city"]) <= 50:
            raise ServiceException("Invalid city name.")
        if not 3 <= len(data["location"]) <= 50:
            raise ServiceException("Invalid location.")
        if re.fullmatch(r"^[0-9]*$", str(data["availability"])) is None:
            raise ServiceException("Invalid availability.")
