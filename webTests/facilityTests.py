'''
Verify facility functionality works as expected with positive and negative cases
'''
import unittest
from genericHelper.environmentSetup import EnvironmentSetup

class facilityTestCase(EnvironmentSetup):

    def test_demo1(self):
        self.assertTrue(True)
    def test_demo2(self):
        self.assertTrue(True)
    def test_failtest(self):
        self.assertTrue(False)
        
if __name__=='__main__':
    unittest.main()