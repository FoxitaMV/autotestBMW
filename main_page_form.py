import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://demo.bmw.kodixauto.ru/") 
time.sleep(2)

class main_page_form(unittest.TestCase):

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

    try:
        choices1 = driver.find_element_by_css_selector('.choices')
        choices1.send_keys(Keys.ENTER)
        time.sleep(1)
        choices1.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        choices1.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        choices1.send_keys(Keys.ENTER)
        time.sleep(1)

    finally:
        textarea = driver.find_element_by_id('text')
        textarea.send_keys('МОДЕЛЬНЫЙ РЯД BMW')
        time.sleep(1)

        var2 = driver.find_element_by_xpath('//*[@id="processing_of_personal_data"]')
        var2.click()
        time.sleep(1)

        btn = driver.find_element_by_css_selector('button.u107-00__btn > span:nth-child(1)')
        btn.click()

    time.sleep(5)
    screenshot = driver.save_screenshot("img\main_page.png")
    from form import test_drive
    driver.close()