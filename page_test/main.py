from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://demo.bmw.kodixauto.ru/") 
time.sleep(2)

def status_slider_check():
    if(driver.find_element_by_css_selector('.main-content > div:nth-child(1)')):
        ssc = "True"
    else:
        ssc = "False"
    print(ssc)
status_slider_check()
try:
    screenshot = driver.save_screenshot("\img\ssc.png")
finally:
    time.sleep(3)

def status_model_check():
    if(driver.find_element_by_css_selector('.main-content > div:nth-child(2)')):
        smc = "True"    
    else:
        smc = "False"
    print(smc)
status_model_check()
try:
    status_model_check = driver.find_element_by_css_selector('.main-content > div:nth-child(2)')
    driver.execute_script("arguments[0].scrollIntoView(true);", status_model_check)
    screenshot = driver.save_screenshot("\img\smc.png")
finally:
    time.sleep(3)

def status_spec_check():
    if(driver.find_element_by_css_selector('.main-content > div:nth-child(3)')):
        sspc = "True"
    else:
        sspc = "False"
    print(sspc)
status_spec_check()
try:
    status_spec_check = driver.find_element_by_css_selector('.main-content > div:nth-child(3)')
    driver.execute_script("arguments[0].scrollIntoView(true);", status_spec_check)
    screenshot = driver.save_screenshot("\img\sspc.png")
finally:
    time.sleep(3)

def status_form_check():
    if(driver.find_element_by_css_selector('.main-content > div:nth-child(4)')):
        sfc = "True"
    else:
        sfc = "False"
    print(sfc)
status_form_check()
try:
    status_form_check = driver.find_element_by_css_selector('.main-content > div:nth-child(4)')
    driver.execute_script("arguments[0].scrollIntoView(true);", status_form_check)
    screenshot = driver.save_screenshot("\img\sfc.png")
finally:
    time.sleep(3)

driver.close()