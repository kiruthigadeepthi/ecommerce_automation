from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def test_list_refresh_after_delete(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    items_before = cart_page.get_cart_items()
    assert "Sauce Labs Bolt T-Shirt" in items_before

    # Step 3: Delete product
    cart_page.remove_product()

    # Step 4: Refresh list (re-read cart items)
    items_after = cart_page.get_cart_items()

    # Step 5: Validate list refresh
    assert "Sauce Labs Bolt T-Shirt" not in items_after
    assert len(items_after) == 0