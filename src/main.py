print("Welcome to selenium test")

from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in your PATH

# Navigate to the specified URL
driver.get("https://testautomationpractice.blogspot.com/")

# Close the WebDriver
driver.quit()