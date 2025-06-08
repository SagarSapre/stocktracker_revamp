'''import datetime, requests, zipfile, io, pandas as pd

day = datetime.date(2025, 6, 2)          # ← change as needed
folder = "cm"                            # "fo" for derivatives, etc.
url = (f"https://nsearchives.nseindia.com/content/{folder}/"
       f"BhavCopy_NSE_{folder.upper()}_0_0_0_{day:%Y%m%d}_F_0000.csv.zip")

resp = requests.get(url, timeout=30)
resp.raise_for_status()

with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
    df = pd.read_csv(zf.open(zf.namelist()[0]))
print(df.head())'''


import datetime
import os
import requests

def download_bhavcopy(
        date: datetime.date,
        segment: str = "cm",                 # "fo" for F&O, "cd" currency, etc.
        save_dir: str = "downloads") -> str:
    """
    Download the UDiFF Bhavcopy ZIP for `date` & `segment`
    and save it under `save_dir`.  Returns the local file path.
    """
    url = (
        f"https://nsearchives.nseindia.com/content/{segment}/"
        f"BhavCopy_NSE_{segment.upper()}_0_0_0_{date:%Y%m%d}_F_0000.csv.zip"
    )
    print(f"Downloading {url} ...")

    # ---- one reusable HTTP session ----
    session = requests.Session()
    session.headers.update({
        "User-Agent":
            ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
             "AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/124.0.0.0 Safari/537.36"),
        "Accept":
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.nseindia.com/",
        "DNT": "1",
        "Connection": "keep-alive",
    })

    # (Optional) Warm-up visit to get Akamai cookies – not needed for static CDN,
    # but harmless if you also hit JSON APIs later.
    # session.get("https://www.nseindia.com/", timeout=10)

    resp = session.get(url, timeout=30)
    resp.raise_for_status()          # raises if 404/403/etc.

    os.makedirs(save_dir, exist_ok=True)
    local_path = os.path.join(save_dir, url.rsplit("/", 1)[-1])

    with open(local_path, "wb") as fp:
        fp.write(resp.content)

    print(f"✅  Saved → {local_path}")
    return local_path


# -------------- example --------------
if __name__ == "__main__":
    trade_day = datetime.date(2025, 6, 2)
    download_bhavcopy(trade_day,
                      segment="cm",
                      save_dir=r"K:\Sagar_new\ORDER\00_Programming\python\projects\stocktracker_revamp\files\bhavcopy")


'''

old path https://archives.nseindia.com/content/historical/EQUITIES/2024/JUN/cm20JUN2024bhav.csv.zip
new path https://nsearchives.nseindia.com/content/cm/BhavCopy_NSE_CM_0_0_0_20250602_F_0000.csv.zip

'''