import pytest
from driver_setup import get_driver
from gui_elements import check_weekday_forms

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    
    driver.quit()

@pytest.mark.parametrize("day", ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"])
def test_weekday_forms(driver, day):
    check_weekday_forms(driver, day)