
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.logout_page import LogoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valid(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_sorting_and_products(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.sort_items("az")
    products = inventory.get_product_titles()
    assert len(products) > 0

def test_add_to_cart_and_checkout(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_to_cart()
    inventory.go_to_cart()
    CheckoutPage(driver).checkout("John", "Doe", "12345")
    assert "checkout-complete" in driver.current_url

def test_logout(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    LogoutPage(driver).logout()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
    assert driver.find_element(By.ID, "login-button").is_displayed()

@pytest.mark.parametrize("username,password", [
    ("standard_user", "wrong_pass"),
    ("locked_out_user", "secret_sauce"),
    ("", "secret_sauce"),
    ("standard_user", "")
])
def test_negative_login(driver, username, password):
    LoginPage(driver).login(username, password)
    assert "inventory" not in driver.current_url
