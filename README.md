# Altmertic Python-Django sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/dharma-s/altmetric-python.git
$ cd altmetric-python
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd telecom_mobility_project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/swagger/` for project api documentation.
And navigate to `http://127.0.0.1:8000/admin/` for project admin access.

Credentials are as
```
username-dharmendra
password - 1234
```