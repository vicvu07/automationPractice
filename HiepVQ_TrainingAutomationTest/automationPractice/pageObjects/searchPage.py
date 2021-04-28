from locator.searchPage_locator import SearchPage_locator


class SearchPage:
    # Get locator
    locator = SearchPage_locator

    def __init__(self, driver):
        self.driver = driver

    def getSearchResultMessage(self):
        return self.driver.find_element_by_xpath(self.locator.searchResultMessage_xpath).text

    def getAllProductsResult(self):
        return self.driver.find_elements_by_xpath(self.locator.allProductsResult_xpath)

    def getProductsResultQuantity(self):
        return len(self.getAllProductsResult())

    def getProductPrice(self, index):
        # productPrice_fullXpath = self.locator.allProductsResult_xpath + '[' + str(index) + ']' + self.locator.productPrice_xpath
        productPrice_fullXpath = f'{self.locator.allProductsResult_xpath}[{index}]{self.locator.productPrice_xpath}'
        return self.driver.find_element_by_xpath(productPrice_fullXpath).text

    def getSearchNoResultMessage(self):
        return self.driver.find_element_by_xpath(self.locator.searchNoResultMessage_xpath).text
