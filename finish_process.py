from selenium.webdriver.common.by import By

class FinishProcess():
    def __init__(self,driver):
        self.driver = driver

    # Locator
    SCROLLMIDDLE = "window.scrollBy(0,750)"
    FINISHBUTTON = "#finish"

    def getScrollMiddle(self):
        return self.driver.execute_script(self.SCROLLMIDDLE)

    def getFinishProcess(self):
        return self.driver.find_element(By.CSS_SELECTOR ,self.FINISHBUTTON)

    def enter_finish_process(self):
        self.getScrollMiddle()
        self.getFinishProcess().click()

