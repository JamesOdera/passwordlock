import pyperclip


class User:
    """
    Class that generates new instances of contacts.
    """

    user_list = [] 

    def __init__(self,first_name,last_name,password,email):



        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email


    def save_user(self):    

        User.user_list.append(self)


    def delete_user(self):

        '''
        deletes user from list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns user that match the password

        Args:
            password: pass to search
        Returns :
            user
        '''

        for user in cls.user_list:
            if user.password == password:
                return user


