import unittest
from user import User
class TestUser(unittest.TestCase):
    '''Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
     '''
    # The setUp() method allows us to define instructions that will be executed before each test method.
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
    #  self.assertEqual() this is a TestCase method that checks for an expected result. The first argument is the expected result and the second argument is the result that is actually gotten.
        self.assertEqual(self.new_user.first_name,"Rhona")
        self.assertEqual(self.new_user.last_name,"Koome")
        self.assertEqual(self.new_user.phone_number,"0706555078")
        self.assertEqual(self.new_user.email,"rhonajoy8@gmail.com")
        self.assertEqual(self.new_user.username,"Jojo")
        self.assertEqual(self.new_user.password,"12345")

    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Rhona","Koome","0706555078","rhonajoy8@gmail.com","Jojo","12345") # create user object

    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []


    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            proto_user = User("Test","user","0712345678","test@user.com","lnk","trhj89") # new contact
            proto_user.save_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.user_list),1) 
    
    def test_find_by_username(self):
        '''
        test to check if we can find a user by username and display information
        '''

        # self.new_contact.save_contact()
        # test_contact = User("Test","user","0711223344","test@user.com") # new contact
        # test_contact.save_contact()

        found_contact = User.find_by_username("Jojo")
    
    def test_check_user(self):

        self.found_user = User.check_user("Jojo","466777")

if __name__ ==  '__main__':
    unittest.main()