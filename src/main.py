from driver_setup import get_driver
from gui_elements import valid_text_box_inputs, test_check_labels
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

print("Welcome to selenium test")

driver = get_driver()

# Find title element
title = driver.title

# Find name, email, phone, address text_boxes
def main(driver):
    try:
        valid_text_box_inputs(driver)
        time.sleep(3)
        driver.refresh()
        test_check_labels(driver)
        time.sleep(3)

    except NoSuchElementException as e:
        print("UH OH")

    finally:
        driver.quit()


main(driver)