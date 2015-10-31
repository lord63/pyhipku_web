# Pyhipku site

[![Build Status][1]][2]

This is the source code repo for the web page: [pyhipku_web][], an online demo for [pyhipku][].

Use bootstrap [cover template][], color theme is from [uiGradients][].

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## How to run it:

install the requirements first, it's recommanded to use virtualenv

    $ virtualenv venv
    $ . venv/bin/activate
    (venv)$ pip install -r requirements.txt

run the app:

    (venv)$ gunicorn pyhipku_web:app

open your browser and have a look at `127.0.0.1:8000`

## Run the tests

after installed the requirements, run the tests is easy:

    (venv)$ python test_pyhipku_web.py

## License

MIT.

[1]: https://travis-ci.org/lord63/pyhipku_web.svg
[2]: https://travis-ci.org/lord63/pyhipku_web
[cover template]: http://getbootstrap.com/examples/cover/
[uiGradients]: https://github.com/Ghosh/uiGradients
[pyhipku_web]: http://pyhipku.lord63.com/
[pyhipku]: https://github.com/lord63/pyhipku
