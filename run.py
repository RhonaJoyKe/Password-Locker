#!/usr/bin/env python3.8
import random
import string
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
def  save_new_creds(credentials):
    '''
    saves new account in credentials

    '''
    credentials.save_account()
def  delete_new_creds(credentials):
    '''
    saves new account in credentials

    '''
    credentials.delete_account()
def find_new_creds(account_username):
    '''
    finds new account in credentials

    '''
    return Creds.find_by_account_username(account_username)
def display_new_creds():
    '''
    displays contacts

    '''
    return Creds.display_accounts()
def create_password(length=6):
    '''
    creates password

    '''
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
#main function 
def main():
    print("Holla there,Cómo estás,Welcome to your Password Locker App. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
                    print("Use these short codes : na - create a new account, da - display contacts,lg-login into account, fa -find an account, ex -exit the password locker list ")

                    short_code = input().lower()

                    if short_code == 'na':
                            print("New Account")
                            print("-"*10)

                            print ("Please Enter your First name ....")
                            first_name = input()

                            print("Please Enter your Last name ...")
                            last_name = input()

                            print("Please Enter your Phone number ...")
                            phone_number = input()

                            print("Please Enter your Email address ...")
                            email = input()

                            print("Please Enter your Username ...")
                            username = input()

                            print("Please Enter your Password ...")
                            password = input()
                            save_new_user(new_user(first_name,last_name,phone_number,email,username,password))
                       


if __name__ ==  '__main__':
    main()


