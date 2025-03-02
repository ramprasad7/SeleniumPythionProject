from selenium.webdriver.common.by import By

from PageObjects.CheckOut_Confirmation import CheckOut_Confirmation
from utils.BrowserUtils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_button = (By.LINK_TEXT, "Shop")
        self.products_list = (By.XPATH, "//div/div/app-card-list/app-card")
        self.checkout = (By.CSS_SELECTOR, ".btn-primary")

    def add_prods_to_cart(self, product_name):
        self.driver.find_element(*self.shop_button).click()
        products = self.driver.find_elements(*self.products_list)
        # print(products)
        for product in products:
            item = product.find_element(By.XPATH, "div/div/h4/a").text
            if item == product_name: #"Blackberry":
                product.find_element(By.XPATH, "div/div/button").click()
                break

    def got_to_cart(self):
        self.driver.find_element(*self.checkout).click()
        checkout_confirm = CheckOut_Confirmation(self.driver)
        return checkout_confirm