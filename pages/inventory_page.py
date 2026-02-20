from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def add_product(self, product_id):
        self.driver.find_element(By.ID, f"add-to-cart-{product_id}").click()

    def remove_product(self, product_id):
        self.driver.find_element(By.ID, f"remove-{product_id}").click()
    def search_product(self, product_name):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for product in products:
            if product.text == product_name:
                return product
        return None

    def read_product_details(self, product_element):
        return product_element.text
