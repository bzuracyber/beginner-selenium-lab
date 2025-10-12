def test_homepage_title(driver):
    # Just open the homepage and check the title contains "Juice Shop"
    driver.get(driver.base_url + "/#/")

    assert "Juice Shop" in driver.title
