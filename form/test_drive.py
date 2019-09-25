from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
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

class testDrive(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_testdrive_form_send(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://demo.bmw.kodixauto.ru/offers-and-services/test-drive/") 
        assert "Запись на тест-драйв" in driver.title

        self = driver.find_element_by_css_selector('.choices')
        self.send_keys(Keys.ENTER)
        time.sleep(1)
        self.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        self.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        self.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        self.send_keys(Keys.ENTER)
        time.sleep(2)

    
        self = driver.find_element_by_xpath('//*[@id="datepicker"]')
        self.send_keys('20092019')
        time.sleep(3)

        self = driver.find_element_by_xpath('//*[@id="timepicker"]')
        self.click()
        self.send_keys('1231')
        time.sleep(1)

        self = driver.find_element_by_css_selector('label.u116-00:nth-child(2)')
        self.click()
        time.sleep(1)

        self = driver.find_element_by_css_selector('label.u116-00:nth-child(1)')
        self.click()
        time.sleep(2)

        self = driver.find_element_by_xpath('//*[@id="name"]')
        self.send_keys('Иван')
        time.sleep(1)

        self = driver.find_element_by_id('last_name')
        self.send_keys('Иванов')
        time.sleep(1)

        self = driver.find_element_by_xpath('//*[@id="phone"]')
        self.send_keys('9991234567')
        time.sleep(1)

        self = driver.find_element_by_xpath('//*[@id="email"]')
        self.send_keys('dmp@kodix.ru')
        time.sleep(1)

        self = driver.find_element_by_xpath('//*[@id="processing_of_personal_data"]')
        self.click()
        time.sleep(1)

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div/div/div/div/div/div/div[2]/form/div/div[5]/div/button')
        self.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main()