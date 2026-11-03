import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login():
    # 1. Start the Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # 2. Go to the SauceDemo login page
        driver.get("https://www.saucedemo.com/")

        # 3. Find the Username box and type 'standard_user'
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys("standard_user")

        # 4. Find the Password box and type 'secret_sauce'
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("secret_sauce")

        # 5. Click the Login button
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        # 6. Wait 2 seconds for the page to load
        time.sleep(2) 
        
        # 7. Check if we successfully logged in by looking for the title "Products"
        page_source = driver.page_source
        assert "Products" in page_source, "Login failed! Could not find the dashboard."

    finally:
        # 8. Always close the browser when done
        driver.quit()