from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver 
import time
import math
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class FormService(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    
    def test_service_form_send(self): 
        driver = self.driver
        driver.maximize_window()
        driver.get("https://demo.bmw.kodixauto.ru/owners/vehicle-service-parts/service-form/") 
        self = driver.find_element_by_css_selector('div.form__section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        self.send_keys(Keys.ENTER)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ENTER)

        self = driver.find_element_by_xpath('//*[@id="vin"]')
        self.send_keys('12345678912345678')

        self = driver.find_element_by_xpath('//*[@id="year"]')
        self.send_keys('2012')


        self = driver.find_element_by_css_selector('div.form-element:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        self.send_keys(Keys.ENTER)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ARROW_DOWN)
        self.send_keys(Keys.ENTER)

        self = driver.find_element_by_xpath('//*[@id="datepicker"]')
        self.send_keys('20092019')

        self = driver.find_element_by_xpath('//*[@id="timepicker"]')
        self.click()
        self.send_keys('1231')

        self = driver.find_element_by_css_selector('label.u116-00:nth-child(2)')
        self.click()

        self = driver.find_element_by_css_selector('label.u116-00:nth-child(1)')
        self.click()

        self = driver.find_element_by_xpath('//*[@id="name"]')
        self.send_keys('Иван')  

        self = driver.find_element_by_id('last_name')
        self.send_keys('Иванов')

        self = driver.find_element_by_xpath('//*[@id="phone"]')
        self.send_keys('99978945612')

        self = driver.find_element_by_xpath('//*[@id="email"]')
        self.send_keys('dmp@kodix.ru')

        self = driver.find_element_by_xpath('//*[@id="replacement_car"]')
        self.click()

        self = driver.find_element_by_xpath('//*[@id="processing_of_personal_data"]')
        self.click()

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div/div/div/div/div/div/div[2]/form/div/div[6]/div/button')
        self.click()
        time.sleep(2)
        
        self = driver.find_element_by_css_selector('.f101-00-form__message')

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()