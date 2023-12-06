import inspect
import logging
import softest
from webdriver_manager.core import driver
from selenium.webdriver.common.by import By

class Utils(softest.TestCase):
    def compare_texts(self, locator_1, locator_2):
            element_1 = driver.find_element(By.CSS_SELECTOR,"a[id='item_4_title_link'] div[class='inventory_item_name ']")
            element_2 = driver.find_element(By.CSS_SELECTOR,"a[id='item_0_title_link'] div[class='inventory_item_name ']")
            assert element_1 == element_2, f"Texts do not match: '{element_1}' != '{element_2}'"
            print("Texts match successfully!")

