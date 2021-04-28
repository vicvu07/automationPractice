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
from pageObjects.productDetailPage import ProductDetailPage
from pageObjects.searchPage import SearchPage


class home_page(unittest.TestCase):
    baseURL = 'http://automationpractice.com/'
    # driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
    newsletteremail = 'haylam630' + str(random.randint(0, 19000)) + '@gmail.com'
    allertSuccess = 'Newsletter : You have successfully subscribed to this newsletter.'
    keyword = 'dress'
    keyword_fail = 'dresSSss'
    placehoder = 'Search'

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(cls.baseURL)

    def test_NewsletterSubmit(self):
        homePage = HomePage(self.driver)
        homePage.setNewsletterEmai(self.newsletteremail)
        homePage.clickSubmitNewsletter()
        time.sleep(5)
        self.assertEqual(self.allertSuccess, homePage.getAllertSuccess(), "Submit newsletter emai unsuccesfully!")

    def test_TypeSearchKeyWord(self):
        homePage = HomePage(self.driver)
        homePage.setSearchKeyword(self.keyword)
        time.sleep(5)
        self.assertEqual(self.keyword, homePage.getSearchKeyword(), "Do not automatically delete placeholder!")
        homePage.clearSearchKeyWord()
        time.sleep(5)
        self.assertEqual(self.placehoder, homePage.getSearchPlaceHolder(), 'Placeholder is not match')

    def test_SuggestKeyWord(self):
        homePage = HomePage(self.driver)

        #truyền keyword
        homePage.setSearchKeyword(self.keyword)
        time.sleep(5)
        suggestKeyWords_list = homePage.getAllSuggestKeyWords()
        for suggestKeyword in suggestKeyWords_list:
            self.assertIn(self.keyword, suggestKeyword.lower(), 'Suggest keyword is not suitable!')

    def test_SuitableProductDetail(self):
        homePage = HomePage(self.driver)
        productDetail = ProductDetailPage(self.driver)
        homePage.setSearchKeyword(self.keyword)
        time.sleep(5)
        suggestKeyWords_list = homePage.getAllSuggestKeyWords()
        suggestKeyword_index = 0
        for suggestKeyword in suggestKeyWords_list:
            suggestKeyword_index += 1
            suggestKeyword_text = homePage.getSuggestKeyWord('[' + str(suggestKeyword_index) + ']')
            homePage.clickSuggestKeyWord('[' + str(suggestKeyword_index) + ']')
            productTitle = productDetail.getProductTitle()
            time.sleep(5)
            self.assertIn(productTitle, suggestKeyword_text, 'Product tille is not match!')
            if suggestKeyword_index < len(suggestKeyWords_list):
                homePage.setSearchKeyword(self.keyword)
                time.sleep(5)
            else:
                break

    def test_ProductQuantity(self):
        homePage = HomePage(self.driver)
        time.sleep(2)
        homePage.setSearchKeyword(self.keyword)
        homePage.clickSearchButton()
        time.sleep(5)
        searchPage = SearchPage(self.driver)
        searchResultMessage = searchPage.getSearchResultMessage().split()
        productQuantityMessage = int(searchResultMessage[0])
        productsResultQuantity = searchPage.getProductsResultQuantity()
        self.assertEqual(productQuantityMessage, productsResultQuantity,
                         'The reality quantity of products result is not match with message!')

    def test_ProductPrice(self):
        homePage = HomePage(self.driver)
        time.sleep(2)
        homePage.setSearchKeyword(self.keyword)
        homePage.clickSearchButton()
        time.sleep(5)
        searchPage = SearchPage(self.driver)
        allProductResult = searchPage.getAllProductsResult()
        for i in range(1, len(allProductResult) + 1):
            productPrice = searchPage.getProductPrice(i)
            self.assertNotEqual('', productPrice, "Product price is empty!")

    def test_Search_fail(self):
        homePage = HomePage(self.driver)
        searchPage = SearchPage(self.driver)
        time.sleep(2)
        homePage.setSearchKeyword(self.keyword_fail)
        homePage.clickSearchButton()
        time.sleep(5)
        searchNoResultMessage = searchPage.getSearchNoResultMessage()
        self.assertIn('No results were found for your search', searchNoResultMessage, 'Something went wrong!')

    @classmethod
    def tearDown(cls):
        time.sleep(2)
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
