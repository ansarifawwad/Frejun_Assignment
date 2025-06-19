
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def sort_items(self, option):
        select = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value(option)

    def get_product_titles(self):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [product.text for product in products]

    def add_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
