#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

from flask import Flask, request, render_template, url_for, redirect
from pyhipku import encode


app = Flask(__name__)


@app.route('/<current_ip>')
def index(current_ip):
    your_ip = request.remote_addr
    lines = encode(current_ip).split('\n')
    return render_template('cover.html', lines=lines, your_ip=your_ip,
                           current_ip=current_ip)


@app.route('/')
def get_ip():
    return redirect(url_for('index', current_ip=request.remote_addr))


@app.route('/random')
def random_ip():
    random_ip = '.'.join(map(str, [randint(0, 255) for _ in range(4)]))
    return redirect(url_for('index', current_ip=random_ip))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
