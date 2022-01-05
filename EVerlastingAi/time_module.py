from datetime import datetime
from datetime import date

def get_time():
   time_now = datetime.now()
   current_time = time_now.strftime("%H:%M:%S")
   return current_time

def get_date():
    date_now = datetime.today()
    current_date = date_now.strftime("%B %d, %Y")
    return current_date

def get_hours():
    time_now = datetime.now()
    current_time = time_now.strftime("%H")
    return current_time