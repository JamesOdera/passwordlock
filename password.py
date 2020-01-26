#!/usr/bin/env python3.6

from user import User
from credentials import Credentials


def create_user(fname,lname,password,email):
    '''
    Fxn to create a new user
    '''
    new_user = User(fname,lname,password,email)
    return new_user

def save_users(user):
    '''
    Fxn to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Fxn to delete user
    '''
    user.delete_user()

def find_user(password):
    '''
    Fxn to find user by passwrd
    '''
    return User.find_by_password(password)

def check_existing_users(password):
    '''
    Fxn to check if user exist
    '''
    return User.user_exist(password)

def display_users():
    '''
    Fxn to show saved users
    '''
    return User.display_users()

### CREDENTIALS
def create_credentials(name,credential,password,email):
    '''
    Fxn to create a new credents
    '''
    new_credentials = Credentials(name,credential,password,email)
    return new_credentials

def save_credentials(credentials):

    credentials.save_credentials()

def del_credentials(credentials):
   
    credentials.delete_credentials()

def find_credentials(password):
    '''
    Fxn to find crdtls by passwrd
    '''
    return Credentials.find_by_password(password)

def check_existing_credentials(password):
    '''
    Fxn to check if credents exist
    '''
    return Credentials.credentials_exist(password)

def display_credentials():
    '''
    Fxn to show saved credents
    '''
    return Credentials.display_credentials()

######
## Main function

def main():
    print("Hello Welcome to your user list. Your name, please?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cu - create a user a/c, du - display users, fu -find a user, cc - create credential, dc - display credential, fc - find credential, ex -exit the  list ")

        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-"*10)

            print ("First name ....")
            f_name = input()

            print("Last name ...")
            l_name = input()

            print("Password ...")
            p_password = input()

            print("Email address ...")
            e_address = input()


            save_users(create_user(f_name,l_name,p_password,e_address)) 
            print ('\n')
            print(f"New User {f_name} {l_name} created")
            print ('\n')
        
        # credent
        if short_code == 'cc':
            print("New Credential")
            print("-"*10)

            print ("Name ....")
            n_name = input()

            print("Credential ...")
            c_credential = input()

            print("Password ...")
            p_password = input()

            print("Email address ...")
            e_address = input()


            save_credentials(create_credentials(n_name,c_credential,p_password,e_address)) 
            print ('\n')
            print(f"New Credential {n_name} {c_credential} created")
            print ('\n')
        #

        elif short_code == 'du':

            if display_users():
                print("Here is a list of all your users")
                print('\n')

                for user in display_users():
                    print(f"{user.first_name} {user.last_name} .....{user.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any user list saved yet")
                print('\n')

    # credent
        elif short_code == 'dc':

            if display_credentials():
                print("Hello! This is a list of your credentials")
                print('\n')

                for credentials in display_credentials():
                    print(f"{credentials.name} {credentials.credential} .....{credentials.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have list of credents saved yet")
                print('\n')    
    #

        elif short_code == 'fu':
            
            if find_user(password):

                print("Enter the passwrd you want to search for")

                p_password = input()

            if check_existing_users(search_password):
                search_user = find_user(search_password)
                print(f"{search_user.first_name} {search_user.last_name}")
                print('-' * 20)

                print(f"Password.......{search_user.password}")
                print(f"Email address.......{search_user.email}")
            else:
                print(" does not exist")

## credent

        elif short_code == 'fc':
            
            if find_credentials(password):

                print("Enter the passwrd you want to search for")

                p_password = input()

            if check_existing_credentials(search_password):
                search_credentials = find_credentials(search_password)
                print(f"{search_credentials.name} {search_credentials.credential}")
                print('-' * 20)

                print(f"Password.......{search_credentials.password}")
                print(f"Email address.......{search_credentials.email}")
            else:
                print(" does not exist")

    ##



        elif short_code == "ex":
            print("Have a nice time .......")
            break
        else:
            print("Tumia hizi stuff unaona hapa!")

    
if __name__ == '__main__':

    main()