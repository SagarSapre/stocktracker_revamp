import datetime
import os
import requests

# ---------------------------------------------------------------------------
#  Helper: build the correct Bhavcopy URL for the requested trade-date
# ---------------------------------------------------------------------------
_CUTOFF = datetime.date(2024, 7, 5)          # last day on *legacy* format

def _make_url(date: datetime.date, segment: str) -> str:
    """Return the correct CDN URL for `date` and `segment` (“cm”, “fo”, …)."""
    segment = segment.lower()

    if date <= _CUTOFF:
        # ---------- legacy pattern: /content/historical/EQUITIES/YYYY/MMM/ -----------
        month_abbr = date.strftime("%b").upper()          # JUN, DEC, etc.
        return (
            "https://archives.nseindia.com/content/historical/EQUITIES/"
            f"{date:%Y}/{month_abbr}/cm{date:%d}{month_abbr}{date:%Y}bhav.csv.zip"
        )

    # ---------- UDiFF pattern (in use since 8 Jul 2024) ----------
    return (
        f"https://nsearchives.nseindia.com/content/{segment}/"
        f"BhavCopy_NSE_{segment.upper()}_0_0_0_{date:%Y%m%d}_F_0000.csv.zip"
    )

# ---------------------------------------------------------------------------
#  Main downloader
# ---------------------------------------------------------------------------
def download_bhavcopy(date: datetime.date,
                      segment: str = "cm",
                      save_dir: str = "downloads") -> str:
    """
    Download the Bhavcopy ZIP for `date` & `segment`.
    Automatically switches to the legacy path for trade dates ≤ 5 Jul 2024.
    Returns the local file path.
    """
    url = _make_url(date, segment)

    # One reusable session with “real” browser headers
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

    resp = session.get(url, timeout=30)
    resp.raise_for_status()        # raises on 404/403 so you know the file is missing

    os.makedirs(save_dir, exist_ok=True)
    local_file = os.path.join(save_dir, url.rsplit("/", 1)[-1])

    with open(local_file, "wb") as f:
        f.write(resp.content)

    print(f"✅  Saved → {local_file}")
    return local_file


# ------------------ example usage ------------------
if __name__ == "__main__":

    download_bhavcopy(datetime.date(2025, 6, 4),
                      segment="cm",
                      save_dir=r"K:\Sagar_new\ORDER\00_Programming\python\projects\stocktracker_revamp\files\bhavcopy")
