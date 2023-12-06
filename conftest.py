import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait



@pytest.fixture(scope='class')
def setup(request):
    webdriver_path = "D://Driver//chromedriver-win64//chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=webdriver_path, options=options)
    wait = WebDriverWait(driver, 10)
    # Launch the browser
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()












