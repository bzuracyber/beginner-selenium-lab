def test_contact_form_validation(driver):
    driver.get("http://localhost:3000/#/contact")
    driver.find_element("id", "submitButton").click()
    assert "Please provide an email address" in driver.page_source
