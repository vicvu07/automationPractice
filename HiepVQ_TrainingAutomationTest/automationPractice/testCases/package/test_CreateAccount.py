import unittest
import HtmlTestRunner
from selenium import webdriver
import os
import sys
import time
import random

PRV1_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the root directory of currently file
PRV2_DIR = os.path.dirname(os.path.abspath(PRV1_DIR))  # Get the root directory of PRV1
ROOT_DIR = os.path.dirname(os.path.abspath(PRV2_DIR))  # Get the root directory of PRV2
sys.path.append(ROOT_DIR)  # Locate the root directory
from pageObjects.loginPage import LoginPage
from pageObjects.createAccountPage import CreateAccountPage
from pageObjects.homePage import HomePage


class TestCreateAccount(unittest.TestCase):
    baseURL = 'http://automationpractice.com/'
    emailCreate_fail = 'abc123'
    emailCreate_successfull = 'testselenium' + str(random.randint(0, 1900)) + '@gmail.com'
    invalidEmailCreate_message = 'Invalid email address.'
    firstName = 'Alexander'
    lastName = 'Rooney'
    password = '123456'
    address = '135 NewYork'
    postalCode = '01900'
    city = 'California'
    state = 'Alaska'
    phone = '0947888888'
    aliasAddress = 'Hanoi, Vietnam'
    myAccountPage_title = 'My account - My Store'

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
        # cls.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

    def test_CreateAccount_Error(self):
        loginPage = LoginPage(self.driver)
        homePage = HomePage(self.driver)
        # Click Sign In button
        homePage.clickSignIn()
        # Typing email
        loginPage.setEmail_Create(self.emailCreate_fail)
        # Click Submit button
        loginPage.clickSubmit_Create()
        # Check the Invalid Email Message (Create Account)
        create_account_error_message = loginPage.getCreateAccountError_messages()
        self.assertEqual(self.invalidEmailCreate_message, create_account_error_message,
                         "Error Message is not match!")

    def test_CreateAccount_Successfull(self):
        homePage = HomePage(self.driver)
        loginPage = LoginPage(self.driver)
        createAccount = CreateAccountPage(self.driver)
        # Click Sign In Button
        homePage.clickSignIn()
        # Typing email
        loginPage.setEmail_Create(self.emailCreate_successfull)
        # Click button submit
        loginPage.clickSubmit_Create()

        # Typing personal information
        createAccount.setFirstName(self.firstName)
        createAccount.setLastName(self.lastName)
        createAccount.setPassword(self.password)
        createAccount.setAddress(self.address)
        createAccount.setCity(self.city)
        createAccount.selectState(self.state)
        createAccount.setPostalCode(self.postalCode)
        createAccount.setPhone(self.phone)
        createAccount.setAliasAdress(self.aliasAddress)
        createAccount.clickRegister()
        # Check status of creating account
        time.sleep(5)
        self.assertEqual(self.myAccountPage_title, self.driver.title, "Create Account Uncessfully")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=ROOT_DIR + '/reports'))
