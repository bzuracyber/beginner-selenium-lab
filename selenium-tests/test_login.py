from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login(driver):
    driver.get("http://localhost:5000/login")
    driver.find_element("name", "username").send_keys("testuser")
    driver.find_element("name", "password").send_keys("password123")
    driver.find_element("tag name", "button").click()
    assert "Welcome, testuser!" in driver.page_source
