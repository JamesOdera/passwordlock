#!/usr/bin/env python3.6

from user import User


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
    user.save_users()

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