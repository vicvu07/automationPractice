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
import library.control_excel_files


class createAccountTest(unittest.TestCase):
    baseURL = 'http://automationpractice.com/'
    emailCreate_fail = 'abc123'
    invalidEmailCreate_message = 'Invalid email address.'
    myAccountPage_title = 'My account - My Store'

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(cls.baseURL)

    def test_CreateAccount_Successfull(self):

        createAccount_path = f'{ROOT_DIR}/files/createAccount.xlsx'
        rows = library.control_excel_files.getRowCount(createAccount_path)
        # Read data from dataset and register all accounts
        for row in range(2, rows + 1):
            time.sleep(5)
            self.email = f'{library.control_excel_files.readData(createAccount_path, row, "email")}@gmail.com'
            self.firstName = library.control_excel_files.readData(createAccount_path, row, 'firstName')
            self.lastName = library.control_excel_files.readData(createAccount_path, row, 'lastName')
            self.password = library.control_excel_files.readData(createAccount_path, row, 'password')
            self.address = library.control_excel_files.readData(createAccount_path, row, 'address')
            self.postalCode = library.control_excel_files.readData(createAccount_path, row, 'postalCode')
            self.city = library.control_excel_files.readData(createAccount_path, row, 'city')
            self.state = library.control_excel_files.readData(createAccount_path, row, 'state')
            self.phone = library.control_excel_files.readData(createAccount_path, row, 'phone')
            self.aliasAdress = library.control_excel_files.readData(createAccount_path, row, 'aliasAdress')
            homePage = HomePage(self.driver)
            loginPage = LoginPage(self.driver)
            createAccount = CreateAccountPage(self.driver)
            homePage.clickSignIn()
            loginPage.setEmail_Create(self.email)
            loginPage.clickSubmit_Create()
            time.sleep(5)
            # Select(self.driver.find_element_by_id('s')).select_by_visible_text()
            try:
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
                    library.control_excel_files.writeData(createAccount_path, row, 'Status',
                                                          'Create account Successfully!')
                else:
                    print()
            except:

                # Get message of error
                message = loginPage.getCreateAccountError_messages()
                # Write status of creating the account
                library.control_excel_files.writeData(createAccount_path, row, 'Status', message)

            time.sleep(5)
            self.driver.get(self.baseURL)
            time.sleep(5)

    @classmethod
    def tearDown(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=ROOT_DIR + '/reports'))
