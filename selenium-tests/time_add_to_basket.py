import time

def test_add_product_to_basket(driver):
    # Go to Juice Shop homepage
    driver.get("http://localhost:3000/#/")

    # Wait briefly for products to load
    time.sleep(2)

    # Click on the first "Add to Basket" button
    add_buttons = driver.find_elements("css selector", "button[aria-label='Add to Basket']")
    assert len(add_buttons) > 0, "No products found on homepage"
    add_buttons[0].click()

    # Open the basket
    basket_button = driver.find_element("css selector", "button[aria-label='Show the shopping cart']")
    basket_button.click()

    # Verify that the basket contains at least one item
    time.sleep(1)
    basket_items = driver.find_elements("css selector", "mat-row")
    assert len(basket_items) > 0, "Basket should contain at least one product"