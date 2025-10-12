from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login_shows_error(driver):
    driver.get(driver.base_url + "/#/login")

    email = driver.find_element(By.ID, "email")
    password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "loginButton")

    email.send_keys("fake@example.com")
    password.send_keys("wrongpassword")
    login_button.click()

    # Wait for error message
    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.error"))
    )
    assert "Invalid" in error.text or "Invalid" in driver.page_source
