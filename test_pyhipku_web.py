#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from pyhipku_web import app


# I get this from http://stackoverflow.com/a/14873171
class LocalTestClient(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['REMOTE_ADDR'] = environ.get('REMOTE_ADDR',
                                             '127.0.0.1')
        return self.app(environ, start_response)


class PyhipkuWebTestCase(unittest.TestCase):
    def setUp(self):
        app.wsgi_app = LocalTestClient(app.wsgi_app)
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_user_ip(self):
        rv = self.app.get('/', follow_redirects=True)
        assert '<h1>The hungry white ape</h1>' in rv.data
        assert 'Your IP: <a href="/127.0.0.1">127.0.0.1</a>'in rv.data
        assert 'Current IP:' not in rv.data

    def test_random_ip(self):
        rv = self.app.get('/random', follow_redirects=True)
        assert 'Your IP:' in rv.data
        assert 'Current IP:' in rv.data

    def test_illegal_ip(self):
        rv1 = self.app.get('/127.0.0.256')
        assert "<h1>Wrong IP address!</h1>" in rv1.data
        assert rv1.status_code == 400

        rv2 = self.app.get('/127.0.0')
        assert rv2.status_code == 400

        rv3 = self.app.get('/0::0:')
        assert rv3.status_code == 400

        rv4 = self.app.get('/0:0:0:0:0:z')
        assert rv4.status_code == 400

        rv5 = self.app.get('/helloworld')
        assert rv5.status_code == 400


if __name__ == '__main__':
    unittest.main()