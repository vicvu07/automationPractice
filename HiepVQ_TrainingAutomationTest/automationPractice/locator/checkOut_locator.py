from pageObjects.loginPage import LoginPage
import time


class CheckOut_locator:
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