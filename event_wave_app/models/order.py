"""
Order model used to represent ticket orders
"""
# pylint: disable=cyclic-import
from sqlalchemy import Column, Integer, Date, ForeignKey, FLOAT
from event_wave_app.models.customer import Customer
from event_wave_app.models.event import Event
from event_wave_app import db


class Order(db.Model):
    """
    Model representing order
    :param event_id:id of the event for which the ticket was ordered
    :param price: price per ticket
    :param qty: quantity of tickets purchased
    :param total_cost: total price of ticket/tickets
    :param order_date: the date on which the ticket/tickets were ordered
    :param customer_id: id of the customer who ordered the ticket
    """

    # pylint: disable=too-few-public-methods
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    price = Column(FLOAT, nullable=False)
    qty = Column(Integer, nullable=False)
    order_date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    event = db.relationship(Event, backref=db.backref("orders", lazy=True))
    customer = db.relationship(Customer)

    # pylint: disable=too-many-arguments
    def __init__(self, event_id, price, qty, order_date, customer_id):
        db.Model.__init__(
            self,
            event_id=event_id,
            price=price,
            qty=qty,
            order_date=order_date,
            customer_id=customer_id,
        )

    def to_dict(self):
        """
        Return a dictionary from its fields
        """
        return {
            "id": self.id,
            "event_id": self.event_id,
            "price": self.price,
            "qty": self.qty,
            "order_date": self.order_date,
            "customer_id": self.customer_id,
        }
