from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

def get_driver():

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get("https://testautomationpractice.blogspot.com/")

    driver.implicitly_wait(2)

    # explicit wait test
    # wait = WebDriverWait(driver, timeout=2)
    # wait.until(lambda d : revealed.is_displayed())

    return driver
