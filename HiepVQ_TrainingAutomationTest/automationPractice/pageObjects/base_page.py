# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# class Base_page:
#     def __init__(self, driver):
#         self.driver = driver
#     def getSearchResultMessage(self,second, find_element_method, locator_element):
#         find_element_method =
#         search_result_message = WebDriverWait(self.driver, second).until(
#             EC.presence_of_element_located((By.XPATH, self.locator.searchResultMessage_xpath))
#         )
#         return search_result_message.text