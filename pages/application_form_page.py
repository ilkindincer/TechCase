from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ApplicationFormPage:
    # Locators
    NAME_INPUT = (By.ID, "name")
    BIRTH_DATE_INPUT = (By.ID, "birth")
    TC_INPUT = (By.ID, "tcKimlik")
    PHONE_INPUT = (By.ID, "phone")
    EMAIL_INPUT = (By.ID, "email")
    CV_INPUT = (By.ID, "cv_field")
    EDUCATION_BUTTONS = (By.CSS_SELECTOR, ".grid.grid-cols-3 button")
    KVKK_CHECKBOX = (By.NAME, "pdp1")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    NEXT_STEP_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Go to the next step']")
    NEXT_STEP_FORM = (By.CSS_SELECTOR, "form.next-step-class")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, name, birth_date, tc_number, phone, email, cv_path, education_level):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*self.BIRTH_DATE_INPUT).send_keys(birth_date)
        self.driver.find_element(*self.TC_INPUT).send_keys(tc_number)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.CV_INPUT).send_keys(cv_path)

        education_buttons = self.driver.find_elements(*self.EDUCATION_BUTTONS)
        for button in education_buttons:
            if education_level in button.text:
                button.click()
                break

        kvkk_checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.KVKK_CHECKBOX)
        )
        if not kvkk_checkbox.is_selected():
            kvkk_checkbox.click()

    def submit_form(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    def go_to_next_step(self):
        next_step_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NEXT_STEP_BUTTON)
        )
        next_step_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.NEXT_STEP_FORM)
        )
