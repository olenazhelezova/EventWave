"""
This module defines the `OrderSchema` class, which provides
a Marshmallow schema for the `Order` model.
"""
# pylint: disable=too-few-public-methods
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from event_wave_app.models.order import Order

class OrderSchema(SQLAlchemyAutoSchema):
    """
    Marshmallow schema for the `Order` model.
    """
    class Meta:
        """
        Meta class that specifies the model to use, whether to load instances,
        and whether to include relationships.
        """
        model = Order
        load_instance = True
        include_relationships = True

    event = fields.Nested("EventSchema", many=False)
    customer = fields.Nested("CustomerSchema", many=False)
