'''
Mention number of tests to get run under the defined category
'''
from HtmlTestRunner import HTMLTestRunner
from webTests.loginTests import loginTestCase
from webTests.facilityTests import facilityTestCase
from unittest import TestLoader, TestSuite
from resources.testInputDataWeb import inputData
import sys
env=inputData.environment
totalEnv=env.split(",")
suiteName="sanitySuite"
for environment in totalEnv:
    #set environment details as per the given env
 
    inputData.userName=eval("inputData."+environment+"_userName")
    inputData.password=eval("inputData."+environment+"_password")
    inputData.envURL=eval("inputData."+environment+"_envURL")
    
    #load test cases to loader
    login_tests = TestLoader().loadTestsFromTestCase(loginTestCase)
    facility_tests = TestLoader().loadTestsFromTestCase(facilityTestCase)
    
    #create suite with selection of testcase classes
    sanitySuite = TestSuite([login_tests])
    demoSuite = TestSuite([login_tests])
    
    runner = HTMLTestRunner(output='testReprot')
    if(len(sys.argv) > 1):
        suiteName=' '.join(sys.argv[1:])
    runner.run(eval(suiteName))