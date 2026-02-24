from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_update_cart_items(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    # Step 3: Update (remove item)
    cart_page = CartPage(driver)
    cart_page.remove_backpack()

    # Step 4: Verify update
    items = cart_page.get_cart_items()
    assert "Sauce Labs Backpack" not in items