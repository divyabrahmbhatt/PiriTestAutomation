'''
Define object properties for home page
'''
from selenium.webdriver.common.by import By

class Home(object):
    
    def __init__(self,driver):
        self.driver=driver

#home Page locators and PageObject defining
        self.userIconObj = driver.find_element(By.CSS_SELECTOR, "[id*='userinfo'] i")
        self.logoutObj = driver.find_element(By.CSS_SELECTOR, ".logoff-link")   