#!/usr/bin/env python3

#Movie Queue
#Unit Testing

import unittest
import os
import movieApp_test


class movieAppTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        #Remove Lists folder
        os.remove('Lists')
        pass

    #Test Cases
    #Unit test for filtering movie list by category.
    def test_filters(self):
        x = 0

    def test_list_create(self):
        x = 0

    def test_user_list(self):
        x = 0
