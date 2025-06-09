from datetime import datetime, timedelta

def next_reminder_time(hour=18):
    now = datetime.now()
    reminder = now.replace(hour=hour, minute=0, second=0, microsecond=0)
    if reminder < now:
        reminder += timedelta(days=1)
    return reminder.isoformat()
