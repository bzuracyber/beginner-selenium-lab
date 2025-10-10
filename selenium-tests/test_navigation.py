def test_navigation(driver):
    driver.get("http://localhost:5000/")
    driver.find_element("link text", "Login").click()
    assert "Login" in driver.page_source
