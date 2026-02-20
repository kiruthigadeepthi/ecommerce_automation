from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_checkout_flow(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.checkout("Kiru", "Ajith", "12345")

    confirmation = checkout_page.get_confirmation()
    assert "Thank you for your order" in confirmation

    summary_text = driver.page_source()
    assert "Sauce Labs Backpack" in summary_text
    assert "Kiru" in summary_text
    assert "Ajith" in summary_text
    assert "12345" in summary_text

def test_e2e_purchase(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    try:
        assert "inventory.html" in driver.current_url
    except AssertionError:
        driver.save_screenshot("screenshots/login_failure.png")
        raise

