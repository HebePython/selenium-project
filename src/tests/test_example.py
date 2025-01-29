from selenium import webdriver
import unittest

class TestExample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # You can change this to the appropriate WebDriver for your browser
        self.driver.get("https://testautomationpractice.blogspot.com/")

    def test_title(self):
        self.assertIn("Practice", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()