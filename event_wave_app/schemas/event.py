"""
This module defines the `EventSchema` class, which provides
a Marshmallow schema for the `Event` model.
"""
# pylint: disable=too-few-public-methods
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from event_wave_app.models.event import Event

class EventSchema(SQLAlchemyAutoSchema):
    """
    Marshmallow schema for the `Event` model.
    """
    class Meta:
        """
        Meta class that specifies the model to use, whether to load instances,
        and whether to include relationships.
        """
        model = Event
        load_instance = True
