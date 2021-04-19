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



class contact_us(unittest.TestCase):
    baseURL = 'http://automationpractice.com/'

    email = 'haylam630@gmail.com'
    subjectHeading = 'Customer service'
    orderReference = 'Order Reference'
    message = 'test'
    allertSucess = 'Your message has been successfully sent to our team.'
    file = r"C:\Users\Quang Hiep\Documents\Lotus Quality Assurance\Lotus Quality Assurance\LQA- Selenium_Python\Training Course _Selenium _LQA\automationPractice\files\data.txt"

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
        homePage.clickContactUs()
        contactUs.selectSubjectHeading(self.subjectHeading)
        contactUs.setEmailAdress(self.email)
        contactUs.setOrderReference(self.orderReference)
        contactUs.setMessage(self.message)
        contactUs.attachFile(self.file)
        time.sleep(2)
        contactUs.clickSend()
        time.sleep(5)
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


if __name__ == '__main__':
    unittest.main()
