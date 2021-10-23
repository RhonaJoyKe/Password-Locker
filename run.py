#!/usr/bin/env python3.8
from user import User
from credentials import Creds
def new_user(first_name,last_name,phone_number,email,username,password):
    '''
    new_user method creates a new user
    '''
    new_user = User(first_name,last_name,phone_number,email,username,password)
    return new_user
