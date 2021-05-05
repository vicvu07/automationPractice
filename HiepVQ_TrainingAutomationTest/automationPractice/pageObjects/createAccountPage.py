from selenium.webdriver.support.ui import Select
from pageObjects.locator import CreateAccountLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver
        # Get locator
        self.locator = CreateAccountLocator

    def setFirstName(self, firstName):
        first_name = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, self.locator.firstName_id))
        )
        first_name.send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_id(self.locator.lastName_id).send_keys(lastName)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.locator.password_id).send_keys(password)

    def setAddress(self, address):
        self.driver.find_element_by_id(self.locator.address_id).send_keys(address)

    def setCity(self, city):
        self.driver.find_element_by_id(self.locator.city_id).send_keys(city)

    def setPostalCode(self, postalCode):
        self.driver.find_element_by_id(self.locator.postalCode_id).send_keys(postalCode)

    def setPhone(self, phone):
        self.driver.find_element_by_id(self.locator.phone_id).send_keys(phone)

    def setAliasAdress(self, aliasAdress):
        self.driver.find_element_by_id(self.locator.aliasAdress_id).send_keys(aliasAdress)

    def selectState(self, state):
        Select(self.driver.find_element_by_id(self.locator.state_id)).select_by_visible_text(state)

    def clickRegister(self):
        self.driver.find_element_by_id(self.locator.register_id).click()

    def log_out(self):
        self.driver.find_element_by_xpath(self.locator.logout_xpath).click()
