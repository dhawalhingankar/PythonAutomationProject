from selenium.webdriver.common.by import By
from pages.personal_details_page import PersonalDetails


class CheckoutPage():
    def __init__(self,driver):
        self.driver = driver

    # Locator
    ADDPRODUCT = ".shopping_cart_link"
    SCROLLBY = "window.scrollBy(0,750)"
    PRODUCTCHECKOUT = "#checkout"

    def getaddtocart(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.ADDPRODUCT)

    def getCheckoutScrollby(self):
        return self.driver.execute_script(self.SCROLLBY)

    def getCheckout(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.PRODUCTCHECKOUT)

    def enter_checkout_page(self):
        self.getaddtocart().click()
        self.getCheckoutScrollby()
        self.getCheckout().click()
        personal_details = PersonalDetails(self.driver)
        return personal_details


