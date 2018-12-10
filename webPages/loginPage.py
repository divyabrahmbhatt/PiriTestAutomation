'''
List of actions used for login tests
'''
from selenium.webdriver.common.keys import Keys
from resources.testInputDataWeb import inputData
from PageObject.Pages.loginPageObj import Login
from selenium.webdriver.common.by import By
from PageObject.Locators import locator
import random
def loginWithIncorrectCredentials(self):
    login=Login(self.driver)
    (login.userNameObj).send_keys(inputData.userName+str(random.randint(0,9)))
    (login.passwordObj).send_keys(inputData.password)
    (login.passwordObj).send_keys(Keys.RETURN)
    
    self.assertTrue((self.driver.find_element(By.XPATH, locator.invalidCredentialsMessageObjProperty)).is_displayed())