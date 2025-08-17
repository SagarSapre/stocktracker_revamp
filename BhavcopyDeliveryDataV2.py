import requests
from datetime import timedelta,datetime,date
import time
import random

def date_dt2(start, end='11-5-2021'): #def date_dt2(start, end='15-8-2025'):

    #end=datetime.today().strftime("%d-%m-%Y") if end == '15-8-2025' else end
    start=datetime.strptime(start, "%d-%m-%Y").date()
    end=datetime.strptime(end, "%d-%m-%Y").date()


    # Generate all days

    all_days = [end - timedelta(days=i) for i in range((end - start).days + 1)]

    # Business days only (skip weekends)
    business_days = [d.strftime("%d-%b-%Y") for d in all_days if d.weekday() < 5]  # 0=Mon, ..., 6=Sun

    with open('dates_datetimeFnRev.txt', "w") as f:
        for item in business_days:
            f.write(item+"\n")
    print(business_days)
    return business_days

# if __name__ == "__main__":
#     from datetime import timedelta,datetime
#     date_dt2('30-9-2019')






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
for date1 in date_dt2('30-9-2019', '11-5-2021'):
    url=f"https://www.nseindia.com/api/reports?archives=%5B%7B%22name%22%3A%22Full%20Bhavcopy%20and%20Security%20Deliverable%20data%22%2C%22type%22%3A%22daily-reports%22%2C%22category%22%3A%22capital-market%22%2C%22section%22%3A%22equities%22%7D%5D&date={date1}&type=equities&mode=single"
    folder=r"K:\Sagar_new\ORDER\00_Programming\python\projects\stocktracker_revamp\files\bhavcopy\Bhavcopy with delivery"
    try:
        resp = session.get(url, timeout=30)

        time.sleep(random.uniform(5, 10))  # To avoid hitting the server too frequently
    #print(resp.status_code)
    #print(resp.headers)
    #print(resp.text)
    #print(resp.content)
        if resp.status_code != 200:
            print(f"Failed to fetch data for {date1}: {resp.status_code}")
            continue
        file=f"{folder}//sec_bhavdata_full_{date1}.csv"
        with open(file, "wb") as f:
                f.write(resp.content)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {date1}: {e}")
        continue