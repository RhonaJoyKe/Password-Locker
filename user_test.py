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
        self.assertEqual(self.new_user.password,"12345")

    
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Rhona","Koome","0706555078","rhonajoy8@gmail.com","12345") # create contact object

    
    
    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ ==  '__main__':
    unittest.main()