from selenium.webdriver.common.by import By
from pages.finish_process import FinishProcess


class PersonalDetails():
    def __init__(self,driver):
        self.driver = driver

    #Locators
    SCROLLUP = "window.scrollBy(0,-150)"
    FIRSTNAME = "#first-name"
    LASTNAME = "#last-name"
    ADDRESS = "#postal-code"
    CONTINUEBUTTON = "#continue"

    def getScrollBy(self):
        return self.driver.execute_script(self.SCROLLUP)

    def getFirstName(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.FIRSTNAME)

    def getLastName(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.LASTNAME)

    def getAddress(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ADDRESS)

    def getContinueButton(self):
        return self.driver.find_element(By.CSS_SELECTOR , self.CONTINUEBUTTON)

    def enter_add_personal_details(self,firstname,lastname,address):
        self.getScrollBy()
        self.getFirstName().send_keys(firstname)
        self.getLastName().send_keys(lastname)
        self.getAddress().send_keys(address)
        self.getContinueButton().click()
        finish_process = FinishProcess(self.driver)
        return finish_process


