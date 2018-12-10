'''
Verify login functionality works as expected with positive and negative cases
'''
import unittest
import genericHelper.commonTestHelper as helper
import webPages.loginPage as actions
from genericHelper.environmentSetup import EnvironmentSetup

class loginTestCase(EnvironmentSetup):

#Check if login from UI works with correct credentials
    def test_loginWithValidCredentials(self):
        helper.webLogin(self)
#Verify functionality for logout
    def test_logout(self):
        helper.webLogin(self)
        helper.logout(self)
#Verify proper validation message is shown for incorrect credentials       
    def test_loginWithInvalidCredentials(self):
        actions.loginWithIncorrectCredentials(self)
   
if __name__=='__main__':
    unittest.main()