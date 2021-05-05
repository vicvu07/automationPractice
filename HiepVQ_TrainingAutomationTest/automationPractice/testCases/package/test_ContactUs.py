import unittest
import pytest
import os
import sys
import time
from selenium import webdriver

PRV1_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the root directory of currently file
PRV2_DIR = os.path.dirname(os.path.abspath(PRV1_DIR))  # Get the root directory of PRV1
ROOT_DIR = os.path.dirname(os.path.abspath(PRV2_DIR))  # Get the root directory of PRV2
sys.path.append(ROOT_DIR)  # Locate the root directory
from pageObjects.contactUsPage import ContactUsPage
from pageObjects.homePage import HomePage



class TestContactUs(unittest.TestCase):
    baseURL = 'http://automationpractice.com/'

    email = 'haylam630@gmail.com'
    subjectHeading = 'Customer service'
    orderReference = 'Order Reference'
    message = 'test'
    allertSucess = 'Your message has been successfully sent to our team.'
    file = ROOT_DIR + r"\files\data.txt"

    # allertSuccess = 'Newsletter : You have successfully subscribed to this newsletter.'

    # def init_browser(self, browser):
    #     if browser == 'Chrome':
    #         self.driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
    #     else:
    #         self.driver = webdriver.Firefox(executable_path=ROOT_DIR + '\drivers\geckodriver.exe')
    #     self.driver.maximize_window()
    #     return self.driver

    def test_contact_us(self):

        self.driver = webdriver.Chrome(executable_path=r'C:\Drivers\chromedriver_win32\chromedriver.exe')
        self.driver.maximize_window()

        # self.driver = self.init_browser(browser)
        self.driver.get(self.baseURL)
        homePage = HomePage(self.driver)
        contactUs = ContactUsPage(self.driver)
        # Click Contact Us button
        homePage.clickContactUs()
        # Select subject heading in Contact Us Page
        contactUs.selectSubjectHeading(self.subjectHeading)
        # Typing email address
        contactUs.setEmailAdress(self.email)
        # Typing Order Reference
        contactUs.setOrderReference(self.orderReference)
        # Typing message
        contactUs.setMessage(self.message)
        # Attach File
        contactUs.attach_file_and_send(self.file)
        self.assertEqual(contactUs.getAllertSucess(), self.allertSucess, "Submit Message in Contact us unsucessfully!")

    # def test_ContactUs(self):
    #     arr = 'Chrome'
    #     arr2 = 'Firefox'
    #
    #     t1 = threading.Thread(target=contact_us.contact_us_method(arr), args=(arr,))
    #     # t2 = threading.Thread(target=contact_us, args=(arr2,))
    #     t1.start()
    #     # t2.start()
    #     t1.join()
    #     # t2.join()

    def tearDown(self):
       self.driver.quit()
if __name__ == '__main__':
    unittest.main()
