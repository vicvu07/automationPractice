from locator.searchPage_locator import SearchPage_locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator.homePage_locator import HomePage_locator
from selenium.webdriver.common.by import By

class SearchPage:
    # Get locator
    locator = SearchPage_locator

    def __init__(self, driver):
        self.driver = driver

    def getSearchResultMessage(self):
        search_result_message = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.searchResultMessage_xpath))
        )
        return search_result_message.text

    def getAllProductsResult(self):
        all_products_result = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locator.allProductsResult_xpath))
        )
        return all_products_result

    def getProductsResultQuantity(self):
        return len(self.getAllProductsResult())

    def getProductPrice(self, index):
        # productPrice_fullXpath = self.locator.allProductsResult_xpath + '[' + str(index) + ']' + self.locator.productPrice_xpath
        productPrice_fullXpath = f'{self.locator.allProductsResult_xpath}[{index}]{self.locator.productPrice_xpath}'
        product_price = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, productPrice_fullXpath))
        )
        return product_price.text

    def getSearchNoResultMessage(self):
        searchNoResultMessage = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.searchNoResultMessage_xpath))
        )
        return searchNoResultMessage.text
