from datetime import date, time
from event_wave_app.models import *


customer_1 = Customer("Richard Big", "+443456567894", "richard.big@gmail.com")
customer_2 = Customer("Moe Lester", "+447975777666", "moe.lester@gmail.com")
customer_3 = Customer("Hugh Jass", "+44796223344", "hugh.jass@gmail.com")

event_1 = Event(
    "Depeche Mode", "2020-02-06", "11:00", "London", "Twickenham Stadium", 2000, [], 0
)

event_2 = Event(
    "Placebo", "2020-02-08", "12:00", "Glasgow", "Hampden Park", 15, [], 20
)

event_3 = Event("The Cure", "2020-02-07", "13:00", "Belfast", "SSE Arena", 3200, [], 15)

order_1 = Order(event_1.id, 200.00, 2, "2020-02-03", customer_1.id)
order_2 = Order(event_2.id, 150.00, 2, "2020-02-04", customer_2.id)
order_3 = Order(event_3.id, 180.00, 1, "2020-02-05", customer_3.id)
order_with_ref = Order(123, 200.00, 2, "2020-02-06", 321)
order_1_upd = Order(event_1.id, 190.00, 5, "2020-02-07", customer_1.id)

customer_4 = Customer("Bla Bla", "+1111111111", "bla@bla.bla", [order_1, order_2])
event_4 = Event(
    "The Cure",
    "2020-02-07",
    "13:00",
    "Belfast",
    "SSE Arena",
    3200,
    [order_1, order_2],
    15,
)
