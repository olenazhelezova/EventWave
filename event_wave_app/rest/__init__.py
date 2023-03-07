"""
This package contains modules defining customer, order and event REST APIs and
functions initializes the API endpoints for the EventWave app.
"""
# pylint: disable=cyclic-import
from event_wave_app import api
from . import customer
from . import event
from . import order

def init_api():
    """
    Initializes the API resources for the EventWave app.

    This function adds the following resources to the Flask-Restful API:
    - MultipleOrderResource
    - SingleOrderResource
    - MultipleEventResource
    - SingleEventResource
    - MultipleCustomerResource
    - SingleCustomerResource
    """
    api.add_resource(order.MultipleOrderResource, "/api/orders/")
    api.add_resource(order.SingleOrderResource, "/api/orders/<int:order_id>")
    api.add_resource(event.MultipleEventResource, "/api/events/")
    api.add_resource(event.SingleEventResource, "/api/events/<int:event_id>")
    api.add_resource(customer.MultipleCustomerResource, "/api/customers/")
    api.add_resource(customer.SingleCustomerResource, "/api/customers/<int:customer_id>")
    