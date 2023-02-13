from datetime import date, datetime, timedelta

today = datetime.now()

name_day = today.strftime('%A')
if name_day == 'Sunday':
    date_end = today - timedelta(days=2)
elif name_day == 'Saturday':
    date_end = today - timedelta(days=1)
else:
    date_end = today

date_start = date_end - timedelta(days=4)
