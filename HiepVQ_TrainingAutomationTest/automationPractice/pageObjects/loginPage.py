from locator.loginPage_locator import LoginPage_locator


class LoginPage:
    # Get locator
    locator = LoginPage_locator

    def __init__(self, driver):
        self.driver = driver

    def getCreateAccountError_messages(self):
        createAccountError_message = self.driver.find_element_by_id(self.locator.createAccountError_id).text
        return createAccountError_message

    def setEmail_Create(self, email_create):
        self.driver.find_element_by_id(self.locator.emailCreate_id).send_keys(email_create)

    def clickSubmit_Create(self):
        self.driver.find_element_by_id(self.locator.submitCreate_id).click()

    def sign_in(self, emailSignIn, passwordSignIn):
        self.driver.find_element_by_id(self.locator.email_signIn_id).send_keys(emailSignIn)
        self.driver.find_element_by_id(self.locator.password_signIn_id).send_keys(passwordSignIn)
        self.driver.find_element_by_id(self.locator.signIn_id).click()
