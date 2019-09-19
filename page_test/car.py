from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class car(unittest.TestCase):

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("https://demo.bmw.kodixauto.ru/all-models/bmw-x7/") 
    time.sleep(2)

    def status_slider_check():
        if(driver.find_element_by_css_selector('.main-content > div:nth-child(1)')):
            ssc = "True"
        else:
            ssc = "False"
        print(ssc)
    status_slider_check()
    try:
        screenshot = driver.save_screenshot("img\sscc.png")
    finally:
        time.sleep(1)

    def status_model_ico():
        if(driver.find_element_by_css_selector('.main-content > div:nth-child(2)')):
            smi = "True"    
        else:
            smi = "False"
        print(smi)
    status_model_ico()
    try:
        status_model_ico = driver.find_element_by_css_selector('.main-content > div:nth-child(2)')
        driver.execute_script("arguments[0].scrollIntoView(true);", status_model_ico)
        screenshot = driver.save_screenshot("img\smi.png")
    finally:
        time.sleep(1)

    def status_model_text():
        if(driver.find_element_by_css_selector('.main-content > div:nth-child(3)')):
            smt = "True"    
        else:
            smt = "False"
        print(smt)
    status_model_text()
    try:
        status_model_text = driver.find_element_by_css_selector('.main-content > div:nth-child(3)')
        driver.execute_script("arguments[0].scrollIntoView(true);", status_model_text)
        screenshot = driver.save_screenshot("img\smtext.png")
    finally:
        time.sleep(1)

    def status_model_pp():
        if(driver.find_element_by_css_selector('.main-content > div:nth-child(4)')):
            smpp = "True"    
        else:
            smpp = "False"
        print(smpp)
    status_model_pp()
    try:
        status_model_pp = driver.find_element_by_css_selector('.main-content > div:nth-child(4)')
        driver.execute_script("arguments[0].scrollIntoView(true);", status_model_pp)
        screenshot = driver.save_screenshot("img\smpp.png")
    finally:
        time.sleep(1)

    def status_model_q():
        if(driver.find_element_by_css_selector('.main-content > div:nth-child(5)')):
            smq = "True"    
        else:
            smq = "False"
        print(smq)
    status_model_q()
    try:
        status_model_q = driver.find_element_by_css_selector('.main-content > div:nth-child(5)')
        driver.execute_script("arguments[0].scrollIntoView(true);", status_model_q)
        screenshot = driver.save_screenshot("img\smq.png")
    finally:
        time.sleep(1)

    def status_model_b():
        if(driver.find_element_by_css_selector('.main-content > div:nth-child(6)')):
            smb = "True"    
        else:
            smb = "False"
        print(smb)
    status_model_b()
    try:
        status_model_b = driver.find_element_by_css_selector('.main-content > div:nth-child(6)')
        driver.execute_script("arguments[0].scrollIntoView(true);", status_model_b)
        screenshot = driver.save_screenshot("img\smb.png")
    finally:
        time.sleep(1) 

    def status_model_inn():
        if(driver.find_element_by_css_selector('div.ui:nth-child(7)')):
            sminn = "True"    
        else:
            sminn = "False"
        print(sminn)
    status_model_inn()
    try:
        status_model_inn = driver.find_element_by_css_selector('div.ui:nth-child(7)')
        driver.execute_script("arguments[0].scrollIntoView(true);", status_model_inn)
        screenshot = driver.save_screenshot("img\sminn.png")
    finally:
        time.sleep(1)

    def status_model_img():
        if(driver.find_element_by_css_selector('div.ui:nth-child(8)')):
            smimg = "True"    
        else:
            smimg = "False"
        print(smimg)
    status_model_img()
    try:
        status_model_img = driver.find_element_by_css_selector('div.ui:nth-child(8)')
        driver.execute_script("arguments[0].scrollIntoView(true);", status_model_img)
        screenshot = driver.save_screenshot("img\smimgs.png")
    finally:
        time.sleep(1)

    def status_model_form():
        if(driver.find_element_by_css_selector('div.ui:nth-child(9)')):
            smform = "True"
        elif(driver.find_element_by_css_selector('div.ui:nth-child(12)')):
            smform = "Другой ID"
        else:
            smform = "False"
        print(smform)
    status_model_form()
    try:
        status_model_form = driver.find_element_by_css_selector('div.ui:nth-child(9)')
        driver.execute_script("arguments[0].scrollIntoView(true);", status_model_form)
        screenshot = driver.save_screenshot("img\smform.png")
    finally:
        time.sleep(1)

    from page_test import car
    driver.close()