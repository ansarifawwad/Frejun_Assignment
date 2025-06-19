
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def checkout(self, fname, lname, postal):
        self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        self.driver.find_element(By.ID, "checkout").click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
        self.driver.find_element(By.ID, "first-name").send_keys(fname)
        self.driver.find_element(By.ID, "last-name").send_keys(lname)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal)
        self.driver.find_element(By.ID, "continue").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        self.driver.find_element(By.ID, "finish").click()
