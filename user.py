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
    def find_by_password(cls, password):
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

    @classmethod
    def user_exist(cls, password):
        '''
        it checks if user exists from the list.
        Args:
            passwrd: if it exists
        Returns :
            Boolean: True or false depending if user exists
        '''
        for user in cls.user_list:
            if user.password == password:
                    return True

        return False


    @classmethod
    def display_users(cls):
        '''
        shows the user list
        '''
        return cls.user_list


    @classmethod
    def copy_email(cls,password):
        user_found = User.find_by_password(password)
        pyperclip.copy(user_found.email)


