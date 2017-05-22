#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 18:28:03 2017

@author: Patrick Woo-Sam
"""


def query_to_dict(query):
    '''Return a dictionary of a query.

    Args:
        query -- string formatted like 'query=foo&startAuthorName=bar'

    Returns:
        sample -- {'query': 'foo', 'startAuthorName': 'bar'}
    '''
    kwargs = {}
    args = query.split('&')
    for arg in args:
        key, *value = arg.split('=')
        kwargs[key] = value
    return kwargs
