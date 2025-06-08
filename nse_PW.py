import time
t0 = time.time()
from playwright.sync_api import sync_playwright
# url="https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
url="https://www.nseindia.com/all-reports"
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url,wait_until="domcontentloaded")# wait_until="domcontentloaded" as it is throwing error "Timeout 30000ms exceeded." waiting until "load" =default
    print(page.title())
    browser.close()

t1 = time.time()
print(t1 - t0)