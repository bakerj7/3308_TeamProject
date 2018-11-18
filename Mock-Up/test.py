#!/usr/bin/env python3

#Movie Queue
#Unit Testing

import unittest
import os
os.system("pip install mock")
import mock
import movieApp

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
         
    #Unit test for filtering movie list by category.
    def test_filters(self):
        #Test Genre filtering
        userInputs = ["test_1", "Action", "None"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
        count = 0
        with open("./Lists/test_1.txt") as f:
            next(f); next(f); next(f); next(f)
            for line in f:
                self.assertTrue("Action" in line)
                next(f)
                count += 1
        self.assertEqual(1157, count), "checking all Action movies are found"
        #Test Actor filtering
        userInputs = ["test_2", "Action", "Johnny Depp"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
        count = 0
        with open("./Lists/test_2.txt") as f:
            next(f); next(f); next(f); next(f)
            for line in f:
                self.assertTrue("Johnny Depp" in line)
                next(f)
                count += 1
        self.assertEqual(9, count)  #Make sure all lines were found
        #Test Genre and Actor filtering
        userInputs = ["test_3", "Drama", "Robert De Niro"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
        count = 0
        with open("./Lists/test_3.txt") as f:
            next(f); next(f); next(f); next(f)
            for line in f:
                self.assertTrue(("Drama" in line) and ("Robert De Niro" in line))
                next(f)
                count += 1
        self.assertEqual(10, count)  #Make sure all lines were found
        #Test Genre not present
        userInputs = ["test_4", "ABCDE", "None"]
        with self.assertRaises(ValueError):
            with mock.patch('builtins.input', side_effect=userInputs):
                movieApp.createList()
                
        #Test Actor not present
        userInputs = ["test_5", "Action", "ABCDE"]
        with self.assertRaises(ValueError):
            with mock.patch('builtins.input', side_effect=userInputs):
                movieApp.createList()
                
    def test_list_create(self):
        # Test Creation of .txt file
        # Check if file exsists
        userInputs = ["test_1", "Drama", "Marlon Brando"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
        self.assertTrue(os.path.isfile('./Lists/test_1.txt'))

        userInputs = ["test_2", "Action", "Ruth Wilson"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
        self.assertTrue(os.path.isfile('./Lists/test_2.txt'))

        #Check if file in not empty
        userInputs = ["test_3", "Adventure", "Scarlett Johansson"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
        self.assertTrue(os.path.getsize('./Lists/test_3.txt') > 0)

        userInputs = ["test_4", "Documentary", "Daniel Radcliffe"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
        self.assertTrue(os.path.getsize('./Lists/test_3.txt') > 0)

    def test_user_list(self):
        userInputs = ["test_1", "Drama", "Marlon Brando"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()

        userInputs = ["test_2", "Action", "Ruth Wilson"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
            
        userInputs = ["test_3", "Adventure", "Scarlett Johansson"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()

        userInputs = ["test_4", "Documentary", "Daniel Radcliffe"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()

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

        # Test if file can be opened.
        def check_file(file_name):
            try:
                f = open('./Lists/' + file_name, 'r')
                f.close()
            except IOError:
                 return False
            return True

        self.assertTrue(check_file('test_1.txt'))
        self.assertTrue(check_file('test_2.txt'))
        self.assertTrue(check_file('test_3.txt'))
        self.assertTrue(check_file('test_4.txt'))
        
    def test_search(self):
        userInputs = ["test_1", "Drama", "Marlon Brando"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()

        userInputs = ["test_2", "Action", "Ruth Wilson"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
            
        userInputs = ["test_3", "Adventure", "Scarlett Johansson"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()

        userInputs = ["test_4", "Documentary", "Daniel Radcliffe"]
        with mock.patch('builtins.input', side_effect=userInputs):
            movieApp.createList()
            
        found = movieApp.findFile("test_1")
        self.assertEqual(True, found) #Make sure file was found
        found = movieApp.findFile("test_2")
        self.assertEqual(True, found) #Make sure file was found
        found = movieApp.findFile("test_3")
        self.assertEqual(True, found) #Make sure file was found
        found = movieApp.findFile("test_4")
        self.assertEqual(True, found) #Make sure file was found
        
        found = movieApp.findFile("notTest")
        self.assertEqual(False, found) #Make sure file was not found


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
