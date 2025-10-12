from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_product_to_basket(driver):
    # Use the base_url from conftest.py (set via JUICE_URL env var)
    driver.get(driver.base_url + "/#/")

    # Wait until the product grid is visible
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "mat-grid-tile"))
    )

    # Click the first "Add to Basket" button
    add_buttons = driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Add to Basket']")
    assert add_buttons, "No 'Add to Basket' buttons found on the page"
    add_buttons[0].click()

    # Wait for the basket counter to update
    basket_counter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.fa-layers-counter"))
    )

    # Assert that the basket counter shows '1'
    assert basket_counter.text.strip() == "1"