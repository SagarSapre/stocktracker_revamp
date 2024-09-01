import time
t0 = time.time()
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.options import ArgOptions 
from selenium.webdriver.common.by import By
options = Options() 
options.add_argument('--ignore-certificate-errors')
from selenium.webdriver.chrome.service import Service 

url="https://www.moneycontrol.com/mutual-funds/find-fund/"

driver = webdriver.Chrome()
driver.get(url)

title = driver.title
print(title)
try:
    driver.find_element(By.ID, "wzrk-cancel").click()
except:
    pass
driver.find_element(By.CLASS_NAME, "right_block").click()
driver.find_element(By.CLASS_NAME, "activetick3").click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, '//*[@id="filter_tab3"]/div[1]/a[1]').click()
driver.find_element(By.CLASS_NAME, "activetick4").click()
time.sleep(2)





driver.quit()
t1 = time.time()
print(t1 - t0)