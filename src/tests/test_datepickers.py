import pytest
from pages import HomePage
from driver_setup import get_driver
from datetime import date


# creates driver instance, yields it to tests, then closes driver.
@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


def test_text_input_datepicker(driver):
    home_page = HomePage(driver)
    assert home_page.date_selector("02/02/2023"), f" Date should be 02/02/2023"

def test_pick_datepicker(driver):
    home_page = HomePage(driver)

def test_todays_date(driver):
    home_page = HomePage(driver)

    driver.refresh()
    home_page.open_date_picker()


    ret_year, ret_month, ret_day = home_page.check_today_date()

    exp_year = date.today().year
    exp_month = date.today().month - 1
    exp_day = date.today().day

    assert int(ret_year) == exp_year, f"Expected year {exp_year} but got {ret_year}"
    assert int(ret_month) == exp_month, f"Expected month {exp_month} but got {ret_month}"
    assert int(ret_day) == exp_day, f"Expected day {exp_day} but got {ret_day}"