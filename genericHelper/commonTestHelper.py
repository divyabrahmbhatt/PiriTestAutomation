'''
Common helping functions 
'''
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from PageObject.Pages.loginPageObj import Login
from PageObject.Pages.homePageObj import Home
from selenium.webdriver.common.by import By
from PageObject.Locators import locator
from resources.testInputDataWeb import inputData

def webLogin(self):
    login=Login(self.driver)
    wait = ui.WebDriverWait(self.driver,10)
    (login.userNameObj).send_keys(inputData.userName)
    (login.passwordObj).send_keys(inputData.password)
    (login.passwordObj).send_keys(Keys.RETURN)
    wait.until(lambda driver: driver.find_element_by_class_name("icon-home"))
    self.assertTrue((self.driver.find_element(By.CSS_SELECTOR, locator.userIconObjProperty)).is_displayed())
    
def logout(self):
    home=Home(self.driver)
    (home.userIconObj).click()
    (home.logoutObj).click()
    assert locator.homePageTitle in self.driver.title