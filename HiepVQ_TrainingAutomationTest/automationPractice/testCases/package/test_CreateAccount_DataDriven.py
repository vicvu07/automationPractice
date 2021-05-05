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
from pageObjects.base_page import ControlExelFile


class createAccountTest(unittest.TestCase):
    baseURL = 'http://automationpractice.com/'
    emailCreate_fail = 'abc123'
    invalidEmailCreate_message = 'Invalid email address.'
    myAccountPage_title = 'My account - My Store'

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

    def test_CreateAccount_Successfull(self):

        createAccount_path = f'{ROOT_DIR}/files/createAccount.xlsx'

        rows = ControlExelFile.getRowCount(createAccount_path)
        # Read data from dataset and register all accounts
        for row in range(2, rows + 1):
            #Get information from excel file
            self.email = f'{ControlExelFile.readData(createAccount_path, row, "email")}@gmail.com'
            self.firstName = ControlExelFile.readData(createAccount_path, row, 'firstName')
            self.lastName = ControlExelFile.readData(createAccount_path, row, 'lastName')
            self.password = ControlExelFile.readData(createAccount_path, row, 'password')
            self.address = ControlExelFile.readData(createAccount_path, row, 'address')
            self.postalCode = ControlExelFile.readData(createAccount_path, row, 'postalCode')
            self.city = ControlExelFile.readData(createAccount_path, row, 'city')
            self.state = ControlExelFile.readData(createAccount_path, row, 'state')
            self.phone = ControlExelFile.readData(createAccount_path, row, 'phone')
            self.aliasAdress = ControlExelFile.readData(createAccount_path, row, 'aliasAdress')
            homePage = HomePage(self.driver)
            loginPage = LoginPage(self.driver)
            createAccount = CreateAccountPage(self.driver)
            homePage.clickSignIn()
            loginPage.setEmail_Create(self.email)
            loginPage.clickSubmit_Create()
            # Select(self.driver.find_element_by_id('s')).select_by_visible_text()
            try:
                # Typing personal information
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
                time.sleep(5)
                # Write status of creating the account
                if self.driver.title == self.myAccountPage_title:
                    ControlExelFile.writeData(createAccount_path, row, 'Status',
                                              'Create account Successfully!')
                else:
                    print()
            except:

                # Get message of error
                message = loginPage.getCreateAccountError_messages()
                # Write status of creating the account
                ControlExelFile.writeData(createAccount_path, row, 'Status', message)
            try:
                createAccount.log_out()
            except:
                self.driver.get(self.baseURL)


    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=ROOT_DIR + '/reports'))
