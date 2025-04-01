import re 

def validate_date(date_str):
    dateRegex = re.compile(r'(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([12]\d{3})')
    
    mo = dateRegex.search(date_str)

    if not mo:
        print("Invalid date format")
        exit()

    day = int(mo.group(1))
    month = int(mo.group(2))
    year = int(mo.group(3))

    is_leap = (year % 100 == 0 and year % 4 == 0) or (year % 400 == 0)
    if month == 2:
        if(day>29) or (day == 29 and not is_leap):
            return f"Invalid date : {date_str} (February is a special month)"
        else:
            return f"Valid date"
    elif month in [4,6,9,11]:
        if day > 30:
            return f"Invalid date, {month} has only 30 days" 
        else: 
            return "It's a 30-day month"
    elif month in [1,3,5,7,8,10,12]:
        print("It's a 31-day month")

test_dates = [
    "31/02/2025",
    "29/02/2024",
    "30/04/2025",
]

for date in test_dates:
    print(validate_date(date))