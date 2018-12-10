'''
Mention input require for different tests
'''
class inputData():
#config Data
    browser=""
    screenshot_dir="ScreenShots/"
    reports_dir="Reports/"
#add comma separated environment on which tests will get executed sequentially  
    environment="eng"
    userName=""
    password=""
    envURL=""
#Make sure the environment details are prefix with the environment name given in environment
    prod_userName="prodUser"
    prod_password="Orofii@-1@39"
    prod_envURL="https://eng.lunera.com/"
    eng_userName="Divya"
    eng_password="Orofii@-1@39"
    eng_envURL="https://eng.lunera.com/"