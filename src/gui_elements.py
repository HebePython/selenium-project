from selenium.webdriver.common.by import By

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
    element = driver.find_element(By.ID, "male")
    element.click()