import requests

date="06-Aug-2025"
preurl="https://www.nseindia.com/all-reports"
url=f"https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22Full%20Bhavcopy%20and%20Security%20Deliverable%20data%22%2C%22type%22%3A%22daily-reports%22%2C%22category%22%3A%22capital-market%22%2C%22section%22%3A%22equities%22%7D%5D&date={date}&type=equities&mode=single"


session = requests.Session()
session.headers.update({
    "User-Agent":
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"),
    "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Origin": "https://www.nseindia.com",
    "Referer": "https://www.nseindia.com/reports",
    "DNT": "1",
    "Connection": "keep-alive",
})

session.get(preurl, timeout=30)

resp = session.get(url, timeout=30)

print(resp.status_code)
#print(resp.headers)
#print(resp.text)
#print(resp.content)



file="sec_bhavdata_full_"+date+".csv"
with open(file, "wb") as f:
        f.write(resp.content)