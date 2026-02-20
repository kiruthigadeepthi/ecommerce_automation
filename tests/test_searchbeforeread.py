from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_search_before_read(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Search for product
    inventory_page = InventoryPage(driver)
    product = inventory_page.search_product("Sauce Labs Backpack")

    # Step 3: Read product details
    assert product is not None, "Product not found"
    details = inventory_page.read_product_details(product)

    # Step 4: Verify details
    assert "Sauce Labs Backpack" in details