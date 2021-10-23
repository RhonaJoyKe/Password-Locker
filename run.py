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
def create_password():
    
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
                            f_name = input()

                            print("Please Enter your Last name ...")
                            l_name = input()

                            print("Please Enter your Phone number ...")
                            p_number = input()

                            print("Please Enter your Email address ...")
                            e_address = input()

                            print("Please Enter your Username ...")
                            u_name = input()

                            print("Please Enter your Password ...")
                            p_word = input()
                       


if __name__ ==  '__main__':
    main()


