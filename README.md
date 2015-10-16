UrlShortener
========

To setup the project you need the following packages installed:
```
Git
Python 2.7
pip
virtualenv
virtualenvwrapper
Django==1.8
argparse==1.2.1
wsgiref==0.1.2


Setup
-----
* ``git clone https://github.com/AnastasiaFilatova/UrlShortener.git``
* ``mkvirtualenv <env_name>``
* ``cd UrlShortener && pip install -r requirements.txt``
* ``python manage.py makemigrations``
* ``python manage.py migrate``
* ``python manage.py load_db words.txt [--debug]``


Running the application
-----------------------
Run the following command in the repository root: ``python manage.py runserver``.
If you see the message ``Development server is running at http://127.0.0.1:8000/`` app is running.


Running tests
-------------
To start tests run ``python -m unittest discover`` command from the project root.




