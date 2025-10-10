import pytest
from selenium import webdriver
import tempfile

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")   # modern headless mode
    options.add_argument("--no-sandbox")     # required in CI
    options.add_argument("--disable-dev-shm-usage")  # avoid /dev/shm issues
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")  # unique profile dir

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
