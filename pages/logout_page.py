
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def logout(self):
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
