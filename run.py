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
        print("Use these short codes : na - create a new account,lg-login into account,  ex -exit the password locker list ")

        short_code = input().lower()

        if short_code == 'na':
                            print("New Account")
                            print("-"*50)

                            print ("Please Enter your First name ....")
                            first_name = input()

                            print("Please Enter your Last name ...")
                            last_name = input()

                           

                            print("Please Enter your Username ...")
                            username = input()

                            print("Please Enter your Password ...")
                            password = input()
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
            if username != 'Jojo' and password!= '12345':
                    print('The account does not exist, please create an account')
            else:
                    print(f'Hello {username}. This is your password locker account, Welcome!')
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

                print('What is your username in the Social Account Name...')
                account_username= input()
                
                print ('\n')
                print('Do you want to :1.cp - To create your own password or 2.gp - To get the password generated for you')
               
                short_code1 = input().lower()
                if short_code1 == 'cp':
                    account_password = create_password()
                    print(password)
                elif short_code1 == 'gp':
                    print('Input your password....')
                    account_password = input()
                else:
                    print('Invalid short code')     
                save_new_creds(new_creds(accountname,account_username,account_password))
                   
                print(f'{accountname} account credentials have been saved and stored')
            
        elif short_code == 'esc':
                print('Add your existing account credentials')
                print("-"*30)

                print('Social Account Name ...')
                accountname = input()

                print('Username...')
                username = input()

                print('Password...')
                password = input()

                save_social_account(create_new_account(accountname,username,password))
                print(f'{accountname} You account password has being saved and safely stored')
                
        elif short_code == 'dsc':
                if display_accounts():
                    print("Here is a list of all the accounts you  have saved in the application.") 
                    print("-"*30)   

                    for account  in display_accounts():
                        print(
                            f"{account.account_name} {account.username} {account.password}"
                        )
                    print('\n')    
                else:
                    print('\n')
                    print('You do not have any social account credentials saved')       
                    print('\n')

        elif short_code == 'dl':
                print('Enter an account you want to delete?')

                deleted_account = input()       
                 
                delete_social_account(deleted_account)

        elif short_code == 'ex':
                print('Bye! Come back soon!.')    
        else:
                print('Wrong short code! Try again')
            
            # if find_new_user(username):  # check if user exists
            #     # check if password is correct
            #     if user_password (username, user_password):
            #         print("\n")
            #         print(f"Welcome back {username} ")
            #         print('*'*50)
            #         while True:
            #             print("Select an option below to continue: \n")
            #             print(
            #                 "1. Create a new credential\n2. View saved credentials\n3. Delete credentials\n4. Logout")
            #             print("\n")
         
        
                       


if __name__ ==  '__main__':
    main()


