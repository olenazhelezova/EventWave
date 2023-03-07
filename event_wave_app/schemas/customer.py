"""
This module defines the `CustomerSchema` class, which provides 
a Marshmallow schema for the `Customer` model.
"""
# pylint: disable=too-few-public-methods
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from event_wave_app.models.customer import Customer

class CustomerSchema(SQLAlchemyAutoSchema):
    """
    Marshmallow schema for the `Customer` model.
    """
    class Meta:
        """
        Meta class that specifies the model to use, whether to load instances,
        and whether to include relationships.
        """
        model = Customer
        load_instance = True
