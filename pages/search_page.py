from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SearchPage(BasePage):
    # Locators
    POPUP_TRIGGER = (By.CLASS_NAME, "elementor-widget-cmsmasters-search__popup-trigger-container")
    SEARCH_FIELD = (By.CLASS_NAME, "elementor-widget-cmsmasters-search__field")

    def open_search_popup(self):
        self.click_element(self.POPUP_TRIGGER)

    def search(self, query):

        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_FIELD)
        )

        ActionChains(self.driver).move_to_element(search_input).perform()

        search_input.send_keys(query)
        search_input.send_keys("\n")
