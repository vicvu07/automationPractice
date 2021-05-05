from pageObjects.loginPage import LoginPage
import time
from pageObjects.locator import CheckOutLocator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pageObjects.locator import HomePageLocator


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver
        # Get locator of Checkout Page
        self.locator = CheckOutLocator

    def get_products_price(self):
        products_price_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, self.locator.productsPrice_id))
        )
        products_price_text = products_price_element.text
        products_price = float(products_price_text[1:(len(products_price_text) + 1)])
        return products_price

    def get_complete_message(self):
        completeMessage_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.completeMessage_xpath))
        )
        return completeMessage_element.text

    def get_product_price(self, index):
        productPrice_index_xpath = self.locator.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.locator.productPrice_xpath
        productPrice_text = self.driver.find_element_by_xpath(productPrice_index_xpath).text
        productPrice = float(productPrice_text[1:(len(productPrice_text) + 1)])
        return productPrice

    def get_terms_agreement_warning(self):
        termsAgreementWarning_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.termsAgreementWarning_xpath))
        )
        return termsAgreementWarning_element.text

    def get_product_title(self, index):
        product_title_index_xpath = f'{self.locator.allProductsDetailSummary_xpath}[{index}]{self.locator.product_title_xpath}'
        product_title_index = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, product_title_index_xpath))
        )
        return product_title_index.text

    def get_product_quantity(self, index):
        product_quantity_index_xpath = f'{self.locator.allProductsDetailSummary_xpath}[{index}]{self.locator.productQuantity_xpath}'
        return self.driver.find_element_by_xpath(product_quantity_index_xpath).get_attribute('value')

    def set_product_quantity(self, index, quantity):
        productQuantity_index_xpath = self.locator.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.locator.productQuantity_xpath
        productQuantity_index_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, productQuantity_index_xpath))
        )
        productQuantity_index_element.clear()
        productQuantity_index_element.send_keys(str(quantity))

    def click_proceed_to_check_out_summary_process(self):
        self.driver.find_element_by_xpath(self.locator.proceedToCheckout_summaryProcess_xpath).click()

    def click_proceed_to_check_out_address_process(self):
        proceed_to_checkout_address_process_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.proceedToCheckout_addressProcess_xpath))
        )
        proceed_to_checkout_address_process_element.click()

    def click_proceed_to_check_out_shippingProcess_xpath(self):
        proceedToCheckout_shippingProcess_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.proceedToCheckout_shippingProcess_xpath))
        )
        proceedToCheckout_shippingProcess_element.click()

    def click_term_agreement(self):
        term_agreement_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, self.locator.termsAgreement_id))
        )
        term_agreement_element.click()

    def click_pay_by_bank_wire(self):
        payByBankWire_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.payByBankWire_xpath))
        )
        payByBankWire_element.click()

    def click_confirm_my_order(self):
        confirmMyOrder_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.confirmMyOrder_xpath))
        )
        confirmMyOrder_element.click()

    def proceed_to_checkout(self, emailSignIn, passwordSignIn):
        self.click_proceed_to_check_out_summary_process()
        loginPage = LoginPage(self.driver)
        loginPage.sign_in(emailSignIn, passwordSignIn)
        self.click_proceed_to_check_out_address_process()
        self.click_term_agreement()
        self.click_proceed_to_check_out_shippingProcess_xpath()
        self.click_pay_by_bank_wire()
        self.click_confirm_my_order()
        return self.get_complete_message()

    def click_quantity_down(self, index):
        quantityDown_index_path = self.locator.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.locator.quantityDown_xpath
        self.driver.find_element_by_xpath(quantityDown_index_path).click()

    def click_delete_product(self, index):
        deleteProduct_index_path = self.locator.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.locator.deleteProduct_xpath
        deleteProduct_index_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, deleteProduct_index_path))
        )
        deleteProduct_index_element.click()

    def close_terms_agreement_warning(self):
        self.driver.find_element_by_xpath(self.locator.closeTermsAgreementWarning_xpath).click()
