#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

from flask import Flask, request, render_template, url_for, redirect
from pyhipku import encode


app = Flask(__name__)


@app.route('/<ip>')
def index(ip):
    lines = encode(ip).split('\n')
    return render_template('cover.html', lines=lines)


@app.route('/')
def get_ip():
    return redirect(url_for('index', ip=request.remote_addr))


@app.route('/random')
def random_ip():
    random_ip = '.'.join(map(str, [randint(0, 255) for _ in range(4)]))
    return redirect(url_for('index', ip=random_ip))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
