from selenium.webdriver.support.ui import Select
class ContactUsPage():
    subjectHeading_id = 'id_contact'
    email_id = 'email'
    orderReference_id = 'id_order'
    message_id = 'message'
    send_id = 'submitMessage'
    allertSuccess_xpath = '//*[@id="center_column"]/p'
    attachFile_id = 'fileUpload'

    def __init__(self,driver):
        self.driver = driver
    def getAllertSucess(self):
        return self.driver.find_element_by_xpath(self.allertSuccess_xpath).text
    def setEmailAdress(self,email):
        self.driver.find_element_by_id(self.email_id).send_keys(email)
    def setOrderReference(self, orderReference):
        self.driver.find_element_by_id(self.orderReference_id).send_keys(orderReference)
    def setMessage(self,message):
        self.driver.find_element_by_id(self.message_id).send_keys(message)
    def selectSubjectHeading(self,subjectHeading):
        Select(self.driver.find_element_by_id(self.subjectHeading_id)).select_by_visible_text(subjectHeading)
    def clickSend(self):
        self.driver.find_element_by_id(self.send_id).click()
    def attachFile(self,file):
        self.driver.find_element_by_id(self.attachFile_id).send_keys(file)

