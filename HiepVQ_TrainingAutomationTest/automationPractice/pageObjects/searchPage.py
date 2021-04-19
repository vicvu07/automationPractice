class SearchPage:
    searchResultMessage_xpath = '//*[@id="center_column"]/h1/span[2]'
    allProductsResult_xpath = '//*[@id="center_column"]/ul/li'
    productPrice_xpath = '/div/div[2]/div[1]/span[1]'
    searchNoResultMessage_xpath = '//*[@id="center_column"]/p'

    def __init__(self,driver):
        self.driver = driver
    def getSearchResultMessage(self):
        return self.driver.find_element_by_xpath(self.searchResultMessage_xpath).text
    def getAllProductsResult(self):
        return self.driver.find_elements_by_xpath(self.allProductsResult_xpath)
    def getProductsResultQuantity(self):
        return len(self.getAllProductsResult())
    def getProductPrice(self,index):
        productPrice_fullXpath = self.allProductsResult_xpath + '[' + str(index) + ']' + self.productPrice_xpath
        return self.driver.find_element_by_xpath(productPrice_fullXpath).text
    def getSearchNoResultMessage(self):
        return self.driver.find_element_by_xpath(self.searchNoResultMessage_xpath).text


