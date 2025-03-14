import pytest
from pages import HomePage
from driver_setup import get_driver
from datetime import date
from resources.constants import MONTHS
import time

# creates driver instance, yields it to tests, then closes driver.
@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

#region test suite for Date Picker 1
@pytest.mark.new_feature
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

    # '- 1' to month because Jan = 0 on website.
    exp_year = date.today().year
    exp_month = date.today().month - 1
    exp_day = date.today().day

    assert int(ret_year) == exp_year, f"Expected year {exp_year} but got {ret_year}"
    assert int(ret_month) == exp_month, f"Expected month {exp_month} but got {ret_month}"
    assert int(ret_day) == exp_day, f"Expected day {exp_day} but got {ret_day}"


def test_month_buttons(driver):
    home_page = HomePage(driver)

    cur_year, cur_month = home_page.datepicker_title()

    assert cur_month == date.today().strftime("%B")
    assert int(cur_year) == date.today().year
    #TODO first, look at what month & year is currently selected
    #     second, press button next or prev
    #     third, check that new current month & year has correctly changed.

    home_page.datepicker_month_button("prev")

    

    time.sleep(5)

    # assert cur_month == 

    home_page.datepicker_month_button("next")

    time.sleep(5)



#endregion