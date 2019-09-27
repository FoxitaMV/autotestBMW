from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

class TestX1TestDrive(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def test_X1_testdrive(self):
        driver = self.driver
        driver.get("https://izar-avto.client.bmw.kodixauto.ru/")
        self.assertIn("Главная страница", driver.title)

        self = driver.find_element_by_xpath("/html/body/div[1]/header")
        self = driver.find_element_by_xpath("/html/body/div[1]/footer") 
        
        self = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[2]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/div[1]/div/div/div[5]/div/div/a")
        self.click()

        self = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div/div/div/div/div[2]/a")
        self.click()

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
        time.sleep(2)

        self = driver.find_element_by_xpath('//*[@id="processing_of_personal_data"]')
        self.click()
        time.sleep(1)

        self = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div/div/div/div/div/div/div[2]/form/div/div[6]/div/button')
        self.click()
        time.sleep(1)

        driver.back()

        self = driver.find_element_by_xpath("/html/body/div[1]/header")
        self = driver.find_element_by_xpath("/html/body/div[1]/footer")

        self = driver.find_element_by_css_selector("label.u116-00:nth-child(2)")
        self.click()

        self = driver.find_element_by_css_selector("label.u116-00:nth-child(1)")
        self.click()

        self = driver.find_element_by_css_selector("#name")
        self.send_keys("Петр")

        self = driver.find_element_by_css_selector("#phone")
        self.send_keys("9991234567")

        self = driver.find_element_by_css_selector("#email")
        self.send_keys("mail@example.com")
        time.sleep(2)

        self = driver.find_element_by_xpath('//*[@id="processing_of_personal_data"]')
        self.click()
        time.sleep(1)

        self = driver.find_element_by_css_selector("button.u107-00__btn")
        self.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
	unittest.main()