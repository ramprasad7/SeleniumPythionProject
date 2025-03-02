from selenium.webdriver.common.by import By

from PageObjects.ShopPage import ShopPage
from utils.BrowserUtils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signin = (By.ID, "signInBtn")
        self.driver = driver

    def login(self,userEmail,userPassword):
        self.driver.find_element(*self.username_input).send_keys(userEmail)
        self.driver.find_element(*self.password_input).send_keys(userPassword)
        self.driver.find_element(*self.signin).click()
        shop_page = ShopPage(self.driver)
        return shop_page