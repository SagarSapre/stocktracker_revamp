import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = Options()
options.add_argument('--ignore-certificate-errors')

# Initialize WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Open the target URL
    url = "https://www.nseindia.com/all-reports"
    driver.get(url)

    # Wait for the page to load and click on the "Archives" dropdown
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="Archives_rpt"]'))
    ).click()
    time.sleep(2)

    # Locate and click the date picker to open the calendar
    date_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="cr_equity_archives"]/div/div[1]/div[2]/div/div/div[2]/span/button'))
    )
    date_field.click()
    time.sleep(2)

    # Example: Navigate to the specific month/year (if required)
    # Locate and click the "Next Month" button (adjust XPath based on your calendar)
    
    time.sleep(2)

    # Select the specific date (update XPath based on your calendar structure)
    specific_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//td[contains(text(), '2') and @data-date='2025-01-02']"))  # Update as needed
    )
    specific_date.click()
    time.sleep(2)

    # Verify the date is selected (if applicable)
    selected_date = date_field.get_attribute("value")
    print("Selected date:", selected_date)

finally:
    # Quit the browser
    driver.quit()
