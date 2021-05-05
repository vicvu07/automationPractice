from pageObjects.locator import ProductDetailPageLocator
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailPage:

    def __init__(self, driver):
        self.driver = driver
        # Get locator
        self.locator = ProductDetailPageLocator

    def set_product_quantity(self, quantity):
        self.driver.find_element_by_id(self.locator.quantity_id).clear()
        self.driver.find_element_by_id(self.locator.quantity_id).send_keys(f'{quantity}')

    def set_friend_name(self, friend_name):
        self.driver.find_element_by_id(self.locator.friend_name_id).send_keys(friend_name)

    def set_friend_email(self, friend_email):
        self.driver.find_element_by_id(self.locator.friend_email_id).send_keys(friend_email)

    def getProductTitle(self):
        product_title = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.productTitle_xpath))
        )
        return product_title.text

    def getProductPrice(self):
        return self.driver.find_element_by_id(self.locator.productPrice_id).text

    def get_size_of_product_image(self):
        height = self.driver.find_element_by_id(self.locator.bigPig_id).size.get('height')
        width = self.driver.find_element_by_id(self.locator.bigPig_id).size.get('width')
        return height * width

    def get_size_of_view_large_image(self):
        height = self.driver.find_element_by_xpath(self.locator.image_viewLarge_xpath).size.get('height')
        width = self.driver.find_element_by_xpath(self.locator.image_viewLarge_xpath).size.get('width')
        return height * width

    def get_location_view_large_image(self):
        return self.driver.find_element_by_xpath(self.locator.image_viewLarge_xpath).location

    def get_location_product_title(self):
        return self.driver.find_element_by_xpath(self.locator.productTitle_viewLarge_xpath).location

    def get_null_quantity_message(self):
        null_quantity_message = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.locator.null_quantity_message_xpath))
        )
        return null_quantity_message.text

    def get_add_to_cart_successfully_message(self):
        add_to_cart_successfully_message = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.locator.add_to_cart_successfully_message_xpath))
        )
        return add_to_cart_successfully_message.text

    def get_send_review_message(self):
        send_comment_message = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.locator.send_comment_message_xpath))
        )
        return send_comment_message.text

    def get_send_to_a_friend_message(self):
        send_to_a_friend_message = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.locator.send_to_a_friend_message))
        )
        return send_to_a_friend_message.text

    def click_big_page(self):
        bigPig = WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located((By.ID, self.locator.bigPig_id))
        )
        bigPig.click()

    def click_view_larger_button(self):
        action = ActionChains(self.driver)
        full_size_div = self.driver.find_element_by_xpath(self.locator.full_size_xpath)
        action.move_to_element(full_size_div).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.locator.viewLarger_button_xpath).click()

    def click_close_view_larger(self):
        close_viewLarger =  WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.close_viewLarger_xpath))
        )
        close_viewLarger.click()

    def click_close_add_to_cart_successfully_message(self):
        self.driver.find_element_by_xpath(self.locator.close_add_to_cart_message_xpath).click()

    def click_cart_button(self):
        self.driver.find_element_by_xpath(self.locator.cart_button_xpath).click()

    def click_tweet(self):
        tweet = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.locator.tweet_xpath))
        )
        tweet.click()

    def leave_review(self, review_title, comment_content):
        leave_commnent = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.locator.leave_commnent_xpath))
        )
        leave_commnent.click()
        self.driver.find_element_by_id(self.locator.review_title_id).send_keys(review_title)
        self.driver.find_element_by_id(self.locator.comment_content_id).send_keys(comment_content)
        self.driver.find_element_by_id(self.locator.send_comment_id).click()

    def tweet_a_post(self):
        self.driver.find_element_by_xpath(self.locator.tweet_a_post_xpath).click()

    def check_image_view_large_is_displayed(self):
        try:
            image_viewLarge = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, self.locator.image_viewLarge_xpath))
            )
            return image_viewLarge.is_displayed()
        except:
            assert False

    def check_product_title_view_large_is_displayed(self):
        try:
            return self.driver.find_element_by_xpath(self.locator.productTitle_xpath).is_displayed()
        except:
            return False

    def click_add_to_cart(self):
        action = ActionChains(self.driver)

        add_to_cart_button = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.add_to_cart_productDetail_xpath))
        )
        action.move_to_element(add_to_cart_button).click().perform()
        # self.driver.find_element_by_xpath(self.add_to_cart_productDetail_xpath).click()

    def click_send_to_a_friend(self):
        send_to_a_friend = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, self.locator.send_to_a_friend_id))
        )
        send_to_a_friend.click()

    def send_to_a_friend(self):
        self.driver.find_element_by_id(self.locator.send_to_a_friend_button_id).click()

    def login_twitter(self, username, password):
        self.driver.find_element_by_name(self.locator.username_twitter_name).send_keys(username)
        self.driver.find_element_by_name(self.locator.password_twitter_name).send_keys(password)
        return self.driver.find_element_by_xpath(self.locator.login_button_twitter_xpath).is_displayed()
