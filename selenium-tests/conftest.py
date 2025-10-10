import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # run in CI without GUI
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
