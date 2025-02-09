from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from resources.constants import TEXT_BOX_INPUT_1

class HomePage:
        
        # Locators, CONSTANTS, use * to unpack tuples stored in constants
        WEEKDAYS_CHECKS = (By.ID, "day")
        COUNTRY_DROPDOWN = (By.ID, "country")
        COLORS_LIST = (By.ID, "colors")
        ANIMALS_LIST = (By.ID, "animals")
        NAME = (By.ID, "name")
        EMAIL = (By.ID, "email")
        PHONE = (By.ID, "phone")
        ADDRESS = (By.ID, "textarea")
        MALE_BOX = (By.ID, "male")
        FEMALE_BOX = (By.ID, "female")

        def __init__(self, driver):
            self.driver = driver

        def male_female_checkboxes(self, click_male):
            male_checkbox = self.driver.find_element(*self.MALE_BOX)
            female_checkbox = self.driver.find_element(*self.FEMALE_BOX)

            if click_male:
                male_checkbox.click()
            else:
                 female_checkbox.click()

        def gender_checkbox_selected(self, locator):
            element = self.driver.find_element(*locator)
            return element.is_selected()

        def input_text_boxes(self, text_list_input):
            name_element = self.driver.find_element(By.ID, "name")
            name_element.send_keys(text_list_input[0])

            email_element = self.driver.find_element(By.ID, "email")
            email_element.send_keys(text_list_input[1])

            phone_element = self.driver.find_element(By.ID, "phone")
            phone_element.send_keys(text_list_input[2])

            address_element = self.driver.find_element(By.ID, "textarea")
            address_element.send_keys(text_list_input[3])

        def get_name(self):
             return self.driver.find_element(*self.NAME).get_attribute("value")
        def get_email(self):
             return self.driver.find_element(*self.EMAIL).get_attribute("value")
        def get_phone(self):
             return self.driver.find_element(*self.PHONE).get_attribute("value")
        def get_address(self):
             return self.driver.find_element(*self.ADDRESS).get_attribute("value")

        def clear_text_box(self, locator):
            element = self.driver.find_element(*locator)
            element.clear()

        def get_text_box_max_length(self, locator):
            element = self.driver.find_element(*locator)
            maxlength = element.get_attribute("maxlength")
            return int(maxlength) if maxlength and maxlength.isdigit() else None

        
        def select_weekday(self, day):
             element = self.driver.find_element(By.ID, day)
             element.click()
         
        def is_weekday_selected(self, day):
             element = self.driver.find_element(By.ID, day)
             return element.is_selected() 

        def select_country(self, country):
            select = Select(self.driver.find_element(*self.COUNTRY_DROPDOWN))
            select.select_by_value(country)
        
        def select_color(self, color):
            select = Select(self.driver.find_element(*self.COLORS_LIST))
            select.select_by_visible_text(color)

        def select_animal(self, index):
            select = Select(self.driver.find_element(*self.ANIMALS_LIST))
            select.select_by_index(index)
            return select.first_selected_option.text