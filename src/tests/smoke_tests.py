import pytest
from pages import HomePage
from driver_setup import get_driver

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.smoke
def test_site_loads(driver):
    """Verify that the website loads successfully"""
    home_page = HomePage(driver)
    assert home_page.is_loaded()

@pytest.mark.smoke
def test_basic_navigation(driver):
    """Verify that main navigation works"""
    home_page = HomePage(driver)
    products_page = home_page.navigate_to_products()
    assert products_page.is_loaded()