from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

class LinkClickTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        

    def test_link(self):
        driver = self.driver
        self.driver.get("https://demo.bmw.kodixauto.ru/")
        driver.fullscreen_window()
        links = []
        self.link = driver.find_elements_by_class_name("u107-00__btn")
        
        links = []
        for link in links:
            driver.click()
            driver.back()

       
            
    def tearDown(self):
        self.driver.close()
        
if __name__ == "__main__":
	unittest.main()