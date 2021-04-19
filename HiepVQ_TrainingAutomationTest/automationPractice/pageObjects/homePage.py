from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    signInButton_linkText = 'Sign in'
    newsletter_id = 'newsletter-input'
    submitNewsletter_xpath = '//*[@id="newsletter_block_left"]/div/form/div/button'
    allertSuccess_xpath = '//*[@id="columns"]/p'
    contactUs_linkText = 'Contact us'
    search_id = 'search_query_top'
    search_xpath = '//*[@id="search_query_top"]'
    suggestKeyword_xpath = '//div[@class = "ac_results"]/ul/li'
    searchButton_xpath = '//*[@id="searchbox"]/button'
    allProducts_xpath = '//*[@id="homefeatured"]/li'
    addToCart_xpath = '/div/div[2]/div[2]/a[1]'
    addToCart_link_text = 'Add to cart'
    continueShopping_xpath = '//*[@id="layer_cart"]/div[@class="clearfix"]/div[@class="layer_cart_cart col-xs-12 col-md-6"]/div[@class="button-container"]/span'
    proceedToCheckout_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a'
    price_xpath = '/div/div[2]/div[1]/span'
    allProductsPricePercentReduction = '/div/div[2]/div[1]/span[3]'
    productImage_xpath = '/div/div[1]/div/a[1]/img'

    def __init__(self, driver):
        self.driver = driver

    def getAllertSuccess(self):
        return self.driver.find_element_by_xpath(self.allertSuccess_xpath).text

    def getSearchKeyword(self):
        return self.driver.find_element_by_id(self.search_id).get_attribute('value')

    def getSearchPlaceHolder(self):
        return self.driver.find_element_by_id(self.search_id).get_attribute('placeholder')

    def getSuggestKeyWord(self, suggestKeyword_index):
        return self.driver.find_element_by_xpath(self.suggestKeyword_xpath + suggestKeyword_index).text

    def getAllProducts(self):
        return self.driver.find_elements_by_xpath(self.allProducts_xpath)

    def setNewsletterEmai(self, newsletterEmail):
        self.driver.find_element_by_id(self.newsletter_id).send_keys(newsletterEmail)

    def setSearchKeyword(self, keyword):
        self.driver.find_element_by_id(self.search_id).send_keys(keyword)
        # self.driver.find_element_by_xpath(self.search_xpath).send_keys(keyword)

    def clickSignIn(self):
        self.driver.find_element_by_link_text(self.signInButton_linkText).click()

    def clickSubmitNewsletter(self):
        self.driver.find_element_by_xpath(self.submitNewsletter_xpath).click()

    def clickContactUs(self):
        self.driver.find_element_by_link_text(self.contactUs_linkText).click()

    def click_product_image(self, index):
        # Click a image of a product in product list
        productImage_index_xpath = self.allProducts_xpath + '[' + str(index) + ']' + self.productImage_xpath

        # Use javaScript executor to click on the element.
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element_by_xpath(productImage_index_xpath))

    def hover_product_image(self, index):
        productImage_index_xpath = self.allProducts_xpath + '[' + str(index) + ']' + self.productImage_xpath
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_xpath(productImage_index_xpath)).perform()

    def clearSearchKeyWord(self):
        self.driver.find_element_by_id(self.search_id).clear()

    def getAllSuggestKeyWords(self):
        allSuggestKeyWords = self.driver.find_elements_by_xpath(self.suggestKeyword_xpath)
        suggestKeyWord_list = []
        for suggestKeyWord in allSuggestKeyWords:
            suggestKeyWord_text = suggestKeyWord.text
            suggestKeyWord_list.append(suggestKeyWord_text)
        return suggestKeyWord_list

    def getPrice(self, index):
        price_xpath_full = self.allProducts_xpath + '[' + str(index) + ']' + self.price_xpath
        price_text = self.driver.find_element_by_xpath(price_xpath_full).text
        price = float(price_text[1:(len(price_text) + 1)])
        return price

    def get_price_percent_reduction(self, index):
        price_percent_reduction_xpath = self.allProducts_xpath + '[' + str(
            index) + ']' + self.allProductsPricePercentReduction
        price_percent_reduction_text = self.driver.find_element_by_xpath(price_percent_reduction_xpath).text
        percent_index = len(price_percent_reduction_text) - 1
        price_percent_reduction = int(price_percent_reduction_text[1:percent_index])
        return price_percent_reduction

    def clickSuggestKeyWord(self, suggestKeyword_index):
        self.driver.find_element_by_xpath(self.suggestKeyword_xpath + suggestKeyword_index).click()

    def clickSearchButton(self):
        self.driver.find_element_by_xpath(self.searchButton_xpath).click()

    def click_add_to_cart(self, index):
        addToCart_xpath_full = self.allProducts_xpath + '[' + str(index) + ']' + self.addToCart_xpath
        self.driver.find_element_by_xpath(addToCart_xpath_full).click()

    def hover_product(self, index):
        action = ActionChains(self.driver)
        allProducts_element = self.driver.find_elements_by_xpath(self.allProducts_xpath)
        action.move_to_element(allProducts_element[index - 1]).perform()

    def click_continue_shopping(self):
        self.driver.find_element_by_xpath(self.continueShopping_xpath).click()

    def click_proceed_to_checkout(self):
        self.driver.find_element_by_xpath(self.proceedToCheckout_xpath).click()

    def add_product_and_continue(self, index):
        self.hover_product(index)
        self.click_add_to_cart(index)
        time.sleep(5)
        # self.driver.implicit_wait(10)
        self.click_continue_shopping()
        time.sleep(2)

    def add_product_and_checkout(self, index):
        self.hover_product(index)
        self.click_add_to_cart(index)
        time.sleep(5)
        self.click_proceed_to_checkout()
        time.sleep(2)
