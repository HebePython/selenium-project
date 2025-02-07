import pytest
from selenium import webdriver
from driver_setup import get_driver
from gui_elements import check_weekday_forms

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    
    driver.quit()

def test_title(driver):
    driver.get("https://testautomationpractice.blogspot.com/")

    driver.implicitly_wait(2)

    title = driver.title
    assert title == "Automation Testing Practice", f"Expected title to be 'Automation Testing Practice' bu got '{title}'"