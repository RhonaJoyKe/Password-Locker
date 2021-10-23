import unittest
from credentials import Creds
class TestCreds(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours
    '''
    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_cred= Creds("Twitter","Roro","46677")
    
    def test_init(self):
        '''
        tests if the object is initialized properly
        '''
        self.assertEqual(self.new_cred.account_name,"Twitter")
        self.assertEqual(self.new_cred.account_username,"Roro")
        self.assertEqual(self.new_cred.account_password,"46677")
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Creds.user_accounts = []
    