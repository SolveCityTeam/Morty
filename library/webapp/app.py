#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:13:02 2017

@author: Patrick Woo-Sam
"""

from flask import Flask, request, jsonify, render_template
from helpers import api_helpers

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('Morty.html')


@app.route('/search')
def search():
    query = request.query_string.decode()
    kwargs = api_helpers.query_to_dict(query)
    return jsonify(**kwargs)


if __name__ == '__main__':
    app.run()
