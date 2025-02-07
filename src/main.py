from driver_setup import get_driver
from gui_elements import valid_text_box_inputs, test_check_labels, check_weekday_forms
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
        check_weekday_forms(driver, "sunday")

    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    except TimeoutException as e:
        print(f"Timeout occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()


main(driver)