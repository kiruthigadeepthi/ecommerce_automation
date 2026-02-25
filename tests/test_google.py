def test_google(driver):
    driver.get("https://www.google.com")
    assert "Yahoo" in driver.title  