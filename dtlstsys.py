def date_dt2(start, end='15-8-2025'):

    end=datetime.today().strftime("%d-%m-%Y") if end == '15-8-2025' else end
    start=datetime.strptime(start, "%d-%m-%Y").date()
    end=datetime.strptime(end, "%d-%m-%Y").date()


    # Generate all days

    all_days = [end - timedelta(days=i) for i in range((end - start).days + 1)]

    # Business days only (skip weekends)
    business_days = [d.strftime("%d-%b-%Y") for d in all_days if d.weekday() < 5]  # 0=Mon, ..., 6=Sun

    with open('dates_datetimeFnRev.txt', "w") as f:
        for item in business_days:
            f.write(item+"\n")
    return business_days,print(business_days)

if __name__ == "__main__":
    from datetime import timedelta,datetime
    import sys
    date_dt2(sys.argv[1] if len(sys.argv) > 1 else '30-9-2019', sys.argv[2] if len(sys.argv) > 2 else '15-8-2025')