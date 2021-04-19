import unittest
import HtmlTestRunner
from selenium import webdriver
import os
import sys
import time
import random
PRV1_DIR = os.path.dirname(os.path.abspath(__file__)) #Get the root directory of currently file
PRV2_DIR = os.path.dirname(os.path.abspath(PRV1_DIR)) #Get the root directory of PRV1
ROOT_DIR= os.path.dirname(os.path.abspath(PRV2_DIR))  #Get the root directory of PRV2
sys.path.append(ROOT_DIR) #Locate the root directory
from pageObjects.loginPage import LoginPage
from pageObjects.createAccountPage import CreateAccountPage
from pageObjects.homePage import HomePage

class createAccountTest(unittest.TestCase):
    baseURL = 'http://automationpractice.com/'
    emailCreate_fail = 'abc123'
    emailCreate_successfull = 'testselenium'+ str(random.randint(0, 1900)) +'@gmail.com'
    invalidEmailCreate_message = 'Invalid email address.'
    firstName = 'Alexander'
    lastName = 'Rooney'
    password = '123456'
    address = '135 NewYork'
    postalCode = '01900'
    city = 'California'
    state = 'Alaska'
    phone = '0947888888'
    aliasAdress = 'Hanoi, Vietnam'
    myAccountPage_title = 'My account - My Store'

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(cls.baseURL)
    def test_CreateAccount_Error(self):
        loginPage = LoginPage(self.driver)
        homePage = HomePage(self.driver)
        homePage.clickSignIn()
        loginPage.setEmail_Create(self.emailCreate_fail)
        loginPage.clickSubmit_Create()
        time.sleep(5)
        # Check the Invalid Email Message (Create Account)
        self.assertEqual(self.invalidEmailCreate_message,loginPage.getCreateAccountError_messages(),"Error Message is not match!")
    def test_CreateAccount_Successfull(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        createAccount = CreateAccountPage(self.driver)
        homePage.clickSignIn()
        loginPage.setEmail_Create(self.emailCreate_successfull)
        loginPage.clickSubmit_Create()
        time.sleep(5)
        # Select(self.driver.find_element_by_id('s')).select_by_visible_text()
        createAccount.setFirstName(self.firstName)
        createAccount.setLastName(self.lastName)
        createAccount.setPassword(self.password)
        createAccount.setAddress(self.address)
        createAccount.setCity(self.city)
        createAccount.selectState(self.state)
        createAccount.setPostalCode(self.postalCode)
        createAccount.setPhone(self.phone)
        createAccount.setAliasAdress(self.aliasAdress)
        createAccount.clickRegister()

        self.assertEqual(self.myAccountPage_title,self.driver.title,"Create Account Uncessfully")



    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output= ROOT_DIR + '/reports'))