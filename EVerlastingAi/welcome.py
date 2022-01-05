from time_module import get_hours
from output_module import output
from module_database import update_last_seen, get_last_seen
from datetime import date

def greet():
    

    #---------Fetch Previous Date---------#
    previous_date = get_last_seen()

    #------Fetch Today's Date and Store it to Database------#
    today_date = str(date.today())
    update_last_seen(today_date)

    hour = int(get_hours())
    if hour >= 4 and hour < 12:
        output("Good Morning Arata")
    elif hour >= 12 and hour < 16:
        output("Good Afternoon Arata")
    else:
        output("Good Evening Arata")

    if previous_date == today_date and hour >= 4 and hour < 12:
        output("Welcome back dear")
    