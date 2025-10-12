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

    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=options,
        desired_capabilities=DesiredCapabilities.CHROME
    )
    driver.base_url = base_url
    yield driver
    driver.quit()