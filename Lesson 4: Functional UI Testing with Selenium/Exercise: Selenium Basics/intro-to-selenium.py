# #!/usr/bin/env python

# Basic usage of Selenium from Selenium website: (https://github.com/SeleniumHQ/seleniumhq.github.io/blob/trunk/examples/python/tests/getting_started/first_script.py#L12-L13)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

URL = "https://magento.softwaretestingboard.com/"
SEARCH_ITEM = "t-shirt"

print("Navigating to: " + URL)
driver.get(URL)

title = driver.title

driver.implicitly_wait(5)

search_box = driver.find_element(by=By.ID, value="search")

print("Search for: " + SEARCH_ITEM)
search_box.send_keys(SEARCH_ITEM)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button[class='action search']")
submit_button.click()

print("We are on the search page for: " + SEARCH_ITEM)

results = driver.find_element(by=By.CSS_SELECTOR, value="p[class='toolbar-amount']")

print("Results for the search: " + results.text + " were found.")

driver.quit()
