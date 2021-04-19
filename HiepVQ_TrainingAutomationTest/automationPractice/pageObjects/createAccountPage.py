from selenium.webdriver.support.ui import Select
class CreateAccountPage():
    # MrTitle_id = 'id_gender1'
    firstName_id = 'customer_firstname'
    lastName_id = 'customer_lastname'
    password_id = 'passwd'
    days_id = 'days'
    months_id ='months'
    years_id = 'years'
    address_id = 'address1'
    city_id = 'city'
    state_id = 'id_state'
    postalCode_id ='postcode'
    # country_id = 'id_country'
    phone_id = 'phone_mobile'
    aliasAdress_id = 'alias'
    register_id = 'submitAccount'

    def __init__(self,driver):
        self.driver = driver
    def setFirstName(self,firstName):
        self.driver.find_element_by_id(self.firstName_id).send_keys(firstName)
    def setLastName(self,lastName):
        self.driver.find_element_by_id(self.lastName_id).send_keys(lastName)
    def setPassword(self,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)
    def setAddress(self,address):
        self.driver.find_element_by_id(self.address_id).send_keys(address)
    def setCity(self,city):
        self.driver.find_element_by_id(self.city_id).send_keys(city)
    def setPostalCode(self,postalCode):
        self.driver.find_element_by_id(self.postalCode_id).send_keys(postalCode)
    def setPhone(self,phone):
        self.driver.find_element_by_id(self.phone_id).send_keys(phone)
    def setAliasAdress(self,aliasAdress):
        self.driver.find_element_by_id(self.aliasAdress_id).send_keys(aliasAdress)

    def selectState(self,state):
        Select(self.driver.find_element_by_id(self.state_id)).select_by_visible_text(state)
    def clickRegister(self):
        self.driver.find_element_by_id(self.register_id).click()