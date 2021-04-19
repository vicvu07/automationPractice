# Run pytest in Terminal
# cd testCases/package
# pytest -n 2 test_productDetail_parallel.py


import unittest

from selenium import webdriver
import os
import sys
import time

PRV1_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the root directory of currently file
PRV2_DIR = os.path.dirname(os.path.abspath(PRV1_DIR))  # Get the root directory of PRV1
ROOT_DIR = os.path.dirname(os.path.abspath(PRV2_DIR))  # Get the root directory of PRV2
sys.path.append(ROOT_DIR)  # Locate the root directory
from pageObjects.homePage import HomePage
from pageObjects.productDetailPage import ProductDetailPage
from pageObjects.checkOutPage import CheckOutPage
from pageObjects.loginPage import LoginPage
from parameterized import parameterized, parameterized_class
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test_product_detail(unittest.TestCase):
    baseURL = 'http://automationpractice.com/'

    # driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')

    # @classmethod
    # def setUp(cls):
    #     cls.driver = webdriver.Chrome(executable_path=ROOT_DIR + '\drivers\chromedriver.exe')
    #     cls.driver.maximize_window()
    #     cls.driver.get(cls.baseURL)

    def get_result(self, productDetailPage):
        # Kiểm tra ảnh phóng to và tên sản phẩm hiển thị dưới ảnh

        image_viewLarge_status = productDetailPage.check_image_view_large_is_displayed()
        size_of_product_image = productDetailPage.get_size_of_product_image()
        size_of_view_large_image = productDetailPage.get_size_of_view_large_image()
        # Check size of image in view large mode
        if size_of_view_large_image > size_of_product_image:
            assert True
        else:
            assert False
        # Check the product title is after the image of view larger mode
        image_viewLarge_location_height = productDetailPage.get_location_view_large_image().get('y')
        product_title_location_height = productDetailPage.get_location_product_title().get('y')
        if product_title_location_height > image_viewLarge_location_height:
            assert True
        else:
            assert False

        time.sleep(5)

    #
    # # @unittest.skip('Not test this case!')
    @parameterized.expand(['chrome_LQA_PC', 'chrome'])
    def test_view_large_product_image(self, browser):
        # Thiết lập trình duyệt Chrome, Firefox

        if browser == 'chrome':
            self.driver = webdriver.Chrome(executable_path=r'C:\Drivers\chromedriver_win32\chromedriver.exe')
            # self.driver.maximize_window()
            # self.driver.get(self.baseURL)
            # self.driver.implicitly_wait(5)

        else:
            self.driver = webdriver.Remote(
                command_executor='http://10.10.31.79:4444/wd/hub',
                desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True, 'video': True})





        # Feature: Chi tiết sản phẩm; Title: Kiểm tra chức năng View Large

        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver)
        homePage.click_product_image(1)  # Click a image of the first product
        time.sleep(2)
        productDetailPage = ProductDetailPage(self.driver)
        productDetailPage.click_big_page()
        time.sleep(2)
        self.get_result(productDetailPage)

        # Feature: Chi tiết sản phẩm; Title: Kiểm tra chức năng View Large; Preconditional: Click vào button [Close] trên ảnh

        productDetailPage.click_close_view_larger()
        productDetailPage.click_view_larger_button()
        time.sleep(2)
        self.get_result(productDetailPage)

        # Feature: Chi tiết sản phẩm; Title: Add to cart với Quantity =0
        productDetailPage.click_close_view_larger()
        productDetailPage.set_product_quantity(0)
        time.sleep(2)
        productDetailPage.click_add_to_cart()
        time.sleep(2)
        null_quantity_message = productDetailPage.get_null_quantity_message()
        self.assertEqual('Null quantity.', null_quantity_message, "Null message is not match")

        # Feature: Chi tiết sản phẩm; Title: Add to cart với Quantity > 0
        productDetailPage.click_close_view_larger()
        productDetailPage.set_product_quantity(1)
        time.sleep(5)
        product_title = productDetailPage.getProductTitle()  # Get the title of the product
        productDetailPage.click_add_to_cart()  # Adding product to cart
        time.sleep(5)
        add_to_cart_successfully_message = productDetailPage.get_add_to_cart_successfully_message()
        time.sleep(5)
        self.assertEqual('Product successfully added to your shopping cart', add_to_cart_successfully_message,
                         'Message is not match!')
        productDetailPage.click_close_add_to_cart_successfully_message()
        productDetailPage.click_cart_button()
        time.sleep(2)
        checkOutPage = CheckOutPage(self.driver)
        product_title_cart = checkOutPage.get_product_title(1)
        product_quantity_cart = checkOutPage.get_product_quantity(1)
        self.assertEqual(product_title, product_title_cart, "Product title is not match!")
        self.assertEqual('1', product_quantity_cart, 'Product price is not match!')
        time.sleep(5)
        self.driver.quit()

# @unittest.skip('Not test this case!')
# @parameterized.expand(['chrome', 'firefox'])
# def test_share_to_twitter(self, browser):
#     # Thiết lập trình duyệt Chrome, Firefox
#     if browser == 'chrome':
#         self.driver = webdriver.Chrome(executable_path=r'C:\Drivers\chromedriver_win32\chromedriver.exe')
#         self.driver.maximize_window()
#         self.driver.get(self.baseURL)
#         self.driver.implicitly_wait(5)
#
#     else:
#         self.driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver-v0.29.0-win64\geckodriver.exe')
#         self.driver.maximize_window()
#         self.driver.get(self.baseURL)
#         self.driver.implicitly_wait(5)
#
#     # Feature: Chi tiết sản phẩm; Title: Share to TWitter
#     homePage = HomePage(self.driver)
#     homePage.click_product_image(1)
#     productDetailPage = ProductDetailPage(self.driver)
#     productDetailPage.click_tweet()
#     time.sleep(5)
#     window_after = self.driver.window_handles[1]
#     self.driver.switch_to.window(window_after)
#     self.assertTrue(productDetailPage.login_twitter('vicvu8', '123456aA@'))
#     time.sleep(5)
#     self.driver.quit()


# @unittest.skip('Not test this case!')
# @parameterized.expand(['chrome', 'firefox'])
# def test_write_a_comment(self,browser):
#     # Thiết lập trình duyệt Chrome, Firefox
#     if browser == 'chrome':
#         self.driver = webdriver.Chrome(executable_path=r'C:\Drivers\chromedriver_win32\chromedriver.exe')
#         self.driver.maximize_window()
#         self.driver.get(self.baseURL)
#         self.driver.implicitly_wait(5)
#
#     else:
#         self.driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver-v0.29.0-win64\geckodriver.exe')
#         self.driver.maximize_window()
#         self.driver.get(self.baseURL)
#         self.driver.implicitly_wait(5)
#     # Feature: Chi tiết sản phẩm; Title: Write a comment
#     emailSignIn = 'testselenium1542@gmail.com'
#     passwordSignIn = '123456'
#     homePage = HomePage(self.driver)
#     homePage.clickSignIn()
#     time.sleep(3)
#     loginPage = LoginPage(self.driver)
#     loginPage.sign_in(emailSignIn, passwordSignIn)
#     time.sleep(3)
#     self.driver.get(self.baseURL)
#     homePage.click_product_image(1)
#     time.sleep(3)
#     productDetailPage = ProductDetailPage(self.driver)
#     productDetailPage.leave_review('Comment', 'Good')
#     time.sleep(7)
#     send_review_message = productDetailPage.get_send_review_message()
#     self.assertEqual('Your comment has been added and will be available once approved by a moderator', send_review_message, "Send review unsuccessfully")
#
# # @unittest.skip('Not test this case!')
# @parameterized.expand(['chrome', 'firefox'])
# def test_send_to_a_friend(self,browser):
#     # Thiết lập trình duyệt Chrome, Firefox
#     if browser == 'chrome':
#         self.driver = webdriver.Chrome(executable_path=r'C:\Drivers\chromedriver_win32\chromedriver.exe')
#         self.driver.maximize_window()
#         self.driver.get(self.baseURL)
#         self.driver.implicitly_wait(5)
#
#     else:
#         self.driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver-v0.29.0-win64\geckodriver.exe')
#         self.driver.maximize_window()
#         self.driver.get(self.baseURL)
#         self.driver.implicitly_wait(5)
# # Feature: Chi tiết sản phẩm; Title:Send to friend
#     homePage = HomePage(self.driver)
#     homePage.click_product_image(1)
#     productDetailPage = ProductDetailPage(self.driver)
#     productDetailPage.click_send_to_a_friend()
#     productDetailPage.set_friend_name('Alexander')
#     productDetailPage.set_friend_email('selenium@gmail.com')
#     productDetailPage.send_to_a_friend()
#     time.sleep(5)
#     send_to_a_friend_message = productDetailPage.get_send_to_a_friend_message()
#     self.assertEqual('Your e-mail has been sent successfully', send_to_a_friend_message, "Send to a friend unsuccessfully!")


# @classmethod
# def tearDown(cls):
#     time.sleep(2)
#     cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
