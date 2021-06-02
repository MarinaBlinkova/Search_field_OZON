import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome("C:/Users/Dom/chromedriver_win32/chromedriver.exe")
    yield driver
    driver.quit()
