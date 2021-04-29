class ProductDetailPage_locator:
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



