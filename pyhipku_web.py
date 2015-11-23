#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from flask import Flask, request, render_template, url_for, redirect, abort
from pyhipku import encode


app = Flask(__name__)


@app.route('/<current_ip>')
def index(current_ip):
    your_ip = request.remote_addr
    try:
        lines = encode(current_ip).strip().split('\n')
    except ValueError:
        abort(400)
    return render_template('cover.html', lines=lines, your_ip=your_ip,
                           current_ip=current_ip)


@app.errorhandler(400)
def bad_requests(error):
    return render_template('cover.html', error=True), 400


@app.route('/')
def get_ip():
    current_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return redirect(url_for('index', current_ip=current_ip))


@app.route('/random')
def random_ip():
    if random.random() < 0.5:
        random_ip = '.'.join(map(str,
                                 [random.randint(0, 255) for _ in range(4)]))
    else:
        random_ip = ':'.join('{0:x}'.format(random.randint(0,2**16-1))
                                            for _ in range(8))
    return redirect(url_for('index', current_ip=random_ip))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
