import requests
from bs4 import BeautifulSoup
url="https://www.moneycontrol.com/mutualfundindia/"

r = requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r, 'html.parser')

#amcdiv=driver.find_elements(By.XPATH, '//*[@id="mc_content"]/section[4]/div/div[2]/ul/li/a')