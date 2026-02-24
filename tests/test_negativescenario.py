from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By


def test_negative_checkout_missing_fields(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.checkout("", "", "")  

    error_message = driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3").text
    assert "First Name is required" in error_message
    #assert "Sauce Labs Bolt T-Shirt" in driver.page_source