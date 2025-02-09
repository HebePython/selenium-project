import pytest
from pages import HomePage
from driver_setup import get_driver
from resources.constants import COUNTRIES, COLORS, ANIMAL_INDEXES

# creates driver instance, yields it to tests, then closes driver.
@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("country", COUNTRIES)
def test_select_country(driver, country):
    home_page = HomePage(driver)
    home_page.select_country(country)


@pytest.mark.parametrize("color", COLORS)
def test_color_list(driver, color):
    home_page = HomePage(driver)
    home_page.select_color(color)

@pytest.mark.parametrize("index", ANIMAL_INDEXES)
def test_sorted_animals_list(driver, index):
    home_page = HomePage(driver)
    home_page.select_animal(index)
