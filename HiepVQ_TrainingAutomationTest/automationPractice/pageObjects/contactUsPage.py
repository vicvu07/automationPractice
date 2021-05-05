from selenium.webdriver.support.ui import Select
from pageObjects.locator import ContactUsLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactUsPage:

    def __init__(self, driver):
        self.driver = driver
        # Get locator
        self.locator = ContactUsLocator

    def getAllertSucess(self):
        allert_success = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, self.locator.allertSuccess_xpath))
        )
        return allert_success.text

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

    def attach_file_and_send(self, file):
        self.attachFile(file)
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located((By.XPATH, self.locator.no_file_selected_xpath))
        )
        self.clickSend()
