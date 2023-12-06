from selenium.webdriver.common.by import By
from pages.add_product_page import AddProduct


class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    # Locators
    USERNAME = "input[id='user-name']"
    PASSWORD = "input[id='password']"
    LOGINBTN = "//input[@id='login-button']"

    def getUsername(self):
        return self.driver.find_element(By.CSS_SELECTOR ,self.USERNAME)

    def getPassword(self):
        return self.driver.find_element(By.CSS_SELECTOR ,self.PASSWORD)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH ,self.LOGINBTN)

    def enter_login_details(self,username,password):
        self.getUsername().send_keys(username)
        self.getPassword().send_keys(password)
        self.getLoginButton().click()
        add_product_page = AddProduct(self.driver)
        return add_product_page






