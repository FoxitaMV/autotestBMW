from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest

class TestMainPageWork(unittest.TestCase):
	
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_title_header(self):
        driver = self.driver
        driver.get("https://demo.bmw.kodixauto.ru/")
        self.assertIn("Главная страница", driver.title)

    def test_header_find(self):
        driver = self.driver
        driver.get("https://demo.bmw.kodixauto.ru/")
        self = driver.find_element_by_class_name("main-header")
        header = driver.find_elements_by_class_name("main-header")
        if driver.find_elements_by_class_name("main-header") == header:
            print('Шапка есть')
        else:
            print('Шапки нет')
	
    def test_content_find(self):
        driver = self.driver
        driver.get("https://demo.bmw.kodixauto.ru/")
        self = driver.find_element_by_class_name("main-content")
        content = driver.find_elements_by_class_name("main-content")
        if driver.find_element_by_class_name("main-content") == content:
            print('Content есть!')
        else:
            print('Content нет')
        
    def test_stage_find(self):
        driver = self.driver
        driver.get("https://demo.bmw.kodixauto.ru/")
        self = driver.find_element_by_css_selector(".main-content > div:nth-child(1)")
        stage = driver.find_element_by_css_selector(".main-content > div:nth-child(1)")
        if driver.find_element_by_css_selector(".main-content > div:nth-child(1)") == stage:
            print('Element stage find!')
        else:
            print('Error')

    def test_cars_find(self):
        driver = self.driver
        driver.get("https://demo.bmw.kodixauto.ru/")
        self = driver.find_elements_by_css_selector(".main-content > div:nth-child(2)")
        cars = driver.find_element_by_css_selector(".main-content > div:nth-child(2)")
        if driver.find_element_by_css_selector(".main-content > div:nth-child(2)") == cars:
            print('Element cars find!')
        else:
            print('Error')
    
    def test_spc_find(self):
        driver = self.driver
        driver.get("https://demo.bmw.kodixauto.ru/")
        self = driver.find_elements_by_css_selector(".main-content > div:nth-child(3)")
        spc = driver.find_elements_by_css_selector(".main-content > div:nth-child(3)")
        if driver.find_elements_by_css_selector(".main-content > div:nth-child(3)") == spc:
            print('Element spc find!')
        else:
            print('Error!')


    def test_form_find(self):
        driver = self.driver
        driver.get("https://demo.bmw.kodixauto.ru/")
        self = driver.find_elements_by_css_selector(".main-content > div:nth-child(4)")
        form = driver.find_elements_by_css_selector(".main-content > div:nth-child(4)")
        if driver.find_elements_by_css_selector(".main-content > div:nth-child(4)") == form:
            print('Element form find!')
        else:
            print('Error!')
    
    def test_footer_find(self):
        driver = self.driver
        driver.get("https://demo.bmw.kodixauto.ru/")
        self = driver.find_elements_by_class_name("main-footer")
        footer = driver.find_elements_by_class_name("main-footer")
        if driver.find_elements_by_class_name("main-footer") == footer:
            print('Element footer find')
        else:
            print('Error!')

    def test_form_send(self):
        driver = self.driver
        driver.get("https://demo.bmw.kodixauto.ru/")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main()