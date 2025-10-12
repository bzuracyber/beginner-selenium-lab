from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigation_to_about_page(driver):
    driver.get(driver.base_url + "/#/")

    # Wait for the side menu toggle
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Open Sidenav']"))
    )
    menu_button.click()

    # Click the "About Us" link
    about_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[routerlink='/about']"))
    )
    about_link.click()

    # Assert the About page loaded
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "About Us" in driver.page_source