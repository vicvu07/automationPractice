from pageObjects.loginPage import LoginPage
import time


class CheckOutPage:
    productsPrice_id = 'total_product'
    proceedToCheckout_summaryProcess_xpath = '//*[@id="center_column"]/p[2]/a[1]'
    proceedToCheckout_addressProcess_xpath = '//*[@id="center_column"]/form/p/button'
    termsAgreement_id = 'cgv'
    proceedToCheckout_shippingProcess_xpath = '//*[@id="form"]/p/button'
    payByBankWire_xpath = '//*[@id="HOOK_PAYMENT"]/div[1]/div/p/a'
    confirmMyOrder_xpath = '//*[@id="cart_navigation"]/button'
    completeMessage_xpath = '//*[@id="center_column"]/div/p/strong'
    allProductsDetailSummary_xpath = '//*[@id="cart_summary"]/tbody/tr'  # xpath of all products
    quantityDown_xpath = '/td[5]/div/a[1]'
    deleteProduct_xpath = '/td[7]/div/a'
    productQuantity_xpath = '/td[5]/input[2]'
    productPrice_xpath = '/td[6]/span'
    termsAgreementWarning_xpath = '//*[@id="order"]/div[2]/div/div/div/div/p'
    closeTermsAgreementWarning_xpath = '//*[@id="order"]/div[2]/div/div/a'
    product_title_xpath = '/td[2]/p/a'

    def __init__(self, driver):
        self.driver = driver

    def get_products_price(self):
        products_price_text = self.driver.find_element_by_id(self.productsPrice_id).text
        products_price = float(products_price_text[1:(len(products_price_text) + 1)])
        return products_price

    def get_complete_message(self):
        return self.driver.find_element_by_xpath(self.completeMessage_xpath).text

    def get_product_price(self, index):
        productPrice_index_xpath = self.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.productPrice_xpath
        productPrice_text = self.driver.find_element_by_xpath(productPrice_index_xpath).text
        productPrice = float(productPrice_text[1:(len(productPrice_text) + 1)])
        return productPrice

    def get_terms_agreement_warning(self):
        return self.driver.find_element_by_xpath(self.termsAgreementWarning_xpath).text

    def get_product_title(self, index):
        product_title_index_xpath = f'{self.allProductsDetailSummary_xpath}[{index}]{self.product_title_xpath}'
        return self.driver.find_element_by_xpath(product_title_index_xpath).text

    def get_product_quantity(self, index):
        product_quantity_index_xpath = f'{self.allProductsDetailSummary_xpath}[{index}]{self.productQuantity_xpath}'
        return self.driver.find_element_by_xpath(product_quantity_index_xpath).get_attribute('value')

    def set_product_quantity(self, index, quantity):
        productQuantity_index_xpath = self.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.productQuantity_xpath
        self.driver.find_element_by_xpath(productQuantity_index_xpath).clear()
        self.driver.find_element_by_xpath(productQuantity_index_xpath).send_keys(str(quantity))

    def click_proceed_to_check_out_summary_process(self):
        self.driver.find_element_by_xpath(self.proceedToCheckout_summaryProcess_xpath).click()

    def click_proceed_to_check_out_address_process(self):
        self.driver.find_element_by_xpath(self.proceedToCheckout_addressProcess_xpath).click()

    def click_proceed_to_check_out_shippingProcess_xpath(self):
        self.driver.find_element_by_xpath(self.proceedToCheckout_shippingProcess_xpath).click()

    def click_term_agreement(self):
        self.driver.find_element_by_id(self.termsAgreement_id).click()

    def click_pay_by_bank_wire(self):
        self.driver.find_element_by_xpath(self.payByBankWire_xpath).click()

    def click_confirm_my_order(self):
        self.driver.find_element_by_xpath(self.confirmMyOrder_xpath).click()

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
        quantityDown_index_path = self.allProductsDetailSummary_xpath + '[' + str(index) + ']' + self.quantityDown_xpath
        self.driver.find_element_by_xpath(quantityDown_index_path).click()

    def click_delete_product(self, index):
        deleteProduct_index_path = self.allProductsDetailSummary_xpath + '[' + str(
            index) + ']' + self.deleteProduct_xpath
        self.driver.find_element_by_xpath(deleteProduct_index_path).click()

    def close_terms_agreement_warning(self):
        self.driver.find_element_by_xpath(self.closeTermsAgreementWarning_xpath).click()
