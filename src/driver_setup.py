import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    
    # Use headless mode if environment variable is set
    if os.environ.get('SELENIUM_HEADLESS', 'false').lower() == 'true':
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://testautomationpractice.blogspot.com/")
    
    driver.maximize_window()
    
    driver.implicitly_wait(2)
    
    return driver
