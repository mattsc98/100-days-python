from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set the Chromedriver path (replace with your path)
chromedriver_path = r'C:\Users\matthew.schembri\OneDrive - Gain Changer\Documents\Automation\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Initialize the webdriver
driver = webdriver.Chrome(executable_path=chromedriver_path)

# Open the Cookie Clicker game
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Find the cookie element
cookie = driver.find_element(by=By.ID, value="cookie")

# Find upgrade item IDs
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

# Set timers
timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    # Click the cookie
    cookie.click()

    # Every 5 seconds
    if time.time() > timeout:
        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create a dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that can be afforded
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes, stop and check the cookies per second count
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

# Close the browser
driver.quit()
