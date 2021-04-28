from selenium.webdriver.support.ui import Select
from locator.contactUsPage_locator import ContactUs_locator


class ContactUsPage:
    # Get locator
    locator = ContactUs_locator

    def __init__(self, driver):
        self.driver = driver

    def getAllertSucess(self):
        return self.driver.find_element_by_xpath(self.locator.allertSuccess_xpath).text

    def setEmailAdress(self, email):
        self.driver.find_element_by_id(self.locator.email_id).send_keys(email)

    def setOrderReference(self, orderReference):
        self.driver.find_element_by_id(self.locator.orderReference_id).send_keys(orderReference)

    def setMessage(self, message):
        self.driver.find_element_by_id(self.locator.message_id).send_keys(message)

    def selectSubjectHeading(self, subjectHeading):
        Select(self.driver.find_element_by_id(self.locator.subjectHeading_id)).select_by_visible_text(subjectHeading)

    def clickSend(self):
        self.driver.find_element_by_id(self.locator.send_id).click()

    def attachFile(self, file):
        self.driver.find_element_by_id(self.locator.attachFile_id).send_keys(file)
