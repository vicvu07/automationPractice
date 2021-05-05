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


class TestHomePage(unittest.TestCase):
    baseURL = 'http://automationpractice.com/'
    # driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
    newsletteremail = 'haylam630' + str(random.randint(0, 19000)) + '@gmail.com'
    allertSuccess = 'Newsletter : You have successfully subscribed to this newsletter.'
    keyword = 'dress'
    keyword_fail = 'dresSSss'
    placehoder = 'Search'

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

    def test_NewsletterSubmit(self):
        homePage = HomePage(self.driver)
        # Set Newsletter email
        homePage.setNewsletterEmail(self.newsletteremail)
        # Click Submit button
        homePage.clickSubmitNewsletter()
        # Check submit in Newsletter successfully
        self.assertEqual(self.allertSuccess, homePage.getAllertSuccess(), "Submit newsletter emai unsuccesfully!")

    def test_TypeSearchKeyWord(self):
        homePage = HomePage(self.driver)
        # Send keyword to the input field
        homePage.setSearchKeyword(self.keyword)
        # Check the search Keyword after typing
        self.assertEqual(self.keyword, homePage.getSearchKeyword(), "Do not automatically delete placeholder!")
        homePage.clearSearchKeyWord()
        # Check the placeholder after clearing the search keyword
        self.assertEqual(self.placehoder, homePage.getSearchPlaceHolder(), 'Placeholder is not match')

    def test_SuggestKeyWord(self):
        homePage = HomePage(self.driver)
        # Type keyword
        homePage.setSearchKeyword(self.keyword)
        # Get all suggest keywords
        suggestKeyWords_list = homePage.getAllSuggestKeyWords()
        # Check all suggest keywords
        for suggestKeyword in suggestKeyWords_list:
            self.assertIn(self.keyword, suggestKeyword.lower(), 'Suggest keyword is not suitable!')

    def test_SuitableProductDetail(self):
        homePage = HomePage(self.driver)
        productDetail = ProductDetailPage(self.driver)
        # Type keywords
        homePage.setSearchKeyword(self.keyword)
        # Get all suggest keywords
        suggestKeyWords_list = homePage.getAllSuggestKeyWords()
        suggestKeyword_index = 0
        for suggestKeyword in suggestKeyWords_list:
            suggestKeyword_index += 1
            # Get single suggest keyword
            suggestKeyword_text = homePage.getSuggestKeyWord(suggestKeyword_index)
            # Click single suggest keyword
            homePage.clickSuggestKeyWord(suggestKeyword_index)
            # Get the title of product in product detail page
            productTitle = productDetail.getProductTitle()
            # Compare the title of product to the suggest keyword clicked
            self.assertIn(productTitle, suggestKeyword_text, 'Product tille is not match!')
            # Typing keyword again after compare the previous result
            if suggestKeyword_index < len(suggestKeyWords_list):
                homePage.setSearchKeyword(self.keyword)
            else:
                break

    def test_ProductQuantity(self):
        homePage = HomePage(self.driver)
        # Typing keyword
        homePage.setSearchKeyword(self.keyword)
        # Click search button
        homePage.clickSearchButton()
        searchPage = SearchPage(self.driver)
        # Get result message after searching
        searchResultMessage = searchPage.getSearchResultMessage().split()
        # Get product quantity in result message
        productQuantityMessage = int(searchResultMessage[0])
        # Get quantity of products
        productsResultQuantity = searchPage.getProductsResultQuantity()
        # Compare quantity of products to product quantity in result message
        self.assertEqual(productQuantityMessage, productsResultQuantity,
                         'The reality quantity of products result is not match with message!')

    def test_ProductPrice(self):
        homePage = HomePage(self.driver)
        # Typing keyword
        homePage.setSearchKeyword(self.keyword)
        # Click Search Button
        homePage.clickSearchButton()
        searchPage = SearchPage(self.driver)
        # Get all products result
        allProductResult = searchPage.getAllProductsResult()
        for i in range(1, len(allProductResult) + 1):
            productPrice = searchPage.getProductPrice(i)
            # Check the existence of product price
            self.assertNotEqual('', productPrice, "Product price is empty!")

    def test_Search_fail(self):
        homePage = HomePage(self.driver)
        searchPage = SearchPage(self.driver)
        # Typing keyword
        homePage.setSearchKeyword(self.keyword_fail)
        # Click search button
        homePage.clickSearchButton()
        # Get message when there is no result
        searchNoResultMessage = searchPage.getSearchNoResultMessage()
        self.assertIn('No results were found for your search', searchNoResultMessage, 'Something went wrong!')

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
