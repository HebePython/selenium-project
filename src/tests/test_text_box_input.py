import pytest
from pages import HomePage
from driver_setup import get_driver
from resources.constants import TEXT_BOX_INPUT_1

# field_name, locator, expected_max_length
TEXT_BOX_FIELDS = [
    ("name", HomePage.NAME, 15),     
    ("email", HomePage.EMAIL, 25),
    ("phone", HomePage.PHONE, 10),
    ("textarea", HomePage.ADDRESS, None),
]

# creates driver instance, yields it to tests, then closes driver.
@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("name, email, phone, address", [
    TEXT_BOX_INPUT_1,
    # add more data sets here if needed. 
])
def test_text_boxes_input(driver, name, email, phone, address):
    home_page = HomePage(driver)
    home_page.input_text_boxes(TEXT_BOX_INPUT_1)
    
    assert home_page.get_name() == name, "Incorrect name"
    assert home_page.get_email() == email, "Incorrect email"
    assert home_page.get_phone() == phone, "Incorrect phone number"
    assert home_page.get_address() == address, "Incorrect address"

@pytest.mark.parametrize("field_name, locator, expected_max", TEXT_BOX_FIELDS)
def test_text_box_max_length(driver, field_name, locator, expected_max):
    home_page = HomePage(driver)
    
    max_length = home_page.get_text_box_max_length(locator)
    if max_length is None:
        pytest.skip(f"No maxlength attribute defined for {field_name} field")

    assert max_length == expected_max, f"Expected length for {field_name} is {expected_max}, but got {max_length} "