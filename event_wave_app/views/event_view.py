from flask import render_template
from . import app


@app.route("/events")
def events():
    """
    Renders static frontend page for events grid and corresponsing CRUD action
    """
    return render_template("events.html")
