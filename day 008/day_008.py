from datetime import datetime as dt
import datetime

def greet_with_name(name):
    print(f"Hello {name}")

greet_with_name("Bob")


ninety_years_in_days = 90 * 365
ninety_years = datetime.timedelta(ninety_years_in_days)
secs_to_weeks = 1 / 60 / 60 / 24 / 7

def calculate_life_left_in_weeks(name, date_of_birth):
    date_now = dt.now()
    date_at_birth = dt.strptime(date_of_birth, "%Y, %m, %d")
    date_at_ninety_years_old = date_at_birth + ninety_years
    weeks_left = int((date_at_ninety_years_old - date_now).total_seconds() * secs_to_weeks)
    print(f"{name}, you have {weeks_left} weeks left till you are 90")

calculate_life_left_in_weeks("Bob", "1969, 01, 01")