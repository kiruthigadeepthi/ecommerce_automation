from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        items = self.driver.find_element(By.LINK_TEXT, "Sauce Labs Bolt T-Shirt")
        return items
        #lists=list.append()
           
    def remove_backpack(self):
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
