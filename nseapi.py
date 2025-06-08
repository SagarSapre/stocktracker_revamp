import requests


url = "https://www.nseindia.com/api/reports"

querystring = {"archives":"[{\"name\":\"CM-UDiFF Common Bhavcopy Final (zip)\",\"type\":\"daily-reports\",\"category\":\"capital-market\",\"section\":\"equities\"}]","date":"16-Oct-2024","type":"equities","mode":"single"}

payload = ""
headers = {
    "cookie": "nsit=wmDTzZKQeusMaOCgdpmsHRGD; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcyOTkyNjE3NiwiZXhwIjoxNzI5OTMzMzc2fQ.-GsBHUrvihDcp1dvAO49g_ZmOmj25_Gljnv-9ldKOhM; _abck=642407083FA45C03C1D08DE85AF3B451~-1~YAAQF1M2F7aPsXCSAQAAzB6ixwxvrdsj6ET%2BAfpRWDpC%2BknKsTtrrHKZSE61SeVMxqlebpr3iIiArKDbuKpiO9%2B6LyNe5ALdxyKK2ec0WYdU8V1bRs6FROM75Ix52PwyzfP81fzS%2Bxy%2FnV8Nppt8PpqL2CPyyYcsBguvJlY4JgaLJdwmJ2GaPDN03OhSdVGjpw8chn0CMoxa3ykF1wref%2FQmO9x38KIXLshuXP7%2F3JkZ9VKdgJmG9zMYskJFFUGPcfIWLOcC78utzNjs1PnjiMFmkCXGwN1mV%2B6nF0p8jM9QCL77wSVvx5VAK%2FoRxrsu9ZXIybDEWeF7BgSUTxcXCwWCVbUADF%2BBDgXRHQCqvmcF6PAL1xLbqGs84M3%2BLKM8Jesgw%2FEaRpotFImaU3iFPFmOpvlT6NpwvZkhog%3D%3D~-1~-1~-1; bm_sz=559501B39083983294B4084589902098~YAAQF1M2F7ePsXCSAQAAzB6ixxmLI4uNsBlQVy7M8r3EbDYuyXyanv7EkdYWJCTpW0MuL4JhtcvtT0%2FuHJdPbdRZp3EPOYNXTh2Lnq5Y1WYeWdcEVmmW0HiAKdu4%2FkBiCIkoib92VkORUJn2pkNSZvcH8oEg%2FtmpPC9RrT3FwAyekqp4ztoAZc2SRmSk%2Bh19LS3m9U78f%2BRRdCTZo%2F3C5xZTslcEV%2BXIu5QvlAo%2FR3H%2BQk%2BO8Y9VMa5HIevhRP8SkUrJ%2F1mlcv50tCJtQVDR2sKEcVErPs6ph8GUsKzbITWrudl3FJMrOdoDK0heqacZSAtSA%2BZ9hCRqet7hp%2Fxk2fItIU1LuYrNBrLI01G%2Ff7ErHNHLbyGS~3556661~4535877",
    "^accept": "*/*^",
    "^accept-language": "en-US,en;q=0.9,hi;q=0.8^",
    "^cache-control": "no-cache^",
    "^cookie": "defaultLang=en; _ga=GA1.1.279452972.1724546327; _abck=F150EE5178F818BCDA870A4A6EAC7CA7~0~YAAQvFI2F5/6rXGSAQAA1AvUxgzhZFyFTAhgBBwc3iwppMBjDKDyklF8mLe/Ogam5o944UEV+bMSSVBSNz6N9ABeCLKqzsIeniMK8CTPVR41ZR/7bz711NboTyXVsD0lD+puBX5PMIK+KwznSp7Yb9ivglbvZNAXoAxB3qILxb7+b1LdiK6VbUho0Pg/K2DAAXcJ7IhhtvnwSZG7dRIfpHfFvMmhJ/McajsPhoj80RmeBmr0Hod2W6l8bT5lYHpsyIgjYpsLU24rAG+1M5xlqMXPWKE5OovI5TplhCt6D1pPS1+2jJ18kuuWP/nFPuH4wT+ysZHB1ddtyq2FH0eY8Zl94SEZh78KF1vj+pkVFWeVUOUsY2HrJdlKwMANrAjYyf2rmRiGXLKpMXlynGWUmmEbWzsu8XFcumM=~-1~-1~-1; nsit=pyaT5Jih8TrhEWiq5QeyimKK; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcyOTkyNDk5NCwiZXhwIjoxNzI5OTMyMTk0fQ.VdeyZuJf6E7i-UAyP0Jj_XgRslY3qDc52IvSAHAxlC4; AKA_A2=A; bm_mi=33493C753474A516DA7CC040D3A6E6AA~YAAQxFM2FzdRTcOSAQAAn5mQxxlHuemZs8h5/gTqR23MSSVkN6VgVnze10+I61SVuQewqbuokZXWovT+mk0ns+GyJdk6mfW24V5ph0B/FNGxBrptLC+8ILWUQukNhZ4kmIvT0vGAyaDq8aK5uum9p/ZT/gdd5PaULO13/n6dODhvxy1VwHM7qSiiet/FjHokd733ih5V7ri+xsQ1lzM6wjbtMYtPGHa7SeyVrqy4WhGNCf8piWpIjBa66ReDt5TUPFtnN7eUHB7k6/hiUWFNHKzcEsW9V04CMgQfXvp0eP3DHahKxnlknfDZFO/K/RCgt0vBbJYCHQE=~1; bm_sz=9F2FD19CB89D265EB350CC53DCD7BFFB~YAAQxFM2FzlRTcOSAQAAn5mQxxlhU2rwwUBKmNKxBvcnPNQbots3WzS4hZ2KxhODWoXA21LFEjy7rLp5IhXSlxKxJrZl8x7PlYDJbyY+/P4n8+UDIerO4oVw6GX7kCVakf9/UEj2SM2tCVusYBQqD54pjvgFj1hwr5VYgpi3pTap2Q4zOpd1oRrSr6Jry3jlrwFNtuzrTEdzXFfbKx86b6CCHFupjzJ5Kk0ksYXbXZb/fTsezhXca89y5Td6Sy7QvuhBvb7/z7WAuEXS7uXVeXwTFqQL7XWRDm0kZyyS3x2z6eOcfui6tYQjVZ93erdph9c30zj7d3kQOGGCU8/fIk9atUIJyRi5SS16WCSUkrwGxeu8tM9tk15zm1A8EiSWxUW68GzLRNskwKogXuEHdWUJBbaRhRkH1XkP/CytYfldVOxnD10Lo2xnbua2vUCORTumlb+EKqoniw==~4342323~4604230; ak_bmsc=AF698C51141A21759CE3631C0F256E77~000000000000000000000000000000~YAAQxFM2F5JRTcOSAQAAqJ6QxxlOAksWGfW6vOcHr7FCHzg/WC2qlsOB5pW4IngSYBzijuPtpEECerGzR9u4GL4s5N5wruGIQE+Gz1RIMwKrsApMTKlsd9181E4DzdzfzvcrUDGnoh01QR9uS/JS10AzQ6FWj3zhKwd7X8iYuZZfIFYqWDHemHYpgGu/ZKy9jRntVtonnXy+Ng79NmNzUW2t7AhU9GUyZ8gNitQTvBqyfKedGSxAPJseuNozxBaSuGKHGNMuNMKXy9mPJLASHl9JQBZxCwkvaYhh7rJL5oir37kaoruaThj9trZfag6oyp4i0bvnmk7FdmVru/9Eo/Eq+diSOveqalbsuWLSEC4xLGIzPdVG52f69BicqBI0Zc1/axa9Mo594/+M7dkvNQcdP7WAtf9/0IdzQWMyKie7WvsEKodfNXZtQhjTojRfNNmJBeW78IxqGN4Mge6QoEQJytXPyeEhU7vg/gprDRhiXTqzFPGqSY6oJA==; _ga_87M7PJ3R97=GS1.1.1729924995.31.1.1729925311.40.0.0; _ga_WM2NSQKJEK=GS1.1.1729924995.5.1.1729925311.0.0.0; bm_sv=30A14D36DCC5263BB94289B4EF78C63E~YAAQxFM2F49mTcOSAQAAh2+Vxxl7xXqzjlbPvJHDTVWKfabDQNhBrpUkFQxNRy2SEMsepGFlzhyuIROqOYFDUZkG96/Uj0GzY5hUYmsbSmHWYWP5ZEsBXMbtkCvjfR5l7eGD7XKupsfATDytQl3Pqd2vrUnV6snFynT+lZdb3lNq5XQHeWJszXHMZj3S+zCRSGmJH1OtEb4fl/DZOpjcnpvlptwn1tNl6rS0lhsZz7Y2uUgdRkaiZYqcAnrUBsY7eaF2Rg==~1; RT=^\^z=1^",
    "^pragma": "no-cache^",
    "^priority": "u=1, i^",
    "^referer": "https://www.nseindia.com/all-reports^",
    "^sec-ch-ua": "^\^Chromium^^;v=^\^130^^, ^\^Google",
    "^sec-ch-ua-mobile": "?0^",
    "^sec-ch-ua-platform": "^\^Windows^^^",
    "^sec-fetch-dest": "empty^",
    "^sec-fetch-mode": "cors^",
    "^sec-fetch-site": "same-origin^",
    "^user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36^",
    "^x-requested-with": "XMLHttpRequest^"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
print(type(response))
#print(response.content)