from OzonPages import SearchHelper
from OzonPages import OzonSeacrhLocators
from selenium.webdriver.support.wait import WebDriverWait

def test_ozon_search(browser):
    ozon_main_page = SearchHelper(browser)
    ozon_main_page.go_to_site()
    ozon_main_page.enter_word("Телефон")
    ozon_main_page.click_on_the_search_button()

    def product_titles(self):
        all_list = self.find_elements(OzonSeacrhLocators.LOCATOR_PRODUCT_TITLES)
        return len(all_list) > 0
    #WebDriverWait(browser, 5, 0.5).until(product_titles, "Количество результатов больше 0")

    #assert len(ozon_main_page.LOCATOR_PRODUCT_TITLES) > 0

