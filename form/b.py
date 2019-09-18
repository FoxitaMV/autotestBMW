from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver 
import time
import math

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://demo2.bmw.kodixauto.ru/owners/vehicle-service-parts/service-form/") 
time.sleep(2)

link1 = driver.find_element_by_xpath('//*[@id="vin"]')
link1.send_keys('12345678912345678')
time.sleep(1)

link2 = driver.find_element_by_xpath('//*[@id="year"]')
link2.send_keys('2012')
time.sleep(1)

link3 = driver.find_element_by_xpath('//*[@id="datepicker"]')
link3.send_keys('20092019')
time.sleep(3)

time1 = driver.find_element_by_xpath('//*[@id="timepicker"]')
time1.click()
time1.send_keys('1231')
time.sleep(1)

# gender = driver.find_element_by_xpath('//*[@id="gender-76674764"]')
# gender.click()
# time.sleep(1)

name = driver.find_element_by_xpath('//*[@id="name"]')
name.send_keys('Ivan')
time.sleep(1)

phone = driver.find_element_by_xpath('//*[@id="phone"]')
phone.send_keys('9991234567')
time.sleep(1)

mail = driver.find_element_by_xpath('//*[@id="email"]')
mail.send_keys('ivan@ivan.ivan')
time.sleep(1)

var1 = driver.find_element_by_xpath('//*[@id="replacement_car"]')
var1.click()
time.sleep(1)

var2 = driver.find_element_by_xpath('//*[@id="processing_of_personal_data"]')
var2.click()
time.sleep(1)

btn = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div/div/div/div/div/div/div[2]/form/div/div[6]/div/button')
btn.click()

time.sleep(5)
driver.close()