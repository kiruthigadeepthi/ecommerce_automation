from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    assert "cart.html" in driver.current_url
    assert "Sauce Labs Backpack" in driver.page_source