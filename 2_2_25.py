import requests
url = "https://www.nseindia.com/all-reports"


headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"}


session = requests.Session()
session.headers.update(headers)

url = "https://www.nseindia.com"
session.get(url)  # Visit once to set cookies

response = session.get(url)
print(response.status_code, response.text[:500])


#cookie = response.cookies
#print(cookie)