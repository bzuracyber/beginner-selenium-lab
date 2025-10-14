from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException


def dismiss_overlays(driver, wait):
    """Dismiss welcome modal and cookie banner if they appear."""
    # Dismiss welcome modal
    try:
        dismiss_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Dismiss')]"))
        )
        dismiss_btn.click()
        print("Dismissed welcome modal.")
    except TimeoutException:
        print("No welcome modal found.")

    # Dismiss cookie banner
    try:
        cookie_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Me want it!')]"))
        )
        cookie_btn.click()
        print("Dismissed cookie banner.")
    except TimeoutException:
        print("No cookie banner found.")


def test_invalid_login_shows_error(driver):
    driver.get(driver.base_url + "/#/login")
    wait = WebDriverWait(driver, 15)

    # --- Clear onboarding popups ---
    dismiss_overlays(driver, wait)

    # --- Fill login form ---
    email = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password = driver.find_element(By.ID, "password")

    email.clear()
    email.send_keys("fake@example.com")
    password.clear()
    password.send_keys("wrongpassword")

    # --- Click login button safely ---
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    ActionChains(driver).move_to_element(login_button).click().perform()

    # --- Wait for either snackbar or inline error ---
    possible_selectors = [
        (By.CSS_SELECTOR, "simple-snack-bar .mat-mdc-snack-bar-label"),
        (By.CSS_SELECTOR, "mat-error"),
        (By.XPATH, "//*[contains(text(),'Invalid email or password')]"),
        (By.XPATH, "//*[contains(text(),'Invalid')]"),
    ]

    error_element = None
    for selector in possible_selectors:
        try:
            element = wait.until(EC.visibility_of_element_located(selector))
            if element and element.text.strip():
                error_element = element
                break
        except TimeoutException:
            continue

    if not error_element:
        driver.save_screenshot("debug_no_error.png")
        print("DEBUG: No login error message found. Saved screenshot: debug_no_error.png")
        raise AssertionError("No invalid login error appeared after submitting the form.")

    print("Found login error message:", error_element.text)
    assert any(word in error_element.text.lower() for word in ["invalid", "error", "wrong"]), \
        f"Expected invalid login message, got: '{error_element.text}'"