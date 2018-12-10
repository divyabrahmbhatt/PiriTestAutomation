'''
Define object properties for login page
'''
from selenium.webdriver.common.by import By

class Login(object):
    
    def __init__(self,driver):
        self.driver=driver
        
#login page locators and PageObject defining
        self.userNameObj = driver.find_element(By.ID, "UserName")
        self.passwordObj = driver.find_element(By.ID, "Password")