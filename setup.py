from setuptools import setup, find_packages

setup(
    name = 'Event Wave',
    version = '1.0',
    author='Olena Zheliezova',
    author_email='lena.zhelezova@gmail.com',
    description='Web application to manage ticket orders, events and customers using web service',
    url = 'https://github.com/olenazhelezova/EventWave',
    install_requires=[
        'Flask==2.2.3',
        'Flask-RESTful==0.3.9',
        'Flask-SQLAlchemy==2.5.1'
    ],
    include_package_data = True,
    packages = find_packages(),
    zip_safe=False
)