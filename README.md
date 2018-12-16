# Fixtures API
A simple REST API for obtaining footbal match fixtures.

Documentation at http://yudo-fixtures-api.herokuapp.com/docs/
APIs at http://yudo-fixtures-api.herokuapp.com/v1/

## Retrieve code

* `$ git clone https://github.com/yudori/fixtures-api.git`
* `$ cd fixtures-api`

## Installation

* `$ virtualenv -p /usr/bin/python3.6 venv`
* `$ source venv/bin/activate`
* `$ pip install -r requirements/dev.txt`
* `$ python manage.py migrate`

## Running

* `$ python manage.py runserver`

## Testing

* `$ pytest`
