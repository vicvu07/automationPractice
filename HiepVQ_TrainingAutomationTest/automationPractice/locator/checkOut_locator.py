from pageObjects.loginPage import LoginPage
import time


class CheckOut_locator:
    productsPrice_id = 'total_product'
    proceedToCheckout_summaryProcess_xpath = "//p[@class='cart_navigation clearfix']//span[contains(text(),'Proceed to checkout')]"
    proceedToCheckout_addressProcess_xpath = "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]"
    termsAgreement_id = 'cgv'
    proceedToCheckout_shippingProcess_xpath = '//*[@id="form"]/p/button'
    payByBankWire_xpath = "//a[@title='Pay by bank wire']"
    confirmMyOrder_xpath = '//*[@id="cart_navigation"]/button'
    completeMessage_xpath = "//p[@class='cheque-indent']//strong"
    allProductsDetailSummary_xpath = '//*[@id="cart_summary"]/tbody/tr'  # xpath of all products
    # quantityDown_xpath = "//input[starts-with(@class,'cart_quantity_input')]"
    deleteProduct_xpath = "//i[@class='icon-trash']"
    productQuantity_xpath = "//input[starts-with(@class,'cart_quantity_input')]"
    productPrice_xpath = "//td[@class='cart_total']//span[@class='price']"
    termsAgreementWarning_xpath = "//p[@class='fancybox-error']"
    closeTermsAgreementWarning_xpath = "//a[@title='Close']"
    product_title_xpath = "//td[@class='cart_description']//p[@class='product-name']"
