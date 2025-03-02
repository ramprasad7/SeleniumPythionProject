import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.ShopPage import ShopPage
from PageObjects.login import LoginPage

test_data_path = "Data/test_firstFrameWork.json"

with open(test_data_path) as fd:
    test_data = json.load(fd)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_parameters",test_list)
def test_end_to_end(browserInvocation,test_parameters):
    driver = browserInvocation
    loginpage = LoginPage(driver)
    print(loginpage.getTitle())
    shop_page = loginpage.login(test_parameters["userEmail"],test_parameters["userPassword"])
    print(shop_page.getTitle())
    shop_page.add_prods_to_cart(test_parameters["productName"])
    checkout_confirmation = shop_page.got_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Ind")
    checkout_confirmation.validate_order()





