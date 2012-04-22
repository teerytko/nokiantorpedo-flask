'''
Created on 21.4.2012

@author: teerytko
'''

import os
import unittest
from tests.base import TestCase
import json

class RestUserTests(TestCase):
    def test_empty_db(self):
        rv = self.app.get('/users/')
        self.assertEquals(json.loads(rv.data), [])

    def test_create_user(self):
        rv = self.app.post('/users/', data=dict(name='Tester Erkki',
                                                email='test@t.com'))
        self.assertEquals(json.loads(rv.data)['success'], True)
        rv = self.app.get('/users/')
        self.assertEquals(json.loads(rv.data), [{'password': None, 
                                                 'email': 'test@t.com', 
                                                 'name': 'Tester Erkki', 
                                                 'id': 1}])

class RestUserTestsOperations(TestCase):
    def setUp(self):
        super(RestUserTestsOperations, self).setUp()
        self.app.post('/users/', data=dict(name='Tester Erkki',
                                           email='test@t.com',
                                           password='tester'))
        self.app.post('/users/', data=dict(name='Tester 2',
                                           email='test2@t.com'))

    def test_create_user_get_specific_user(self):
        rv = self.app.get('/users/1')
        self.assertEquals(json.loads(rv.data), {'password': 'tester', 
                                                 'email': 'test@t.com', 
                                                 'name': 'Tester Erkki', 
                                                 'id': 1})

    def test_create_users_and_find_users(self):
        rv = self.app.get('/users/find?name=Tester 2&id=2')
        self.assertEquals(json.loads(rv.data), [{'password': None, 
                                                 'email': 'test2@t.com', 
                                                 'name': 'Tester 2', 
                                                 'id': 2}])

    def test_update_user(self):
        rv = self.app.put('/users/2', data=dict(password='foo'))
        self.assertEquals(json.loads(rv.data)['success'], True)
        rv = self.app.get('/users/2')
        self.assertEquals(json.loads(rv.data), {'password': 'foo', 
                                                 'email': 'test2@t.com', 
                                                 'name': 'Tester 2', 
                                                 'id': 2},
                                                )

    def test_delete_user(self):
        rv = self.app.delete('/users/2')
        self.assertEquals(json.loads(rv.data)['success'], True)
        rv = self.app.get('/users/')
        self.assertEquals(json.loads(rv.data), [{'password': 'tester', 
                                                 'email': 'test@t.com', 
                                                 'name': 'Tester Erkki', 
                                                 'id': 1},
                                                ])


if __name__ == '__main__':
    unittest.main()