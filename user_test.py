import unittest # Importing the unittest module
import pyperclip
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for user class

    '''


    def setUp(self):
        '''
        Set method to run before test classes
        '''
        self.new_user = User("James","Odera","6656","nyangoma.odera@gmail.com") # create user object


    def test_init(self):
        '''
        test_init_ to test if the object is initialized well
        '''

        self.assertEqual(self.new_user.first_name,"James")
        self.assertEqual(self.new_user.last_name,"Odera")
        self.assertEqual(self.new_user.password,"6656")
        self.assertEqual(self.new_user.email,"nyangoma.odera@gmail.com")


if __name__ == '__main__':
    unittest.main()