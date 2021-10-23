#!/usr/bin/env python3.8
from user import User
from credentials import Creds

## for the user class

def new_user(first_name,last_name,phone_number,email,username,password):
    '''
    new_user method creates a new user
    '''
    new_user = User(first_name,last_name,phone_number,email,username,password)
    return new_user

def save_new_user(user):  
    '''
    save_user
    '''
    user.save_user()

def delete_new_user(user):  
    '''
    deletes_user
    '''
    user.delete_user()
def find_new_user(user):
    '''
    finds users
    '''
    user.find_by_username()
##credentials class
def new_creds(account_name,account_username,account_password):
    '''
    creates new account in credentials

    '''
    new_creds= Creds(account_name,account_username,account_password)
    return new_creds



