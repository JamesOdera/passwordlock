import pyperclip
import random

class Credentials:
    '''
    credentials class to create new credentials
    '''
    
    credentials_list = [] 

    def __init__(self,name,credential,password,email):


        self.name = name
        self.credential = credential
        self.password = password
        self.email = email

    def save_credentials(self):

        '''
        save credentials
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_password(cls,password):
      

        for credentials in cls.credentials_list:
            if credentials.password == password:
                return credentials

    @classmethod
    def credentials_exist(cls,password):
     
        for credentials in cls.credentials_list:
            if credentials.password == password:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns cerdentials list
        '''
        return cls.credentials_list

    @classmethod
    def copy_email(cls,password):
        credentials_found = Credentials.find_by_password(password)
        pyperclip.copy(credentials_found.email)

    
