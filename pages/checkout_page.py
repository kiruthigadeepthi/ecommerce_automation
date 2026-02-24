from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()
        #self.driver.find_element(By.ID, "finish").click()

    def get_confirmation(self):
        return self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/h2").text
    
    def get_errormessage(self):
        return self.driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']").text