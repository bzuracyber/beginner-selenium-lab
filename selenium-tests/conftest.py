import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture(scope="session")
def driver():
    # Use environment variable to switch between local and CI
    selenium_url = os.getenv("SELENIUM_URL", "http://localhost:4444/wd/hub")
    base_url = os.getenv("JUICE_URL", "http://localhost:3000")

    options = webdriver.ChromeOptions()
    # Run headless in CI
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    options.set_capability("browserName", "chrome")

@pytest.fixture(scope="session")
def driver():
    base_url = os.getenv("JUICE_URL", "http://localhost:3000")
    if os.getenv("SELENIUM_URL"):
        options = webdriver.ChromeOptions()
        options.set_capability("browserName", "chrome")
        driver = webdriver.Remote(
            command_executor=os.getenv("SELENIUM_URL"),
            options=options
        )
    else:
        driver = webdriver.Chrome()
    driver.base_url = base_url
    yield driver
    driver.quit()