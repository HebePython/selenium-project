print("Welcome to selenium test")

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in your PATH

# Navigate to the specified URL
driver.get("https://testautomationpractice.blogspot.com/")

# Implicit wait
driver.implicitly_wait(2)

# explicit wait
# wait = WebDriverWait(driver, timeout=2)
# wait.until(lambda d : revealed.is_displayed())

# Find title element
title = driver.title
assert title 

# Close the WebDriver
driver.quit()