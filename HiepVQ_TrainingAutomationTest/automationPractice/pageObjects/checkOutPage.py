from pageObjects.loginPage import LoginPage
import time
from locator.checkOut_locator import CheckOut_locator


class CheckOutPage:
    # Get locator of Checkout Page
    locator = CheckOut_locator

    def __init__(self, driver):
        self.driver = driver

    def get_products_price(self):
        products_price_text = self.driver.find_element_by_id(self.locator.productsPrice_id).text
        products_price = float(products_price_text[1:(len(products_price_text) + 1)])
        return products_price

    def get_complete_message(self):
        return self.driver.find_element_by_xpath(self.locator.completeMessage_xpath).text

    def get_product_price(self, index):
        productPrice_index_xpath = self.locator.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.locator.productPrice_xpath
        productPrice_text = self.driver.find_element_by_xpath(productPrice_index_xpath).text
        productPrice = float(productPrice_text[1:(len(productPrice_text) + 1)])
        return productPrice

    def get_terms_agreement_warning(self):
        return self.driver.find_element_by_xpath(self.locator.termsAgreementWarning_xpath).text

    def get_product_title(self, index):
        product_title_index_xpath = f'{self.locator.allProductsDetailSummary_xpath}[{index}]{self.locator.product_title_xpath}'
        return self.driver.find_element_by_xpath(product_title_index_xpath).text

    def get_product_quantity(self, index):
        product_quantity_index_xpath = f'{self.locator.allProductsDetailSummary_xpath}[{index}]{self.locator.productQuantity_xpath}'
        return self.driver.find_element_by_xpath(product_quantity_index_xpath).get_attribute('value')

    def set_product_quantity(self, index, quantity):
        productQuantity_index_xpath = self.locator.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.locator.productQuantity_xpath
        self.driver.find_element_by_xpath(productQuantity_index_xpath).clear()
        self.driver.find_element_by_xpath(productQuantity_index_xpath).send_keys(str(quantity))

    def click_proceed_to_check_out_summary_process(self):
        self.driver.find_element_by_xpath(self.locator.proceedToCheckout_summaryProcess_xpath).click()

    def click_proceed_to_check_out_address_process(self):
        self.driver.find_element_by_xpath(self.locator.proceedToCheckout_addressProcess_xpath).click()

    def click_proceed_to_check_out_shippingProcess_xpath(self):
        self.driver.find_element_by_xpath(self.locator.proceedToCheckout_shippingProcess_xpath).click()

    def click_term_agreement(self):
        self.driver.find_element_by_id(self.locator.termsAgreement_id).click()

    def click_pay_by_bank_wire(self):
        self.driver.find_element_by_xpath(self.locator.payByBankWire_xpath).click()

    def click_confirm_my_order(self):
        self.driver.find_element_by_xpath(self.locator.confirmMyOrder_xpath).click()

    def proceed_to_checkout(self, emailSignIn, passwordSignIn):
        self.click_proceed_to_check_out_summary_process()
        time.sleep(2)
        loginPage = LoginPage(self.driver)
        loginPage.sign_in(emailSignIn, passwordSignIn)
        time.sleep(2)
        self.click_proceed_to_check_out_address_process()
        time.sleep(2)
        self.click_term_agreement()
        time.sleep(2)
        self.click_proceed_to_check_out_shippingProcess_xpath()
        time.sleep(2)
        self.click_pay_by_bank_wire()
        time.sleep(2)
        self.click_confirm_my_order()
        time.sleep(2)
        return self.get_complete_message()

    def click_quantity_down(self, index):
        quantityDown_index_path = self.locator.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.locator.quantityDown_xpath
        self.driver.find_element_by_xpath(quantityDown_index_path).click()

    def click_delete_product(self, index):
        deleteProduct_index_path = self.locator.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.locator.deleteProduct_xpath
        self.driver.find_element_by_xpath(deleteProduct_index_path).click()

    def close_terms_agreement_warning(self):
        self.driver.find_element_by_xpath(self.locator.closeTermsAgreementWarning_xpath).click()
