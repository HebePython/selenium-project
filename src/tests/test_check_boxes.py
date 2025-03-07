import pytest
from pages import HomePage
from driver_setup import get_driver
from resources.constants import WEEKDAYS

# creates driver instance, yields it to tests, then closes driver.
@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_gender_checkboxes(driver):
    home_page = HomePage(driver)
    home_page.male_female_checkboxes(True)
    
    assert home_page.gender_checkbox_selected(HomePage.MALE_BOX), f"Male checkbox should be selected"
    assert not home_page.gender_checkbox_selected(HomePage.FEMALE_BOX), f"Female checkbox should NOT be selected"

    home_page.male_female_checkboxes(False)

    assert not home_page.gender_checkbox_selected(HomePage.MALE_BOX), f"Male checkbox should NOT be selected"
    assert home_page.gender_checkbox_selected(HomePage.FEMALE_BOX), f"Female checkbox should be selected"

# checks and unchecks weekday checkboxes, also checks if they are checked and unchecked.
@pytest.mark.parametrize("day", WEEKDAYS)
def test_weekdays(driver, day):
    home_page = HomePage(driver)
    home_page.select_weekday(day)
    assert home_page.is_weekday_selected(day), f"{day} checkbox should be selected"
    home_page.select_weekday(day)
    assert not home_page.is_weekday_selected(day), f"{day} checkbox should NOT be selected"
