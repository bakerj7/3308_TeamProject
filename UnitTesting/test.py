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
        #Remove all lists in Lists folder
        for i in range(1,6):
            file = "./Lists/test_"+ str(i) +".txt"
            if os.path.exists(file):
                os.remove(file)
        #os.rmdir("Lists")
        pass

    #Test Cases
    #Unit test for filtering movie list by category.
    def test_filters(self):
        #Test Genre filtering
        movieApp_test.movieApp("test_1", "Action", "None")
        count = 0
        with open("./Lists/test_1.txt") as f:
            next(f); next(f); next(f); next(f)
            for line in f:
                self.assertTrue("Action" in line)
                next(f)
                count += 1
        self.assertEqual(14, count)  #Make sure all lines were found

        #Test Actor filtering
        movieApp_test.movieApp("test_2", "Action", "Johnny Depp")
        count = 0
        with open("./Lists/test_2.txt") as f:
            next(f); next(f); next(f); next(f)
            for line in f:
                self.assertTrue("Johnny Depp" in line)
                next(f)
                count += 1
        self.assertEqual(3, count)  #Make sure all lines were found

        #Test Genre and Actor filtering
        movieApp_test.movieApp("test_3", "Drama", "Robert De Niro")
        count = 0
        with open("./Lists/test_3.txt") as f:
            next(f); next(f); next(f); next(f)
            for line in f:
                self.assertTrue(("Drama" in line) and ("Robert De Niro" in line))
                next(f)
                count += 1
        self.assertEqual(2, count)  #Make sure all lines were found

        #Test Genre not present
        with self.assertRaises(ValueError):
            movieApp_test.movieApp("test_4", "ABCD", "None")

        #Test Actor not present
        with self.assertRaises(ValueError):
            movieApp_test.movieApp("test_5", "Action", "ABCD")


    def test_list_create(self):
        # Test Creation of .txt file
        # Check if file exsists
        movieApp_test.movieApp("test_1", "Drama", "Marlon Brando")
        self.assertTrue(os.path.isfile('./Lists/test_1.txt'))

        movieApp_test.movieApp("test_2", "Action", "Ruth Wilson")
        self.assertTrue(os.path.isfile('./Lists/test_2.txt'))

        #Check if file in not empty
        movieApp_test.movieApp("test_3", "Adventure", "Scarlett Johansson")
        self.assertTrue(os.path.getsize('./Lists/test_3.txt') > 0)

        movieApp_test.movieApp("test_4", "Documentary", "Daniel Radcliffe")
        self.assertTrue(os.path.getsize('./Lists/test_3.txt') > 0)


    def test_user_list(self):
        movieApp_test.movieApp("test_1", "Drama", "Marlon Brando")
        movieApp_test.movieApp("test_2", "Action", "Ruth Wilson")
        movieApp_test.movieApp("test_3", "Adventure", "Scarlett Johansson")
        movieApp_test.movieApp("test_4", "Documentary", "Daniel Radcliffe")


        def find_user_lists(file_name):
            folder = os.listdir("./Lists")
            if file_name in folder:
                return True
            else:
                False

        # Find files by file name; file name is same as username.
        self.assertTrue(find_user_lists('test_1.txt'))
        self.assertTrue(find_user_lists('test_2.txt'))
        self.assertTrue(find_user_lists('test_3.txt'))
        self.assertTrue(find_user_lists('test_4.txt'))

        # Test for false positives
        self.assertFalse(find_user_lists('test_29.txt'))
        self.assertFalse(find_user_lists('test.txt'))
        self.assertFalse(find_user_lists('test_9.txt'))


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
