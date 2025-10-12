def test_login(driver):
    driver.get(driver.base_url)
    # Example login flow
    driver.find_element("id", "navbarAccount").click()
    driver.find_element("id", "navbarLoginButton").click()
    driver.find_element("id", "email").send_keys("admin@juice-sh.op")
    driver.find_element("id", "password").send_keys("admin123")
    driver.find_element("id", "loginButton").click()
    assert "account" in driver.page_source.lower()
