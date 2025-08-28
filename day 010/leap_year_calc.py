def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap year"
            else:
                return "Normal year"
        else:
            return "Leap year"
    else:
        return "Normal year"
    
print(is_leap_year(int(input("I can tell you if a year is leap or not. Try me, type a year: "))))