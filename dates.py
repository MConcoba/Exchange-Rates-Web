from datetime import datetime, timedelta

today = datetime.now()

name_day = today.strftime('%A')

if name_day == 'Thursday':
    date_end = today - timedelta(days=6)
elif name_day == 'Wednesday':
    date_end = today - timedelta(days=5)
elif name_day == 'Tuesday':
    date_end = today - timedelta(days=4)
elif name_day == 'Monday':
    date_end = today - timedelta(days=3)
elif name_day == 'Sunday':
    date_end = today - timedelta(days=2)
elif name_day == 'Saturday':
    date_end = today - timedelta(days=1)
else:
    date_end = today

date_start = date_end - timedelta(days=4)
# last_day = today - timedelta(days=1)
