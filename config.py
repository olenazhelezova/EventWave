import os

user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
server = os.environ.get('MYSQL_SERVER')
database = os.environ.get('MYSQL_DATABASE')

class Config():
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{server}/{database}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    