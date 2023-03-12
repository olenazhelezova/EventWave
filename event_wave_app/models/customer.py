"""
Customer model used to represent customers
"""
# pylint: disable=cyclic-import
from sqlalchemy import Column, Integer, String
from event_wave_app import db


class Customer(db.Model):
    """
    Model representing customer
    :param name: customer's name
    :param phone_number: customer's phone number
    :param email: customer's e-mail
    """

    # pylint: disable=too-few-public-methods
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)

    orders = db.relationship("Order", back_populates="customer")

    def __init__(self, name, phone_number, email, orders=None):
        if orders is None:
            orders = []
        db.Model.__init__(
            self, name=name, phone_number=phone_number, email=email, orders=orders
        )

    def to_dict(self):
        """
        Return a dictionary from its fields
        """
        return {
            "id": self.id,
            "name": self.name,
            "phone_number": self.phone_number,
            "email": self.email,
        }
