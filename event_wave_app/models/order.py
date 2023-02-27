"""
Order model used to represent ticket orders
"""
# pylint: disable=cyclic-import
from sqlalchemy import Column, Integer, Date, DECIMAL, ForeignKey

from event_wave_app import db

class Order(db.Model):
    """
    Model representing order
    :param event_id:id of the event for which the ticket was ordered
    :param cost: cost per ticket
    :param qty: quantity of tickets purchased
    :param total_cost: total cost of ticket/tickets
    :param order_date: the date on which the ticket/tickets were ordered
    :param customer_id: id of the customer who ordered the ticket
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'), nullable=False)
    cost = Column(DECIMAL(10, 2), nullable=False)
    qty = Column(Integer, nullable=False)
    total_cost = Column(DECIMAL(10, 2), nullable=False)
    order_date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    # pylint: disable=too-many-arguments
    def __init__(self, event_id, cost, qty, total_cost, order_date, customer_id):
        db.Model.__init__(self, event_id=event_id, cost=cost, qty=qty,
        total_cost=total_cost, order_date=order_date, customer_id=customer_id)

    def __repr__(self):
        """
        Returns string representation of the order
        :return: string representation of the order
        """
        return f"""<Order(event_id='{self.event_id}', cost='{self.cost}', qty='{self.qty}',
         total_cost='{self.total_cost}', order_date='{self.order_date}', customer_id='{self.customer_id}')>"""