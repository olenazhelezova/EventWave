from flask import render_template
from . import app


@app.route("/customers")
def customers():
    """
    Renders static frontend page for customers grid and corresponsing CRUD action
    """
    return render_template("customers.html")
