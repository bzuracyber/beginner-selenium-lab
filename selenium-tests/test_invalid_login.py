def test_invalid_login(driver):
    driver.get("http://localhost:3000/#/login")
    driver.find_element("id", "email").send_keys("fake@user.com")
    driver.find_element("id", "password").send_keys("wrongpass")
    driver.find_element("id", "loginButton").click()
    assert "Invalid email or password" in driver.page_source
