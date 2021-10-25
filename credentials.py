class Creds:
    '''
    Class that generates new 
    instances of the different social  accounts
    '''
    user_accounts=[]
    def __init__ (self,account_name,account_username,account_password):     
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    def save_account(self):
        '''
        save_user method saves account objects into user_list
    '''
        Creds.user_accounts.append(self)
    
    def delete_account(self):
        '''
        delete_account method delets account objects from user_accounts

        '''
        Creds.user_accounts.remove(self)
    
    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''

        for creds in cls.user_accounts:
            if creds.account_name == account_name:
                return creds
        return False


    @classmethod
    def display_accounts(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_accounts
    
    
