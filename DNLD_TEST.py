import time
t0 = time.time()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.options import ArgOptions 
from selenium.webdriver.common.by import By
# instance of Options class allows 
# us to configure Headless Chrome 
options = Options() 
  
# this parameter tells Chrome that 
# it should be run without UI (Headless) 
#options.headless = True |not working

options.add_argument('--ignore-certificate-errors')
from selenium.webdriver.chrome.service import Service 
#from webdriver.manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
'''
following error occurs sometimes
ERROR:cert_issuer_source_aia.cc(35)] Error parsing cert retrieved from AIA (as DER):
ERROR: Couldn't read tbsCertificate as SEQUENCE
ERROR: Failed parsing Certificate
hence following lines were added
options.add_argument('--ignore-certificate-errors')
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

'''



'''
import requests
import csv
from bs4 import BeautifulSoup
'''

url="https://www.python.org/downloads/"

driver = webdriver.Chrome()
driver.get(url)

title = driver.title
print(title)
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div/header/div/div[2]/div/div[2]/p/a').click()
time.sleep(3)



# date_field.send_keys(Keys.CONTROL + 'a')
# date_field.send_keys(Keys.DELETE)
# date_field.send_keys('02/01/2025')
# date_field.send_keys(Keys.TAB)


#print(f"cookiesvar is {cookiesvar}")

driver.quit()

t1 = time.time()
print(t1 - t0)