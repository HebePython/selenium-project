from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://testautomationpractice.blogspot.com/")

    driver.maximize_window()

    driver.implicitly_wait(2)

    # explicit wait, don't mix with implicit.
    # wait = WebDriverWait(driver, timeout=2)
    # wait.until(lambda d : revealed.is_displayed())

    return driver
