'''
Setting up the environment which is inherited ny every tests
'''
import unittest
import datetime
from selenium import webdriver
from resources.testInputDataWeb import inputData
import os

class EnvironmentSetup(unittest.TestCase):
#setup contains the browser setup attributes
    def setUp(self):
        self.driver =  webdriver.Chrome("chromedriver.exe")
        self.driver.get(inputData.envURL)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

#teardown method to close all the browser instances and then quit
    def tearDown(self):
        print("--------------------------------------------")
        print("Run complete")
        directoryScreenShot=inputData.screenshot_dir+datetime.datetime.today().strftime('%Y-%m-%d')
        if not os.path.exists(directoryScreenShot):
            os.makedirs(directoryScreenShot)
        self.driver.save_screenshot(directoryScreenShot+"/%s.png" % unittest.TestCase.id(self))
        self.driver.close()
        self.driver.quit()        