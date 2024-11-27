import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.search_page import SearchPage


class TestSearchPopup(unittest.TestCase):
    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self._outcome = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://2nhaber.com/")
        self.driver.maximize_window()

    def test_search_popup(self):
        search_page = SearchPage(self.driver)
        search_page.open_search_popup()
        search_page.search("istanbul")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cmsmasters-blog__posts"))
        )
        posts = self.driver.find_elements(By.CSS_SELECTOR, ".cmsmasters-blog__posts .cmsmasters-blog__post")
        print(f"Bulunan makale sayısı: {len(posts)}")

        if len(posts) >= 8:
            eighth_post = posts[7]  # 8. post (0'dan başlar)
            animation_element = eighth_post.find_element(By.CSS_SELECTOR, ".cmsmasters-animation")
            print(f"8. Makale Başlığı: {animation_element.text}")
        else:
            print("Yeterli makale bulunamadı.")

    def tearDown(self):
        if any(error for (method, error) in self._outcome.errors):
            self.driver.save_screenshot("search_popup_failure.png")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
