"""
This package contains modules defining customer, event and order services:
Modules:
- `customer_view.py`: defines customer views
- `event_view.py`: defines event views
- `order_view.py`: defines order views
"""
# pylint: disable=cyclic-import
from event_wave_app import app

from .customer_view import *
from .event_view import *
from .order_view import *
