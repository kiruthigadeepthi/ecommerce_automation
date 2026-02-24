from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_duplicate_product_creation(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add product twice
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.add_to_cart()  # attempt duplicate
    driver.save_screenshot("Duplicate.png")
    inventory_page.go_to_cart()

    # Step 3: Read cart items
    cart_page = CartPage(driver)
    items = cart_page.get_cart_items()

    # Step 4: Verify duplicate handling
    # SauceDemo only allows one instance of each product in cart
    assert items.count("Sauce Labs Bolt T-Shirt") == 1