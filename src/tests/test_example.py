import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    
    driver.quit()

def test_title(driver):
    driver.get("https://testautomationpractice.blogspot.com/")

    driver.implicitly_wait(2)

    title = driver.title
    assert title == "Automation Testing Practice", f"Expected title to be 'Automation Testing Practice' bu got '{title}'"