from webdriver_manager.chrome import ChromeDriverManager
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

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://demo.bmw.kodixauto.ru/owners/vehicle-service-parts/service-form/") 
time.sleep(1)

class service(unittest.TestCase):
    

    try: 
        choices1 = driver.find_element_by_css_selector('div.form__section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        choices1.send_keys(Keys.ENTER)
        time.sleep(1)
        choices1.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        choices1.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        choices1.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        choices1.send_keys(Keys.ENTER)
        time.sleep(2)

    finally:
        link1 = driver.find_element_by_xpath('//*[@id="vin"]')
        link1.send_keys('12345678912345678')
        time.sleep(1)

        link2 = driver.find_element_by_xpath('//*[@id="year"]')
        link2.send_keys('2012')
        time.sleep(1)

    try:
        choices1 = driver.find_element_by_css_selector('div.form-element:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
        choices1.send_keys(Keys.ENTER)
        time.sleep(1)
        choices1.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        choices1.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        choices1.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        choices1.send_keys(Keys.ENTER)
        time.sleep(2)

    finally:
        link3 = driver.find_element_by_xpath('//*[@id="datepicker"]')
        link3.send_keys('20092019')
        time.sleep(3)

        time1 = driver.find_element_by_xpath('//*[@id="timepicker"]')
        time1.click()
        time1.send_keys('1231')
        time.sleep(1)

        gender = driver.find_element_by_css_selector('label.u116-00:nth-child(2)')
        gender.click()
        time.sleep(1)

        gender2 = driver.find_element_by_css_selector('label.u116-00:nth-child(1)')
        gender2.click()
        time.sleep(2)

        name = driver.find_element_by_xpath('//*[@id="name"]')
        name.send_keys('Иван')  
        time.sleep(1)

        lastname = driver.find_element_by_id('last_name')
        lastname.send_keys('Иванов')
        time.sleep(1)

        phone = driver.find_element_by_xpath('//*[@id="phone"]')
        phone.send_keys('9991234567')
        time.sleep(1)

        mail = driver.find_element_by_xpath('//*[@id="email"]')
        mail.send_keys('dmp@kodix.ru')
        time.sleep(1)

        var1 = driver.find_element_by_xpath('//*[@id="replacement_car"]')
        var1.click()
        time.sleep(1)

        var2 = driver.find_element_by_xpath('//*[@id="processing_of_personal_data"]')
        var2.click()
        time.sleep(1)

        btn = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div/div/div/div/div/div/div[2]/form/div/div[6]/div/button')
        btn.click()

    screenshot = driver.save_screenshot("img\service.png")
    time.sleep(5)
    from page_test import main
    driver.close()