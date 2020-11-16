# Microblog Application

This is a microblog application utilizing Python Flask framework for backend and vanilla JavaScript/HLM/CSS for frontend.

This app is based on a fantastic [Flask Mega-Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) which I highly recommend you to check out.

The current version is still a _work in progress_. I will be adding additional functionalities in the future.

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
- JavaScript
- HTML5
- CSS3

## Installation

```
$ git clone https://github.com/sid2021/flask-microblog.git
$ cd flask-microblog
```

If you want to use virtualenv (on Windows):

```
$ python -m venv env
$ venv\Scripts\activate
```

If you want to use virtualenv (on MacOS/Linux):

```
$ python3 -m venv venv
$ source env/bin/activate
```

Install dependencies, set FLASK-APP environment variable and run app (on Windows):

On Windows

```
$ pip install -r requirements.txt
$ $env:FLASK_APP="microblog.app"
$ flask run
```

On MacOS/Linux:

```
$ pip install -r requirements.txt
$ export FLASK_APP=microblog.py
$ flask run
```
