from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

# EX + explicit waits, dont mix with implicit
from expected_conditions import wait_for_element, wait_for_element_to_be_clickable


def valid_text_box_inputs(driver):
    element = driver.find_element(By.ID, "name")
    element.send_keys("Henrik")

    element = driver.find_element(By.ID, "email")
    element.send_keys("henrik.b@gmail.com")

    element = driver.find_element(By.ID, "phone")
    element.send_keys(12345678)

    element = driver.find_element(By.ID, "textarea")
    element.send_keys("33C, Lexington drive")

def test_check_labels(driver):
    male_element = driver.find_element(By.ID, "male")
    female_element = driver.find_element(By.ID, "female")

    male_element.click()
    assert male_element.is_selected(), "Male checkbox should be selected"
    assert not female_element.is_selected(), "Female checkbox should not be selected"

    female_element.click()
    assert female_element.is_selected(), "Female checkbox should be selected"
    assert not male_element.is_selected(), "Male checkbox should not be selected"


def check_weekday_forms(driver, day):
    checkbox_element = driver.find_element(By.ID, day)

    checkbox_element.click()

    assert checkbox_element.is_selected(), f"{day.capitalize()} checkbox should be selected"

    checkbox_element.click()

    assert not checkbox_element.is_selected(), f"{day.capitalize()} checkbox should not be selected"


def drop_down_country(driver, country):
    select = Select(driver.find_element(By.ID, "country"))

    select.select_by_value(country)

    selected_value = select.first_selected_option.get_attribute("value")
    assert selected_value == country, f"{country} selection should be selected"

def scroll_list_colors(driver, color):
    select = Select(driver.find_element(By.ID, "colors"))

    select.select_by_visible_text(color)

    selected_text = select.first_selected_option.text
    assert selected_text == color, f"Expected color is {color}, but got {selected_text}"

    if select.is_multiple:
        select.deselect_all()

        assert len(select.all_selected_options) == 0, "No color should be selected"
    else:
        print("list does not suppoert multiple selections, cannot deselect")