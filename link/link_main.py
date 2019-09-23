from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://demo.bmw.kodixauto.ru/") 
driver.implicitly_wait(5)

time.sleep(10)
htmlbody = driver.page_source
      
time.sleep(3)