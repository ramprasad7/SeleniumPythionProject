from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.BrowserUtils import BrowserUtils


class CheckOut_Confirmation(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, ".btn-success")
        self.country_input = (By.CSS_SELECTOR, ".validate")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox = (By.CSS_SELECTOR, "label[for='checkbox2']")
        self.purchase_button = (By.XPATH, "//input[@value='Purchase']")
        self.success_message = (By.CSS_SELECTOR, ".alert")

    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self, countryName):
        self.driver.find_element(*self.country_input).send_keys(countryName)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.purchase_button).click()


    def validate_order(self):
        output: str = self.driver.find_element(*self.success_message).text
        assert "Success!" in output
        print(output)