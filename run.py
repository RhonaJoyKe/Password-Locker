#!/usr/bin/env python3.8
import random
import string
from user import User
from credentials import Creds

## for the user class

def new_user(first_name,last_name,username,password):
    '''
    new_user method creates a new user
    '''
    new_user = User(first_name,last_name,username,password)
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
def find_new_user(username):
    '''
    finds users
    '''
    return User.find_by_username(username)

    
def user_password(username, password):  # check if the password is correct
    '''
    funtion to check whether the user enter the correct username and password
    '''
    return User.check_user(username, password)
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
    return credentials.delete_account()
def find_new_creds(account_name):
    '''
    finds new account in credentials

    '''
    return Creds.find_by_account_name(account_name)
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
        print("Use these short codes :")
        print("na - create a new account")
        print("lg-login into account") 
        print("ex -exit the password locker list ")

        short_code = input().lower()

        if short_code == 'na':
                            print("New Account")
                            print("-"*50)

                            print ("Please Enter your First name ....")
                            first_name = input()
                            print("-"*50)

                            print("Please Enter your Last name ...")
                            last_name = input()
                            print("-"*50)

                           

                            print("Please Enter your Username ...")
                            username = input()
                            print("-"*50)

                            print("Please Enter your Password ...")
                            password = input()
                            print("-"*50)
                            save_new_user(new_user(first_name,last_name,username,password))
                            print('-'*50)
                            print(f"Hello {first_name}.Congratulations Account created successfully. Proceed to login to access your account")
                            print('-'*50)
        elif short_code == 'lg':
            print("Welcome to the Login Portal")
            print("-"*50)
            print("Please Enter your Username ...")
            username = input()
            print("-"*50)
            print("Please Enter your Password ...")
            password = input()
            print("-"*50)
            if username != 'Jojo' and password!= '12345':
                    print('The account does not exist, please create an account')
            else:
                    print(f'Hello {username}. Welcome to your socials password locker account')
                    print ('\n')
                    s_accounts_view()

                    
                   

def s_accounts_view():
        
    print('Good news, you can easily store your social accounts credentials here!')
  
    print('Use these short codes')
    print ('\n')
    while True:
        print('nc - Add a new social account credentials')
        print('ec - Add an existing social account credentials')
        print('da - Display saved social accounts ')
        print('dl - Delete a saved account ')
        print('ex - Exit from the account')

        short_code = input().lower()

        if short_code == 'nc':
            print('Add a new social account credentials')
            print("-"*20)

            print('What is your new Social Account Name? ...')
            accountname = input()
            print("-"*20)

            print('What is your username in the Social Account Name...')
            account_username= input()
            print("-"*20)
                
            print ('\n')
            print('Do you want to :")1.cp - To create your own password or 2.gp - To get the password generated for you')
               
            short_code1 = input().lower()
            if short_code1 == 'cp':
                print('Input your password....')
                account_password = input()

                print(f'Your accountpassword is: {account_password}')
            elif short_code1 == 'gp':
                account_password = create_password()
                print(f'Your accountpassword is: {account_password}')

            else:
                print('Invalid short code') 

            save_new_creds(new_creds(accountname,account_username,account_password))
            print(f'{accountname} account credentials have been saved and stored')
            
        elif short_code == 'ec':
                    print('Add your existing account credentials')
                    print("-"*30)

                    print('Social Account Name ...')
                    accountname = input()

                    print('Username...')
                    account_username = input()

                    print('Password...')
                    account_password= input()

                    save_new_creds(new_creds(accountname,account_username,account_password))
                    print(f'{accountname} You account password has being saved and safely stored')
                
        elif short_code == 'da':
                    if display_new_creds():
                        print("Here is a list of all the accounts you  have saved in the application.") 
                        print("-"*30)   

                        for credentials  in display_new_creds():
                            print(
                            f"{credentials.account_name} {credentials.account_username} {credentials.account_password}"
                        )
                            print('\n')    
                    else:
                        print('\n')
                        print('You do not have any social account credentials saved')       
                        print('\n')

        elif short_code == 'dl':
                    print('Enter username for account you want to delete?')

                    account = input()       
                    found_account=find_new_creds(account)
                 
                    delete_new_creds(found_account)

        elif short_code == 'ex':
                    print('Bye! Come back soon!.')    
        else:
                    print('Wrong short code! Try again')

        break
        
    
            
            
         
        
                       


if __name__ ==  '__main__':
    main()


