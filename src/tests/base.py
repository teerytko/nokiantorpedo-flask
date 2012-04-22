'''
Created on 22.4.2012

@author: teerytko
'''

import unittest

from userapp import create_userapp
from settings import DefaultConfig
from flask import current_app

class TestConfig(DefaultConfig):
    DATABASE_ENGINE = 'sqlite://'

class TestCase(unittest.TestCase):
    uapp = create_userapp(TestConfig)
    def setUp(self):
        self.app = self.uapp.test_client()
        self.uapp.init_db()

    def tearDown(self):
        self.uapp.clear_db()