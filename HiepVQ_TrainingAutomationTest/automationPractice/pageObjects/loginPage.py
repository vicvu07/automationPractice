import time

from pageObjects.locator import LoginPageLocator

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        # Get locator
        self.locator = LoginPageLocator

    def getCreateAccountError_messages(self):
        time.sleep(5)
        create_account_error_message = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.ID, self.locator.createAccountError_id))
        )
        return create_account_error_message.text

    def setEmail_Create(self, email_create):
        emailCreate = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, self.locator.emailCreate_id))
        )
        emailCreate.send_keys(email_create)

    def clickSubmit_Create(self):
        self.driver.find_element_by_id(self.locator.submitCreate_id).click()

    def sign_in(self, emailSignIn, passwordSignIn):
        email_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, self.locator.email_signIn_id))
        )
        email_element.send_keys(emailSignIn)
        self.driver.find_element_by_id(self.locator.password_signIn_id).send_keys(passwordSignIn)
        self.driver.find_element_by_id(self.locator.signIn_id).click()
