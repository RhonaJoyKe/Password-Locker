class User:
    """
    Class that generates new 
    instances of user accounts.
    """
    user_list = [] 
    def __init__ (self,first_name,last_name,phone_number,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.password= password

    def save_user(self):

        '''
        save_user method saves contact objects into user_list
        '''

        User.user_list.append(self)
