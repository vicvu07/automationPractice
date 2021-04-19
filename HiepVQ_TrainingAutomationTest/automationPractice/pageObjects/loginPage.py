class LoginPage:
    emailCreate_id = 'email_create'
    submitCreate_id = 'SubmitCreate'
    createAccountError_id ='create_account_error'
    email_signIn_id = 'email'
    password_signIn_id = 'passwd'
    signIn_id = 'SubmitLogin'

    def __init__(self,driver):
        self.driver = driver
    def getCreateAccountError_messages(self):
        createAccountError_message = self.driver.find_element_by_id(self.createAccountError_id).text
        return createAccountError_message

    def setEmail_Create(self,email_create):
        self.driver.find_element_by_id(self.emailCreate_id).send_keys(email_create)

    def clickSubmit_Create(self):
        self.driver.find_element_by_id(self.submitCreate_id).click()

    def sign_in(self, emailSignIn, passwordSignIn):
        self.driver.find_element_by_id(self.email_signIn_id).send_keys(emailSignIn)
        self.driver.find_element_by_id(self.password_signIn_id).send_keys(passwordSignIn)
        self.driver.find_element_by_id(self.signIn_id).click()


