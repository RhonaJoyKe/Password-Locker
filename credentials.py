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

    def save_creds(self):
        '''
        save_user method saves user objects into user_list
    '''
        Creds.user_accounts.append(self)
    
