
import unittest 
import pyperclip
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    test class that defines credentials behaviour
    '''
    

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("James", "facebook", "6656", "jim@gmail.com")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.name,"James")
        self.assertEqual(self.new_credentials.credential,"facebook")
        self.assertEqual(self.new_credentials.password,"6656")
        self.assertEqual(self.new_credentials.email,"jim@gmail.com")


    

    def test_save_credentials(self):
      
        self.new_credentials.save_credentials() 
        self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()