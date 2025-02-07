import pytest
from driver_setup import get_driver
from gui_elements import check_weekday_forms, drop_down_country, scroll_list_colors

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    
    driver.quit()

@pytest.mark.parametrize("day", ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"])
def test_weekday_forms(driver, day):
    check_weekday_forms(driver, day)

@pytest.mark.parametrize("country", ["usa", "canada", "uk", "germany", "france", "australia", "japan", "china", "brazil", "india"])
def test_drop_down(driver, country):
    drop_down_country(driver, country)

@pytest.mark.parametrize("color", ["Red", "Blue", "Green", "Yellow", "Red", "White", "Green"])
def test_color_list(driver, color):
    scroll_list_colors(driver, color)