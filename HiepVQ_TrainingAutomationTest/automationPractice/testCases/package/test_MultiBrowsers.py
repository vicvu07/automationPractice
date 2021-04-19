# # import pytest
# #
# # from selenium import webdriver
# #
# # from selenium.webdriver.chrome.options import Options
# #
# # from selenium.webdriver.opera.options import Options
# #
# # from selenium.webdriver.common.keys import Keys
# #
# # from time import sleep
# # import os
# #
# # PRV1_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the root directory of currently file
# # PRV2_DIR = os.path.dirname(os.path.abspath(PRV1_DIR))  # Get the root directory of PRV1
# # ROOT_DIR = os.path.dirname(os.path.abspath(PRV2_DIR))  # Get the root directory of PRV2
# #
# #
# # @pytest.fixture(params=["chrome", "firefox", "opera"], scope="class")
# #
# #
# # def driver_init(request):
# #     if request.param == "chrome":
# #         # Local webdriver implementation
# #         web_driver = webdriver.Chrome(executable_path = ROOT_DIR + '\drivers\chromedriver.exe')
# #     if request.param == "firefox":
# #         # Local webdriver implementation
# #         web_driver = webdriver.Firefox(executable_path=ROOT_DIR + '\drivers\geckodriver.exe')
# #
# #
# #     # if request.param == "opera":
# #     #     # Local webdriver implementation
# #     #     options = Options()
# #     #     # Setting the location of the Opera Browser
# #     #     options.binary_location = r' location_of_opera.exe'
# #     #     # Creation of Opera WebDriver instance
# #     #     web_driver = webdriver.Opera(options=options,
# #     #                                  executable_path=r' location_of_operadriver.exe')
# #     request.cls.driver = web_driver
# #     yield
# #     web_driver.close()
# #
# #
# # @pytest.mark.usefixtures("driver_init")
# # class BasicTest:
# #     pass
# #
# #
# # class Test_URL(BasicTest):
# #     def test_open_url(self):
# #         self.driver.get("https://www.lambdatest.com/")
# #         print(self.driver.title)
# #         sleep(5)
#
# import pytest
# import unittest
# from selenium import webdriver
#
#
# # class TestMulti():
#     # @pytest.mark.parametrize('x', [1, 2])
#     # def get_par(x):
#     #     y = x
#     #     return y
#     #
#     # def setUp(self):
#     #     x = self.get_par()
#     #     print('=============', x)
#     #     # if x == 1:
#     #     self.driver = webdriver.Chrome(executable_path=r'C:\Drivers\chromedriver_win32\chromedriver.exe')
#     #     self.driver.maximize_window()
#     #     # elif x == 2:
#     #     # self.driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver-v0.29.0-win64\geckodriver.exe')
#     #     # self.driver.maximize_window()
#     #
#     # def test_method(self):
#     #     self.driver.get('https://google.com')
#     #     assert True
#
# # import pytest
# @pytest.mark.parametrize('x',[1,2])
# def test_asssert(x):
#     print(x)
#     if x == 1:
#         assert True
#     else:
#         assert False
#
import unittest
import pytest, time
from selenium import webdriver
from parameterized import parameterized, parameterized_class
# from testCases.package.conftest import config_test


class Test_MultiBrowser(unittest.TestCase):

    #
    # def initialize(self,x):
    #     if x == 'chrome':
    #         self.driver = webdriver.Chrome(executable_path=r'C:\Drivers\chromedriver_win32\chromedriver.exe')
    #         self.driver.maximize_window()
    #         self.driver.get('http://www.google.com')
    #
    #     else:
    #         self.driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver-v0.29.0-win64\geckodriver.exe')
    #         self.driver.maximize_window()
    #         self.driver.get('http://www.facebook.com')
    #     return self.driver

    @parameterized.expand(['chrome', 'firefox'])
    def test_run(self, x):
        if x == 'chrome':
            self.driver = webdriver.Chrome(executable_path=r'C:\Drivers\chromedriver_win32\chromedriver.exe')
            self.driver.maximize_window()
            self.driver.get('http://www.twitter.com')
            time.sleep(2)
            self.driver.get('http://www.google.com')


        else:
            self.driver = webdriver.Firefox(executable_path=r'C:\Drivers\geckodriver-v0.29.0-win64\geckodriver.exe')
            self.driver.maximize_window()
            self.driver.get('http://www.facebook.com')

        title = self.driver.title
        if title == 'Google':
            assert True
            self.driver.quit()

        else:
            self.driver.quit()
            assert False
        # time.sleep(5)
        # time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
