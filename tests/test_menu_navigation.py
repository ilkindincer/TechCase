import unittest
from selenium import webdriver
from pages.menu_page import MenuPage


class TestMenuNavigation(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self._outcome = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://2nhaber.com/")
        self.driver.maximize_window()

    def test_menu_links(self):
        menu_page = MenuPage(self.driver)
        menu_page.click_all_menu_links()

    def tearDown(self):
        if any(error for (method, error) in self._outcome.errors):
            self.driver.save_screenshot("menu_navigation_failure.png")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
