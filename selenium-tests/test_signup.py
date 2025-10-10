import time

def test_signup(driver):
    driver.get("http://localhost:3000/#/register")
    driver.find_element("id", "emailControl").send_keys("newuser@example.com")
    driver.find_element("id", "passwordControl").send_keys("StrongPass123!")
    driver.find_element("id", "repeatPasswordControl").send_keys("StrongPass123!")
    driver.find_element("id", "registerButton").click()
    time.sleep(2)
    assert "Registration completed" in driver.page_source
