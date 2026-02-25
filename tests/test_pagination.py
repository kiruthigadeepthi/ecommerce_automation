from pages.login_page import LoginPage
from pages.pagination import PaginationPage

def test_read_all_items_with_pagination(driver):
    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    pagination_page = PaginationPage(driver)
    all_items = []
    while True:
        items = pagination_page.get_items_on_page()
        all_items.extend(items)

        if not pagination_page.go_to_next_page():
            break

  
    assert len(all_items) > 0
    assert "Sauce Labs Backpack" in all_items