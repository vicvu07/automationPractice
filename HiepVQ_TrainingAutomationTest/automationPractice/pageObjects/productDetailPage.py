from selenium.webdriver.common.action_chains import ActionChains
import time
class ProductDetailPage():
    productTitle_xpath = '//*[@id="center_column"]/div/div/div[3]/h1'
    productPrice_id = 'our_price_display'
    bigPig_id = 'bigpic'
    image_viewLarge_xpath = '//*[@id="product"]/div[2]/div/div[1]/div/img'
    productTitle_viewLarge_xpath = '//*[@id="product"]/div[@class="fancybox-wrap fancybox-desktop fancybox-type-image fancybox-opened"]/div/div[@class="fancybox-title fancybox-title-float-wrap"]/span'
    viewLarger_button_xpath = '//*[@id="view_full_size"]/span'
    close_viewLarger_xpath = '//a[@title="Close"]'
    quantity_id = 'quantity_wanted'
    add_to_cart_productDetail_xpath = '//*[@id="add_to_cart"]/button'
    null_quantity_message_xpath = '//*[@id="product"]/div[@class="fancybox-overlay fancybox-overlay-fixed"]/div/div/div/div/p'
    add_to_cart_successfully_message_xpath = '//*[@id="layer_cart"]/div[1]/div[1]/h2'
    close_add_to_cart_message_xpath = '//div[@id="layer_cart"]/div[@class="clearfix"]/div[1]/span'
    cart_button_xpath = '//*[@id="header"]/div[3]/div/div/div[3]/div/a'
    tweet_xpath = '//*[@id="center_column"]/div/div/div[3]/p[7]/button[@class="btn btn-default btn-twitter"]'
    username_twitter_name = 'session[username_or_email]'
    password_twitter_name = 'session[password]'
    login_button_twitter_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div[2]'
    tweet_a_post_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div[3]/div'
    leave_commnent_xpath = '//*[@id="product_comments_block_extra"]/ul/li/a'
    review_title_id = 'comment_title'
    comment_content_id = 'content'
    send_comment_id = 'submitNewMessage'
    send_comment_message_xpath = '//*[@id="product"]/div[@class="fancybox-wrap fancybox-desktop fancybox-type-html fancybox-opened"]/div/div/div/p[1]'
    send_to_a_friend_id = 'send_friend_button'
    friend_name_id = 'friend_name'
    friend_email_id = 'friend_email'
    send_to_a_friend_button_id = 'sendEmail'
    send_to_a_friend_message = '//*[@id="product"]/div[@class="fancybox-wrap fancybox-desktop fancybox-type-html fancybox-opened"]/div/div/div/p[1]'
    full_size_xpath = '//*[@id="view_full_size"]'


    def __init__(self, driver):
        self.driver = driver

    def set_product_quantity(self, quantity):
        self.driver.find_element_by_id(self.quantity_id).clear()
        self.driver.find_element_by_id(self.quantity_id).send_keys(f'{quantity}')

    def set_friend_name(self, friend_name):
        self.driver.find_element_by_id(self.friend_name_id).send_keys(friend_name)

    def set_friend_email(self, friend_email):
        self.driver.find_element_by_id(self.friend_email_id).send_keys(friend_email)

    def getProductTitle(self):
        return self.driver.find_element_by_xpath(self.productTitle_xpath).text

    def getProductPrice(self):
        return self.driver.find_element_by_id(self.productPrice_id).text

    def get_size_of_product_image(self):
        height = self.driver.find_element_by_id(self.bigPig_id).size.get('height')
        width = self.driver.find_element_by_id(self.bigPig_id).size.get('width')
        return height * width

    def get_size_of_view_large_image(self):
        height = self.driver.find_element_by_xpath(self.image_viewLarge_xpath).size.get('height')
        width = self.driver.find_element_by_xpath(self.image_viewLarge_xpath).size.get('width')
        return height * width

    def get_location_view_large_image(self):
        return self.driver.find_element_by_xpath(self.image_viewLarge_xpath).location

    def get_location_product_title(self):
        return self.driver.find_element_by_xpath(self.productTitle_viewLarge_xpath).location

    def get_null_quantity_message(self):
        return self.driver.find_element_by_xpath(self.null_quantity_message_xpath).text

    def get_add_to_cart_successfully_message(self):
        return self.driver.find_element_by_xpath(self.add_to_cart_successfully_message_xpath).text

    def get_send_review_message(self):
        return self.driver.find_element_by_xpath(self.send_comment_message_xpath).text

    def get_send_to_a_friend_message(self):
        return self.driver.find_element_by_xpath(self.send_to_a_friend_message).text

    def click_big_page(self):
        self.driver.find_element_by_id(self.bigPig_id).click()

    def click_view_larger_button(self):
        action = ActionChains(self.driver)
        full_size_div = self.driver.find_element_by_xpath(self.full_size_xpath)
        action.move_to_element(full_size_div).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.viewLarger_button_xpath).click()

    def click_close_view_larger(self):
        self.driver.find_element_by_xpath(self.close_viewLarger_xpath).click()

    def click_close_add_to_cart_successfully_message(self):
        self.driver.find_element_by_xpath(self.close_add_to_cart_message_xpath).click()

    def click_cart_button(self):
        self.driver.find_element_by_xpath(self.cart_button_xpath).click()

    def click_tweet(self):
        self.driver.find_element_by_xpath(self.tweet_xpath).click()

    def leave_review(self, review_title, comment_content):
        self.driver.find_element_by_xpath(self.leave_commnent_xpath).click()
        self.driver.find_element_by_id(self.review_title_id).send_keys(review_title)
        self.driver.find_element_by_id(self.comment_content_id).send_keys(comment_content)
        self.driver.find_element_by_id(self.send_comment_id).click()

    def tweet_a_post(self):
        self.driver.find_element_by_xpath(self.tweet_a_post_xpath).click()

    def check_image_view_large_is_displayed(self):
        try:
            return self.driver.find_element_by_xpath(self.image_viewLarge_xpath).is_displayed()
        except:
            return False

    def check_product_title_view_large_is_displayed(self):
        try:
            return self.driver.find_element_by_xpath(self.productTitle_xpath).is_displayed()
        except:
            return False

    def click_add_to_cart(self):
        action = ActionChains(self.driver)
        add_to_cart_button = self.driver.find_element_by_xpath(self.add_to_cart_productDetail_xpath)
        action.move_to_element(add_to_cart_button).click().perform()
        # self.driver.find_element_by_xpath(self.add_to_cart_productDetail_xpath).click()

    def click_send_to_a_friend(self):
        self.driver.find_element_by_id(self.send_to_a_friend_id).click()

    def send_to_a_friend(self):
        self.driver.find_element_by_id(self.send_to_a_friend_button_id).click()

    def login_twitter(self, username, password):
        self.driver.find_element_by_name(self.username_twitter_name).send_keys(username)
        self.driver.find_element_by_name(self.password_twitter_name).send_keys(password)
        return self.driver.find_element_by_xpath(self.login_button_twitter_xpath).is_displayed()





