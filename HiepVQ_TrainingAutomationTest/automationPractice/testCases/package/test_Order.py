import unittest
import HtmlTestRunner
from selenium import webdriver
import os
import sys
import time

PRV1_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the root directory of currently file
PRV2_DIR = os.path.dirname(os.path.abspath(PRV1_DIR))  # Get the root directory of PRV1
ROOT_DIR = os.path.dirname(os.path.abspath(PRV2_DIR))  # Get the root directory of PRV2
sys.path.append(ROOT_DIR)  # Locate the root directory
from pageObjects.homePage import HomePage
from pageObjects.checkOutPage import CheckOutPage
from pageObjects.loginPage import LoginPage
from pageObjects.productDetailPage import ProductDetailPage


class TestOrder(unittest.TestCase):
    baseURL = 'http://automationpractice.com'
    emailSignIn = 'testselenium1542@gmail.com'
    passwordSignIn = '123456'

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)

    def test_order_successfully(self):
        # Feature: Mua hàng; Title: Mua thành công

        homePage = HomePage(self.driver)
        price = homePage.getPrice(1)
        homePage.add_product_and_continue(1)

        # Check total price off all products
        price += homePage.getPrice(2)
        homePage.add_product_and_continue(2)
        new_price = homePage.getPrice(3)
        price += homePage.getPrice(3)
        homePage.add_product_and_checkout(3)
        checkOutPage = CheckOutPage(self.driver)
        productsPrice = checkOutPage.get_products_price()
        self.assertEqual(float(price), productsPrice, 'Something went wrong!')

        # Proceed to checkout
        completeMessage = checkOutPage.proceed_to_checkout(self.emailSignIn, self.passwordSignIn)
        self.assertEqual('Your order on My Store is complete.', completeMessage, "Proceed to checkout unsuccesfully")

    # @unittest.skip('1')
    def test_change_and_order_successfully(self):
        # Feature: Mua hàng; Title: Thay đổi thông tin mua hàng

        # Check total price
        homePage = HomePage(self.driver)
        for i in range(1, 5):
            homePage.add_product_and_continue(i)
        homePage.add_product_and_checkout(5)
        checkOutPage = CheckOutPage(self.driver)
        checkOutPage.set_product_quantity(2, 3)
        checkOutPage.click_delete_product(3)
        time.sleep(10)
        price = 0
        for i in range(1, 5):
            price += checkOutPage.get_product_price(i)
        totalPrice = checkOutPage.get_products_price()
        self.assertEqual(price, totalPrice, "Total price was not suitable")

        # Proceed to checkout (without agree term of service)
        checkOutPage.click_proceed_to_check_out_summary_process()
        loginPage = LoginPage(self.driver)
        loginPage.sign_in(self.emailSignIn, self.passwordSignIn)
        checkOutPage.click_proceed_to_check_out_address_process()
        checkOutPage.click_proceed_to_check_out_shippingProcess_xpath()  # Click proceed to checkout without agree terms of service before
        termsAgreementWarning = checkOutPage.get_terms_agreement_warning()
        self.assertEqual('You must agree to the terms of service before continuing.', termsAgreementWarning,
                         'Terms Agreement warning is not match!')
        checkOutPage.close_terms_agreement_warning()  # Close terms agreement warnings
        checkOutPage.click_term_agreement()  # Click term agreement
        checkOutPage.click_proceed_to_check_out_shippingProcess_xpath()  # Click proceed to checkout with agree terms of service before
        checkOutPage.click_pay_by_bank_wire()
        checkOutPage.click_confirm_my_order()
        completeMessage = checkOutPage.get_complete_message()  # Get complete message
        self.assertEqual('Your order on My Store is complete.', completeMessage, "Proceed to checkout unsuccesfully")

    def test_promotion_product(self):
        # Feature: Mua hàng; Title: Mua đồ khuyến mãi
        # self.driver.get(self.baseURL)
        # time.sleep(3)
        homePage = HomePage(self.driver)
        checkOutPage = CheckOutPage(self.driver)
        totalProducts = homePage.getAllProducts()
        # Click product which has percent reduction is 20
        homePage.click_product_belongs_to_reduction(20)
        # Click add to cart
        product_detail_page = ProductDetailPage(self.driver)
        product_detail_page.click_add_to_cart()
        # Click Proceed to checkout
        homePage.click_proceed_to_checkout()
        checkOutPage.proceed_to_checkout(self.emailSignIn, self.passwordSignIn)
        completeMessage = checkOutPage.get_complete_message()
        self.assertEqual('Your order on My Store is complete.', completeMessage,
                         "Proceed to checkout unsuccesfully")

    def tearDown(sefl):
        time.sleep(2)
        sefl.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
