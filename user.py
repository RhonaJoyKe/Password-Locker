class User:
    """
    Class that generates new 
    instances of user accounts.
    """
    user_list = [] 
    def __init__ (self,first_name,last_name,username,password):
        self.first_name = first_name
        self.last_name = last_name
       
        self.username=username
        self.password= password

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    def delete_user(self):
        '''
        delete_user method deletes user objects from user_list

        '''
        User.user_list.remove(self)
    @classmethod
    def find_by_username(cls,username):
        '''
        Method that returns an username

        
        '''

        for user in cls.user_list:
            if user.username == username:
                return user
    @classmethod
    def check_user(cls, username, password):
        """
        Check if user exists and if password is correct
        """
        user = cls.find_by_username(username)
        if user and user.password == password:
            return True
        return False