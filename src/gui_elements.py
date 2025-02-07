from selenium.webdriver.common.by import By

# EX + explicit waits, dont mix with implicit
from expected_conditions import wait_for_element 
from expected_conditions import wait_for_element_to_be_clickable


def text_box(driver):

    driver.find_element(By.ID, "name")



