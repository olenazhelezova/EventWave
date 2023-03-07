from event_wave_app import db, app
from event_wave_app.models.customer import Customer
from event_wave_app.models.event import Event
from event_wave_app.models.order import Order

from datetime import date, time

@app.cli.command('db_seed')
def seed_db():
    customer_1 = Customer('Richard Big', '+443456567894', 'richard.big@gmail.com')
    customer_2 = Customer('Moe Lester', '+447975777666', 'moe.lester@gmail.com')
    customer_3 = Customer('Hugh Jass', '+44796223344', 'hugh.jass@gmail.com')

    db.session.add(customer_1)
    db.session.add(customer_2)
    db.session.add(customer_3)

    db.session.flush()

    event_1 = Event('Depeche Mode', date(2023, 6, 17), time(18, 00), 'London', 'Twickenham Stadium', 3500)
    event_2 = Event('Placebo', date(2023, 6, 21), time(20, 00), 'Glasgow', 'Hampden Park', 3000)
    event_3 = Event('The Cure', date(2023, 8, 20), time(19, 00), 'Belfast', 'SSE Arena', 3200)

    db.session.add(event_1)
    db.session.add(event_2)
    db.session.add(event_3)

    db.session.flush()

    order_1 = Order(event_1.id, 200.00, 2, date(2023, 2, 5), customer_1.id)
    order_2 = Order(event_2.id, 150.00, 2, date(2023, 2, 20), customer_2.id)
    order_3 = Order(event_3.id, 180.00, 1, date(2023, 2, 25), customer_3.id)

    db.session.add(order_1)
    db.session.add(order_2)
    db.session.add(order_3)

    db.session.commit()