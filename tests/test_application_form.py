import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.application_form_page import ApplicationFormPage
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestApplicationForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://2ntech.com.tr/hr")
        self.driver.maximize_window()

    def test_fill_and_submit_form(self):
        form_page = ApplicationFormPage(self.driver)

        name = "Test"
        birth_date = "1993-03-03"
        tc_number = "12134567665"
        phone = "05503647382"
        email = "test@example.com"
        cv_path = os.path.abspath("test_cv.pdf")
        education_level = "Lisans"

        form_page.fill_form(name, birth_date, tc_number, phone, email, cv_path, education_level)

        form_page.go_to_next_step()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form.next-step-class"))
        )

    def tearDown(self):
        if hasattr(self, '_outcome') and any(error for _, error in self._outcome.errors):
            self.driver.save_screenshot("form_submission_failure.png")
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
