from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage


class AddProduct():
    def __init__(self,driver):
        self.driver = driver

    # Locators
    VIEWPRODUCTONE = "a[id='item_4_title_link'] div[class='inventory_item_name ']"
    PRODUCTONE = "button#add-to-cart-sauce-labs-backpack"
    BACKTOPRODUCT = "#back-to-products"
    VIEWPRODUCTWO = "a[id='item_0_title_link'] div[class='inventory_item_name ']"
    PRODUCTTWO = "button#add-to-cart-sauce-labs-bike-light"
    ADDPRODUCT = "//a[@class='shopping_cart_link']"
    SCROLLTOHOMEPAGE = "window.scrollBy(0,750)"
    BACKTOHOMEPAGE = "#continue-shopping"

    def getProductoView(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.VIEWPRODUCTONE)

    def getProductOne(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.PRODUCTONE)

    def getBackToProduct(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.BACKTOPRODUCT)

    def getProducttView(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.VIEWPRODUCTWO)

    def getProductTwo(self):
        return self.driver.find_element(By.CSS_SELECTOR , self.PRODUCTTWO)

    def getAddProduct(self):
        return self.driver.find_element(By.XPATH ,self.ADDPRODUCT)

    def getScrollToHomepage(self):
        return self.driver.execute_script(self.SCROLLTOHOMEPAGE)

    def getBackToHomepage(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.BACKTOHOMEPAGE)

    def enter_add_product(self):
        self.getProductoView().click()
        self.getProductOne().click()
        self.getBackToProduct().click()
        self.getProducttView().click()
        self.getProductTwo().click()
        self.getAddProduct().click()
        self.getScrollToHomepage()
        self.getBackToHomepage().click()
        add_and_checkout = CheckoutPage(self.driver)
        return add_and_checkout




