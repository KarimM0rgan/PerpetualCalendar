# Description: This project detects the leap year, number of day in the year, what day it is, and the date of thanksgiving.

# Function to determine if a year is a leap year
def is_leap(year):
    # A leap year is divisible by 4, but not every year divisible by 100 is a leap year, except if it is also divisible by 400.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400, so it's a leap year
            else:
                return False  # Divisible by 100 but not by 400, so not a leap year
        else:
            return True  # Divisible by 4 but not by 100, so it's a leap year
    else:
        return False  # Not divisible by 4, so not a leap year

# Function to calculate the number of days that passed before the start if the month
def magic_month(month):  
        # Number of days before each month in a non-leap year
        if month == 12:
                days = 334  # Days before December
        elif month == 11:
                days = 304  # Days before November
        elif month == 10:
                days = 273  # Days before October
        elif month == 9:
                days = 243  # Days before September
        elif month == 8:
                days = 212  # Days before August
        elif month == 7:
                days = 181  # Days before July
        elif month == 6:
                days = 151  # Days before June
        elif month == 5:
                days = 120  # Days before May
        elif month == 4:
                days = 90   # Days before April
        elif month == 3:
                days = 59   # Days before March
        elif month == 2:
                days = 31   # Days before February
        elif month == 1:
                days = 0    # Days before January
        else:
                days = "That's an invalid month"  # Error message for invalid month
        
        return days

# Function to calculate the day of the year for a given date
def day_of_year(month, day, year):
        leap_year = is_leap(year)  # Check if it's a leap year
        days_before_month = magic_month(month)  # Get days before the given month
        day_of_year = days_before_month + day  # Total days so far in the year

        # If it's a leap year and the date is after February, add 1 extra day
        if leap_year and month > 2:
                day_of_year += 1
    
        return day_of_year

# Function to calculate the day of the week for January 1st of a given year
def new_years_day(year):
        quotient1 = year // 4
        addition1 = year + quotient1
      
        quotient2 = year // 100
        subtraction = addition1 - quotient2
      
        quotient3 = year // 400
        addition2 = subtraction + quotient3

        leap_year = is_leap(year)  
        if leap_year:
            addition2 -= 1  # Adjust for leap year if necessary
        
        NewYears = addition2 % 7  # Day of the week for January 1st (0-Sunday, 1-Monday, ...)
        
        return NewYears

# Function to calculate the day of the week for any given date
def day_of_week(month, day, year):
       DayYear = day_of_year(month, day, year)  # Get the day of the year
       NewYearsDay = new_years_day(year)  # Get the day of the week for January 1st
       
       # Calculate the day of the week (0-Sunday, 1-Monday, ..., 6-Saturday)
       DayWeek = ((DayYear + NewYearsDay) - 1) % 7
       
       return DayWeek

# Function to convert the day of the week from a number to a string
def day_of_week_str(month, day, year):
        value = day_of_week(month, day, year)  # Get day of the week as a number
        # Assign each numeric value to its corresponding day of the week
        if value == 6:
              day_str = "Saturday"
        elif value == 5:
              day_str = "Friday"
        elif value == 4:
               day_str = "Thursday"
        elif value == 3:
               day_str = "Wednesday"
        elif value == 2:
               day_str = "Tuesday"
        elif value == 1:
               day_str = "Monday"
        elif value == 0:
               day_str = "Sunday"
        else:
               day_str = "This is not a valid day"  # invalid case

        return day_str

# Function to calculate when Thanksgiving falls in a given year
def find_thanksgiving(year):
        # Get the day of the week for November 1st
        november_first_day = day_of_week(11, 1, year)

        # If November 1st is a Thursday, Thanksgiving falls on the 22nd (3 weeks after)
        if november_first_day == 4:
                return 22 # 1 + 21
        
        # If November 1st is before Thursday, add days to reach the next Thursday
        elif november_first_day < 4: 
               return 22 + (4 - november_first_day)
        
        # If November 1st is after Thursday, calculate days to the next Thursday
        else:
                return 22 + (7 - (november_first_day + 4))

# Main function to run the perpetual calendar program
def main():
        keep_going = "y"
        while keep_going == "y":
                print()
                print("Pick any date! (Maybe your birthday)")

                # Get month, day, and year from the user
                month = int(input("Enter a month (1-12):"))
                day = int(input("Enter a day (1-31):"))
                year = int(input("Enter a year:"))

                # Calculate and display the day of the year
                DayYear = day_of_year(month, day, year)
                print("This is day number", DayYear, "of the year.")

                # Get the day of the week for the given date and display it
                day_str = day_of_week_str(month, day, year)
                print("This day falls on a", day_str)

                # Show what day this date falls on in 2020
                day_str2020 = day_of_week_str(month, day, 2020)
                print("In 2020, this date falls on a", day_str2020)

                # Show what day New Year's Day falls on in the given year
                NewYearsDay = day_of_week_str(1, 1, year)
                print("In ", year, ", New Year's day falls on a ", NewYearsDay, sep="")

                # Calculate and display the date of Thanksgiving
                ThanksGiving = find_thanksgiving(year)
                print("Thanksgiving falls on the", ThanksGiving, "of that year")

                # Ask if the user wants to continue
                keep_going = input("Do you want to keep going? (y or n)")
        
        print("Thanks for using the perpetual calendar!")

# Run the program
if __name__ == "__main__":
    main()           