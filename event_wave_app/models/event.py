"""
Event model used to represent events
"""
# pylint: disable=cyclic-import
from sqlalchemy import Column, Integer, String, Date, Time
from event_wave_app import db

class Event(db.Model):
    """
    Model representing event
    :param name: name of the event
    :param date: the date on which the event will take place
    :param time: the time at which the event will start
    :param city: the city where the event will take place
    :param location: the location where the event will take place
    :param availability: number of seats/spaces that are available for the event    
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    city = Column(String(50), nullable=False)
    location = Column(String(50),nullable=False)
    availability = Column(Integer, nullable=False)

    # pylint: disable=too-many-arguments
    def __init__(self, name, date, time, city, location, availability):
        db.Model.__init__(self, name=name, date=date, time=time,
        city=city, location=location, availability=availability)

    def to_dict(self):
        """
        Return a dictionary from its fields
        """
        return {
            'id':self.id,
            'name': self.name,
            'date': self.date,
            'time': self.time,
            'city': self.city,
            'location': self.location,
            'availability': self.availability
            }
