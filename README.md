# EventWave

![](./coverage.svg)
EventWave is an application that manages events, customers, and orders. It provides a platform for event organizers to create and manage their events, orders and information about customers. It uses RESTful web service to perform CRUD operations.

## With this app you can:

- Display a list of events with event name, date, time, city and location, the number of available tickets and the number of tickets sold, calculated automatically.
- Display the list of customers with name, phone number and e-mail, in the edit field of the customer, information about previous orders is displayed.
- Display the ticket order sheet with information about the name and date of the event, the price of one ticket, the number of tickets purchased, the total cost, the order date and the email of the user who ordered the tickets.
- Change (add / edit / delete) the above data.

## Getting started

Before you start using the application, please ensure that you have Python 3.9 installed on your system.

## How to build this project:

### Clone the repo:

```
git clone https://github.com/olenazhelezova/EventWave.git
```

### Create the virtual environment in project:

```
virtualenv venv
source env/bin/activate
```

### Install project requirements:

```
pip install -r requirements.txt
```

### Configure MySQL database

#### Set the following environment variables:

```
MYSQL_USER=<your_mysql_user>
MYSQL_PASSWORD=<your_mysql_user_password>
MYSQL_SERVER=<your_mysql_server>
MYSQL_DATABASE=<your_mysql_database_name>
```

_You can set these in .env file as the project uses dotenv module to load
environment variables_

#### Run migrations to create database infrastructure:

- `flask db init`
- `flask db migrate`
- `flask db update`

#### Optionally populate the database with sample data:

```
flask db_seed
```

## Now you should be able to access the web service and web application on the following addresses:

### Web Service:

```
localhost:5000/api/events
localhost:5000/api/events/<id>
localhost:5000/api/events/?from_date=<YYYY-MM-DD>&to_date=<YYYY-MM-DD>
localhost:5000/api/events/?from_date=<YYYY-MM-DD>
localhost:5000/api/events/?to_date=<YYYY-MM-DD>
localhost:5000/api/orders
localhost:5000/api/orders/<id>
localhost:5000/api/orders/?from_date=<YYYY-MM-DD>&to_date=<YYYY-MM-DD>
localhost:5000/api/orders/?from_date=<YYYY-MM-DD>
localhost:5000/api/orders/?to_date=<YYYY-MM-DD>
localhost:5000/api/customers
localhost:5000/api/customers/<id>
```

### Web Application:

```
localhost:5000/
localhost:5000/index
localhost:5000/orders
localhost:5000/events
localhost:5000/customers
```
