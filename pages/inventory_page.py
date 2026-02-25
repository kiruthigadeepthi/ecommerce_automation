from selenium.webdriver.common.by import By
import time

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        time.sleep(2)
        #self.driver.find_element(By.LINK_TEXT, product).click()
        self.driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt").click()
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def search_product(self, product_name):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for product in products:
            if product.text == product_name:
                return product
        return None

    def read_product_details(self, product_element):
        return product_element.text
