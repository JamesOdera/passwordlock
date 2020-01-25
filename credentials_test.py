
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

    def tearDown(self):


            Credentials.credentials_list = []



    def test_save_multiple_credentials(self):
            '''
             save multiple credents
            '''
            self.new_credentials.save_credentials()
            test_save_credentials = Credentials("Test","user","6656","jim@gmail.com") 
            test_save_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
            
            self.new_credentials.save_credentials()
            test_save_credentials = Credentials("Test","user","6656","jim@gmail.com") 
            test_save_credentials.save_credentials()

            self.new_credentials.delete_credentials()
            self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_password(self):
        '''
        test to check if we can find a credential by password and display infor
        '''

        self.new_credentials.save_credentials()
        test_save_credentials = Credentials("Test","user","6656","jim@gmail.com")
        test_save_credentials.save_credentials()

        found_credentials = Credentials.find_by_password("6656")

        self.assertEqual(found_credentials.email,test_save_credentials.email)

    def test_credentials_exists(self):
      
        self.new_credentials.save_credentials()
        test_credentials_exists = Credentials("Test","user","6656","jim@gmail.com")
        test_credentials_exists.save_credentials()

        credentials_exists = Credentials.credentials_exist("6656")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        '''
        displays credentials
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_copy_email(self):

        self.new_credentials.save_credentials()
        Credentials.copy_email("6656")

        self.assertEqual(self.new_credentials.email,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()