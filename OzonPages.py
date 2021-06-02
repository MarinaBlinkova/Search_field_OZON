from BaseApp import BasePage
from selenium.webdriver.common.by import By


class OzonSeacrhLocators:
    LOCATOR_SEARCH_FIELD = (By.NAME, "search")
    LOCATOR_SEARCH_BUTTON = (By.CSS_SELECTOR, "button.b7j")
    LOCATOR_PRODUCT_TITLES = (By.CLASS_NAME, ".a0c6 a0d a0c9")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(OzonSeacrhLocators.LOCATOR_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(OzonSeacrhLocators.LOCATOR_SEARCH_BUTTON).click()




