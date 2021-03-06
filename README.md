# Usage

    cd viztube
    export FLASK_APP=app.py
    # export FLASK_DEBUG=1    # only when developing
    flask run

# Documentation

* The web framework [Flask](http://flask.pocoo.org/docs/0.12/)
* The interface CSS/JS framework [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

# Project structure

    .
    ├── README.md
    ├── app.py                         # the controller
    ├── services                       # the services
    │   ├── service.py
    │   └── ...
    ├── static                         # all static files (CSS, JS, images)
    │   ├── bootstrap
    │   │   ├── css
    │   │   │   ├── bootstrap.min.css
    │   │   └── js
    │   │       ├── bootstrap.min.js
    │   ├── jquery-3.2.1.slim.min.js
    │   ├── popper.min.js
    │   ├── script.js
    │   └── style.css
    └── templates                      # all template (HTML)
        └── index.html.j2

Here are the different components:

     [1] + Incoming HTTP request:
         | GET /videos/1251/frames?boxes=ground-truth
         |
    +----v----------------------------------------------------+
    |                                                         |
    |   THE CONTROLLER APP.PY                                 | [8] HTTP response
    |   Parsing HTTP request and generating HTTP response     +------------>
    |                                                         |
    +----+------^------------------------------+------^-------+
     [2] |      | [5] Processed response   [6] |      | [7] A template
         |      | information                  |      |
         |      |                              |      |
    +----v------+----------+    +--------------v------+-------+
    |                      |    |                             |
    |  SERVICES            |    |  TEMPLATES                  |
    |  All the logic and   |    |  The HTML used to generate  |
    |  data processing     |    |  the response               |
    |                      |    |                             |
    +----+------^----------+    +-----------------------------+
     [3] |      | [4] Data
         |      | from DB
         |      |
    +----v------+----------------+
    |                            |
    |  MODELS                    |
    |  All the database queries  |
    |                            |
    +----------------------------+
