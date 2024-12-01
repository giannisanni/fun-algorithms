# objective: find out on what day 9 juli 2025 is

# zero index dagen
# zondag = 0
# maandag = 1
# dinsday = 2
# woesdag = 3
# donderdag = 4
# vrijdag = 5
# zaterdag = 6


# deze data vallen altijd op de zelfde dag van de week
# jan 31 of (leap)32
# feb 28 of (leap)29
# mar 7
# apr 4
# mei 9
# jun 6
# jul 11
# aug 8
# sep 5
# okt 10
# nov 7
# dec 12 

# deze data vallen alijd op de zelfde dag van de week (per eeuw)
# 1500,1900,2300 = woensdag = 3
# 1600,2000,2400 = dinsdag = 2
# 1700,2100,2500 = zondag = 0
# 1800,2200,2600 = vrijdag = 5


# 2000 = 2
# 25/12 = 2 r 1
# 1/4 = 0
# 2+2+1+0= 5 == vrijdag == anker == 11 juli 2025

# 11-9 = 2 dagen = vrijdag-2 = woensdag






def get_century_anchor(year):
    """Get the anchor day for the century (0=Sunday to 6=Saturday)"""
    century = (year // 100) % 4 # modulo operation, gives remainder (r) when div by 4
    century_anchors = {0: 2,  # 2000,2400,etc = Tuesday, divisible by 400
                      1: 0,  # 2100,2500,etc = Sunday, next in line 
                      2: 5,  # 2200,2600,etc = Friday, after the those
                      3: 3}  # 2300,2700,etc = Wednesday, centuries before a year divisible by 400
    return century_anchors[century]

def is_leap_year(year):
    """Check if year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) 
# conditions: 
# 1. year must be div by 4, 
# 2. year is not div by 100 (century year =/= leap years, with an exception)
# 3. century years div by 400 are leap years


def get_year_anchor(year):
    """Calculate the anchor day for the specific year"""
    century_anchor = get_century_anchor(year)
    y = year % 100 #extracts last two digits of given year
    # Algorithm: y + y//4 + century_anchor (mod 7)
    return (y + y//4 + century_anchor) % 7

def get_month_doomsday(month, year):
    """Get the doomsday for each month"""
    # Each month has a doomsday that falls on the year's anchor day
    if is_leap_year(year):
        month_doomsdays = {1: 4, 2: 29, 3: 7, 4: 4, 5: 9, 6: 6,
                          7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
    else:
        month_doomsdays = {1: 3, 2: 28, 3: 7, 4: 4, 5: 9, 6: 6,
                          7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
    return month_doomsdays[month]

def get_day_of_week(day, month, year):
    """Calculate the day of the week for any given date"""
    # Get the year's anchor day
    year_anchor = get_year_anchor(year)
    # Get the doomsday for the month
    month_doomsday = get_month_doomsday(month, year)
    # Calculate the difference between the target date and the month's doomsday
    diff = day - month_doomsday
    # Calculate the day of week (0=Sunday to 6=Saturday)
    day_of_week = (year_anchor + diff) % 7
    # Convert to actual day names
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
            'Thursday', 'Friday', 'Saturday']
    return days[day_of_week]

def main():
    print("Doomsday Algorithm Calculator")
    print("Enter date (example: 9 7 1999 for July 9, 1999):")
    try:
        day, month, year = map(int, input().split())
        result = get_day_of_week(day, month, year)
        print(f"The day is: {result}")
    except ValueError:
        print("Please enter date in format: day month year (space separated)")
        print("Example: 9 7 2025")

if __name__ == "__main__":
    main()
