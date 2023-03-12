"""
This package contains modules defining customer, order and event models:

This package contains the following modules:
- customer: Defines the `Customer` model representing customers.
- event: Defines the `Event` model representing events.
- order: Defines the `Order` model representing orders.
"""
# pylint: disable=E1102
from sqlalchemy.orm import column_property
from sqlalchemy import select, func

from .customer import Customer
from .event import Event
from .order import Order

Event.sold = column_property(
    select(func.coalesce(func.sum(Order.qty), 0))
    .where(Order.event_id == Event.id)
    .correlate_except(Order)
    .scalar_subquery()
)
