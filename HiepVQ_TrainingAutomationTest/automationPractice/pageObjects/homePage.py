from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locator.homePage_locator import HomePage_locator


class HomePage:
    # Get locator
    locator = HomePage_locator

    def __init__(self, driver):
        self.driver = driver

    def getAllertSuccess(self):
        allert_success = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.allertSuccess_xpath)))
        return allert_success.text

    def getSearchKeyword(self):
        search_keyword = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, self.locator.search_id))
        )
        return search_keyword.get_attribute('value')

    def getSearchPlaceHolder(self):
        placeholder = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, self.locator.search_id))
        )
        return placeholder.get_attribute('placeholder')

    def getSuggestKeyWord(self, suggestKeyword_index):
        suggest_keyword_xpath = f'{self.locator.all_suggest_keywords_xpath}[{suggestKeyword_index}]'
        suggest_keyword = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, suggest_keyword_xpath))
        )
        return suggest_keyword.text


    def getAllProducts(self):
        return self.driver.find_elements_by_xpath(self.locator.allProducts_xpath)


    def setNewsletterEmail(self, newsletterEmail):
        self.driver.find_element_by_id(self.locator.newsletter_id).send_keys(newsletterEmail)


    def setSearchKeyword(self, keyword):
        search_input = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, self.locator.search_id))
        )
        search_input.send_keys(keyword)


    def clickSignIn(self):
        self.driver.find_element_by_link_text(self.locator.signInButton_linkText).click()


    def clickSubmitNewsletter(self):
        self.driver.find_element_by_xpath(self.locator.submitNewsletter_xpath).click()


    def clickContactUs(self):
        self.driver.find_element_by_link_text(self.locator.contactUs_linkText).click()


    def click_product_image(self, index):
        # Click a image of a product in product list
        productImage_index_xpath = self.locator.allProducts_xpath + '[' + str(
            index) + ']' + self.locator.productImage_xpath

        # Use javaScript executor to click on the element.
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element_by_xpath(productImage_index_xpath))


    def hover_product_image(self, index):
        productImage_index_xpath = self.locator.allProducts_xpath + '[' + str(
            index) + ']' + self.locator.productImage_xpath
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element_by_xpath(productImage_index_xpath)).perform()


    def clearSearchKeyWord(self):
        self.driver.find_element_by_id(self.locator.search_id).clear()


    def getAllSuggestKeyWords(self):
        allSuggestKeyWords = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locator.all_suggest_keywords_xpath))
        )
        suggestKeyWord_list = []
        for suggestKeyWord in allSuggestKeyWords:
            suggestKeyWord_text = suggestKeyWord.text
            suggestKeyWord_list.append(suggestKeyWord_text)
        return suggestKeyWord_list


    def getPrice(self, index):
        price_xpath_full = self.locator.allProducts_xpath + '[' + str(index) + ']' + self.locator.price_xpath
        price_text = self.driver.find_element_by_xpath(price_xpath_full).text
        price = float(price_text[1:(len(price_text) + 1)])
        return price


    def get_price_percent_reduction(self, index):
        price_percent_reduction_xpath = self.locator.allProducts_xpath + '[' + str(
            index) + ']' + self.locator.allProductsPricePercentReduction
        price_percent_reduction_text = self.driver.find_element_by_xpath(price_percent_reduction_xpath).text
        percent_index = len(price_percent_reduction_text) - 1
        price_percent_reduction = int(price_percent_reduction_text[1:percent_index])
        return price_percent_reduction


    def clickSuggestKeyWord(self, suggestKeyword_index):
        self.driver.find_element_by_xpath(f'{self.locator.all_suggest_keywords_xpath}[{suggestKeyword_index}]').click()


    def clickSearchButton(self):
        self.driver.find_element_by_xpath(self.locator.searchButton_xpath).click()


    def click_add_to_cart(self, index):
        addToCart_xpath_full = self.locator.allProducts_xpath + '[' + str(index) + ']' + self.locator.addToCart_xpath
        self.driver.find_element_by_xpath(addToCart_xpath_full).click()


    def hover_product(self, index):
        action = ActionChains(self.driver)
        allProducts_element = self.driver.find_elements_by_xpath(self.locator.allProducts_xpath)
        action.move_to_element(allProducts_element[index - 1]).perform()


    def click_continue_shopping(self):
        self.driver.find_element_by_xpath(self.locator.continueShopping_xpath).click()


    def click_proceed_to_checkout(self):
        self.driver.find_element_by_xpath(self.locator.proceedToCheckout_xpath).click()


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
