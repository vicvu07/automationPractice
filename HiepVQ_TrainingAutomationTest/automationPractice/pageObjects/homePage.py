from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.locator import HomePageLocator
from decimal import Decimal


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        # Get locator
        self.locator = HomePageLocator

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
        allProducts_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locator.allProducts_xpath))
        )
        return allProducts_element

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
        all_images_of_products = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locator.productImage_xpath))
        )
        # Use javaScript executor to click on the element.
        self.driver.execute_script("arguments[0].click();",
                                   all_images_of_products[index])

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
        # price_xpath_full = self.locator.allProducts_xpath + '[' + str(index) + ']' + self.locator.price_xpath
        price_text_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locator.price_xpath))
        )
        price_text = price_text_element[index - 1].get_attribute('innerHTML').strip()
        price = Decimal(price_text[1:(len(price_text) + 1)])
        return price

    def get_quantity_price_percent_reduction(self):
        # Get all percent reduction prices
        all_prices_percent_reduction = self.driver.find_elements_by_xpath(
            self.locator.allProductsPricePercentReduction_xpath)
        return len(all_prices_percent_reduction)

    def get_price_percent_reduction(self, index):
        # Get all percent reduction prices
        all_prices_percent_reduction = self.driver.find_elements_by_xpath(
            self.locator.allProductsPricePercentReduction_xpath)
        # Get percent reduction price (text) at an product
        price_percent_reduction_text = all_prices_percent_reduction[index].get_attribute('innerHTML').strip()
        # Get percent reduction price in before text
        percent_index = len(price_percent_reduction_text) - 1
        price_percent_reduction = int(price_percent_reduction_text[1:percent_index])
        return price_percent_reduction

    def click_product_belongs_to_reduction(self, percent):
        quantity_price_percent_reduction = self.get_quantity_price_percent_reduction()
        for index in range(quantity_price_percent_reduction):
            price_percent_reduction = self.get_price_percent_reduction(index)
            if price_percent_reduction == percent:
                all_product_belongs_to_reduction = self.driver.find_elements_by_xpath(self.locator.product_belongs_to_reduction_xpath)
                # Use javaScript executor to click on the element.
                self.driver.execute_script("arguments[0].click();",
                                           all_product_belongs_to_reduction[index])
                break


    def clickSuggestKeyWord(self, suggestKeyword_index):
        self.driver.find_element_by_xpath(f'{self.locator.all_suggest_keywords_xpath}[{suggestKeyword_index}]').click()

    def clickSearchButton(self):
        self.driver.find_element_by_xpath(self.locator.searchButton_xpath).click()

    def click_add_to_cart(self, index):
        add_to_cart_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locator.addToCart_xpath))
        )
        add_to_cart_element[index - 1].click()

    def hover_product(self, index):
        action = ActionChains(self.driver)
        allProducts_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locator.allProducts_xpath))
        )
        action.move_to_element(allProducts_element[index - 1]).perform()

    def click_continue_shopping(self):
        continue_shopping_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.continueShopping_xpath))
        )
        continue_shopping_element.click()

    def click_proceed_to_checkout(self):
        proceed_to_checkout = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.locator.proceedToCheckout_xpath))
        )
        proceed_to_checkout.click()

    def add_product_and_continue(self, index):
        self.hover_product(index)
        self.click_add_to_cart(index)
        self.click_continue_shopping()

    def add_product_and_checkout(self, index):
        self.hover_product(index)
        self.click_add_to_cart(index)
        self.click_proceed_to_checkout()
