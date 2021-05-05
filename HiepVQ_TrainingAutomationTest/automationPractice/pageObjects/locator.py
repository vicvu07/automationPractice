class CheckOutLocator:
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


class ContactUsLocator:
    subjectHeading_id = 'id_contact'
    email_id = 'email'
    orderReference_id = 'id_order'
    message_id = 'message'
    send_id = 'submitMessage'
    allertSuccess_xpath = '//*[@id="center_column"]/p'
    attachFile_id = 'fileUpload'
    no_file_selected_xpath = '//span[@class="filename"][contains(text(),"No file selected")]'


class CreateAccountLocator:
    # MrTitle_id = 'id_gender1'
    firstName_id = 'customer_firstname'
    lastName_id = 'customer_lastname'
    password_id = 'passwd'
    days_id = 'days'
    months_id = 'months'
    years_id = 'years'
    address_id = 'address1'
    city_id = 'city'
    state_id = 'id_state'
    postalCode_id = 'postcode'
    # country_id = 'id_country'
    phone_id = 'phone_mobile'
    aliasAdress_id = 'alias'
    register_id = 'submitAccount'
    logout_xpath = '//a[@title="Log me out"]'


class HomePageLocator:
    signInButton_linkText = 'Sign in'
    newsletter_id = 'newsletter-input'
    submitNewsletter_xpath = "//button[@name='submitNewsletter']"
    allertSuccess_xpath = '//p[@class="alert alert-success"]'
    contactUs_linkText = 'Contact us'
    search_id = 'search_query_top'
    search_xpath = '//*[@id="search_query_top"]'
    all_suggest_keywords_xpath = "//div[@class='ac_results']//li[starts-with(@class,'ac_')]"
    searchButton_xpath = '//button[@name="submit_search"]'
    allProducts_xpath = '//*[@id="homefeatured"]/li'
    addToCart_xpath = '//ul[@id="homefeatured"]//span[contains(text(),"Add to cart")]'
    addToCart_link_text = 'Add to cart'
    continueShopping_xpath = '//span[@title="Continue shopping"]'
    proceedToCheckout_xpath = '//a[@title="Proceed to checkout"]'
    price_xpath = '//ul[@id="homefeatured"]//div[@class="right-block"]//span[@itemprop="price"]'
    allProductsPricePercentReduction_xpath = '//ul[@id="homefeatured"]//div[@class="left-block"]//span[@class="price-percent-reduction"]'
    product_belongs_to_reduction_xpath = f'{allProductsPricePercentReduction_xpath}/parent::div/preceding-sibling::a[@class="product_img_link"]'
    productImage_xpath = "//ul[@id='blockbestsellers']//a[@class='product_img_link']"


class LoginPageLocator:
    emailCreate_id = 'email_create'
    submitCreate_id = 'SubmitCreate'
    createAccountError_id = 'create_account_error'
    email_signIn_id = 'email'
    password_signIn_id = 'passwd'
    signIn_id = 'SubmitLogin'


class ProductDetailPageLocator:
    productTitle_xpath = "//h1[@itemprop='name']"
    productPrice_id = 'our_price_display'
    bigPig_id = 'bigpic'
    image_viewLarge_xpath = "//img[@class='fancybox-image']"
    productTitle_viewLarge_xpath = "//span[@class='child']"
    viewLarger_button_xpath = '//*[@id="view_full_size"]/span'
    close_viewLarger_xpath = '//a[@title="Close"]'
    quantity_id = 'quantity_wanted'
    add_to_cart_productDetail_xpath = '//*[@id="add_to_cart"]/button'
    null_quantity_message_xpath = "//p[@class='fancybox-error']"
    add_to_cart_successfully_message_xpath = "//div[@id='layer_cart']//span[@title='Close window']/following-sibling::h2"
    close_add_to_cart_message_xpath = "//div[@id='layer_cart']//span[@title='Close window']"
    cart_button_xpath = "//b[contains(text(),'Cart')]"
    tweet_xpath = "//button[@class='btn btn-default btn-twitter']"
    username_twitter_name = 'session[username_or_email]'
    password_twitter_name = 'session[password]'
    login_button_twitter_xpath = "//span[contains(text(),'Log in')]"
    leave_commnent_xpath = '//*[@id="product_comments_block_extra"]/ul/li/a'
    review_title_id = 'comment_title'
    comment_content_id = 'content'
    send_comment_id = 'submitNewMessage'
    send_comment_message_xpath = "//div[@class='fancybox-inner']/p[contains(text(),'comment')]"
    send_to_a_friend_id = 'send_friend_button'
    friend_name_id = 'friend_name'
    friend_email_id = 'friend_email'
    send_to_a_friend_button_id = 'sendEmail'
    send_to_a_friend_message = "//div[@class='fancybox-inner']/p[contains(text(),'e-mail')]"
    full_size_xpath = '//*[@id="view_full_size"]'


class SearchPageLocator:
    searchResultMessage_xpath = '//span[@class="heading-counter"]'
    allProductsResult_xpath = '//ul[@class="product_list grid row"]/li'
    productPrice_xpath = '//div[@class="product-image-container"]//span[@class="price product-price"]'
    searchNoResultMessage_xpath = '//p[@class="alert alert-warning"]'
