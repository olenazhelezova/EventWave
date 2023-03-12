from flask import render_template
from event_wave_app.service.customer_service import CustomerService
from . import app


@app.route("/orders")
@app.route("/")
@app.route("/index")
def orders():
    """
    Renders static frontend page for orders grid and corresponsing CRUD action
    """
    return render_template("orders.html", customers=CustomerService.get_customers())
