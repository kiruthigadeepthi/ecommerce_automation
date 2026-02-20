from selenium.webdriver.common.by import By

class PaginationPage:
    def __init__(self, driver):
        self.driver = driver

    def get_items_on_page(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    def go_to_next_page(self):
        next_button = self.driver.find_element(By.ID, "next-page")
        if next_button.is_enabled():
            next_button.click()
            return True
        return False