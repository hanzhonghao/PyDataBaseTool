#!/usr/bin/env python
# encoding: utf-8
class MyException(Exception):

    def __init__(self, *args):
        self.args = args


class SqlException(MyException):
    def __init__(self, message='The table is not exist', args=('SqlException',)):
        self.args = args
        self.message = message






