def get_century_anchor(year):
    """Get the anchor day for any century"""
    # Formula works for any century: (5 * (century mod 4) + 2) mod 7
    century = year // 100
    return ((5 * (century % 4) + 2) % 7)

def is_leap_year(year):
    """Check if year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def get_year_anchor(year):
    """Calculate the anchor day for any year"""
    century_anchor = get_century_anchor(year)
    y = abs(year % 100)  # Handle negative years correctly
    
    # Modified algorithm to handle any year
    anchor = (y + y//4 + century_anchor) % 7
    
    # Adjust for negative years
    if year < 0:
        # Negative years need special handling
        anchor = (7 - (abs(anchor) % 7)) % 7
    
    return anchor

def get_month_doomsday(month, year):
    """Get the doomsday for each month"""
    if is_leap_year(year):
        month_doomsdays = {1: 4, 2: 29, 3: 7, 4: 4, 5: 9, 6: 6,
                          7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
    else:
        month_doomsdays = {1: 3, 2: 28, 3: 7, 4: 4, 5: 9, 6: 6,
                          7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
    return month_doomsdays[month]

def validate_date(day, month, year):
    """Validate if the date is possible"""
    if month < 1 or month > 12:
        return False
    
    # Days in each month
    if is_leap_year(year):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if day < 1 or day > days_in_month[month-1]:
        return False
    
    return True

def get_day_of_week(day, month, year):
    """Calculate the day of the week for any given date"""
    # Validate date first
    if not validate_date(day, month, year):
        return "Invalid date"

    # Get the year's anchor day
    year_anchor = get_year_anchor(year)
    
    # Get the doomsday for the month
    month_doomsday = get_month_doomsday(month, year)
    
    # Calculate the difference between the target date and the month's doomsday
    diff = day - month_doomsday
    
    # Calculate the day of week (0=Sunday to 6=Saturday)
    day_of_week = (year_anchor + diff) % 7
    
    # Handle negative results
    if day_of_week < 0:
        day_of_week += 7
    
    # Convert to actual day names
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 
            'Thursday', 'Friday', 'Saturday']
    return days[day_of_week]

def main():
    print("Enhanced Doomsday Algorithm Calculator")
    print("(Works with dates from any year)")
    while True:
        print("\nEnter date (example: 9 7 1999 for July 9, 1999)")
        print("Use negative years for BCE/BC (example: 9 7 -1000 for July 9, 1000 BCE)")
        print("Type 'exit' to quit:")
        
        user_input = input()
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
            
        try:
            day, month, year = map(int, user_input.split())
            result = get_day_of_week(day, month, year)
            if result == "Invalid date":
                print("Invalid date entered. Please check your input.")
            else:
                era = "CE" if year >= 0 else "BCE"
                year_display = abs(year)
                print(f"Date: {day}/{month}/{year_display} {era}")
                print(f"The day is: {result}")
        except ValueError:
            print("Please enter date in format: day month year (space separated)")
            print("Example: 9 7 2025")

if __name__ == "__main__":
    main()
