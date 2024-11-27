from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:
    MENU_LINKS = (By.CSS_SELECTOR, "ul#menu-1-5dc673f1 > li > a")

    def __init__(self, driver):
        self.driver = driver

    def click_all_menu_links(self):

        links = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.MENU_LINKS)
        )
        for link in links:
            link_text = link.text
            print(f"Tıklanıyor: {link_text}")
            link.click()
            self.driver.back()
            links = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(self.MENU_LINKS)
            )
