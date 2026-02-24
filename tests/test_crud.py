from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By

def test_crud_operations(driver):
    # Step 1: CREATE → Add product to cart
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    items = cart_page.get_cart_items()
    assert "Sauce Labs Bolt T-Shirt" in items

    # Step 2: READ → Verify product is in cart
    assert len(items) == 1
    assert items[0] == "Sauce Labs Bolt T-Shirt"

    # Step 3: UPDATE → Remove backpack, add another product
    cart_page.remove_product()
    inventory_page.driver.get("https://www.saucedemo.com/inventory.html")
    inventory_page.driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light").click()
    inventory_page.go_to_cart()
    items = cart_page.get_cart_items()
    assert "Sauce Labs Bike Light" in items
    assert "Sauce Labs Bolt T-Shirt" not in items

    # Step 4: DELETE → Remove all items from cart
    inventory_page.driver.find_element(By.ID,"remove-sauce-labs-bike-light").click()
    items = cart_page.get_cart_items()
    assert len(items) == 0