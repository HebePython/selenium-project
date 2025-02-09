from driver_setup import get_driver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pages import date_selector
import time

print("Welcome to selenium test")

driver = get_driver()

# Find title element
title = driver.title

# 
def main(driver):
    try:
        print("PLACEHOLDER")
        date_selector(driver, "02/03/2025")
    except NoSuchElementException as e:
        print(f"Element not found: {e}")
    except TimeoutException as e:
        print(f"Timeout occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        driver.quit()


main(driver)