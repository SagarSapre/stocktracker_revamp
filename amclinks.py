
import time
t0 = time.time()
from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.options import ArgOptions 
from selenium.webdriver.common.by import By
options = Options() 
options.add_argument('--ignore-certificate-errors')
from selenium.webdriver.chrome.service import Service 



url="https://www.moneycontrol.com/mutualfundindia/"
driver = webdriver.Chrome()
driver.get(url)

title = driver.title
print(title)
try:
    driver.find_element(By.ID, "wzrk-cancel").click()
except:
    pass
#finding div containing amc links
#amcdiv=driver.find_element(By.CLASS_NAME, "amclink")
amcdiv=driver.find_elements(By.XPATH, '//*[@id="mc_content"]/section[4]/div/div[2]/ul/li/a')
#amcdiv.find_element(By.CSS_SELECTOR #mc_content > section.select_amc.mob-hide > div > div.amclink > ul > li:nth-child(1) > a                    
#                    //*[@id="mc_content"]/section[4]/div/div[2]/ul/li[1]/a
# print (type(amcdiv))
linkdict={}

for i in amcdiv:
    link=i.get_attribute('href')
    text=i.get_attribute('text')
    linkdict[text] = link

heading = ['name','link']
driver.quit()
print (type(linkdict))
print ((linkdict.keys()))
print ((linkdict.values()))

with open('amcnames1.csv', 'w',newline='') as csvfile: # added newline='' to fix blank lines being added after everyline
    # https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
    writer = csv.writer(csvfile,dialect='excel')
    for items in linkdict.items():
        writer.writerow(items)

    # for items in linkdict.items():
    #     writer.writerow(items)
        #writer.writerows(zip(*linkdict.values()))