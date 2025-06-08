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

url="https://www.nseindia.com/all-reports"

driver = webdriver.Chrome()
driver.get(url)

title = driver.title
print(title)
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="Archives_rpt"]').click()
time.sleep(3)
date_field=driver.find_element(By.XPATH, '//*[@id="cr_equity_archives"]/div/div[1]/div[2]/div/div/div[2]/span/button')
date="02-Jan-2025"
date_field.click()
time.sleep(3)

# date_field.send_keys(Keys.CONTROL + 'a')
# date_field.send_keys(Keys.DELETE)
# date_field.send_keys('02/01/2025')
# date_field.send_keys(Keys.TAB)

driver.execute_script(f"""arguments[0].value='{date}';arguments[0].dispatchEvent(new Event('input')); 
        arguments[0].dispatchEvent(new Event('change'));""",date_field)
time.sleep(3)
print("Updated value:", date_field.get_attribute("value"))


CHECK=driver.find_element(By.XPATH, '//*[@id="cr_equity_archives"]/div/div[3]/div[27]/div/div/label/span').click
dnbtn=driver.find_element(By.XPATH, '//*[@id="cr_equity_archives"]/div/div[2]/div/a').click
cookiesvar=driver.get_cookies()
#print(f"cookiesvar is {cookiesvar}")
time.sleep(3)
driver.quit()

t1 = time.time()
print(t1 - t0)

'''
https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22CM-UDiFF%20Common%20Bhavcopy%20Final%20(zip)%22%2C%22type%22%3A%22daily-reports%22%2C%22category%22%3A%22capital-market%22%2C%22section%22%3A%22equities%22%7D%5D&date=02-Jan-2025&type=equities&mode=single
'''
'''

https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22CM-UDiFF%20Common%20Bhavcopy%20Final%20(zip)%22%2C%22type%22%3A%22daily-reports%22%2C%22category%22%3A%22capital-market%22%2C%22section%22%3A%22equities%22%7D%5D&date=26-Dec-2024&type=equities&mode=single
'''