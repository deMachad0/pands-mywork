# program that outputs whether or not today is  
# a weekday
# Author: Andre Machado





from datetime import datetime

# datetime.now() returns the current local date and time
today = datetime.now()

# weekday() returns the day of the week as an integer (number)
# monday is number 0 and sunday is 6
number = today.weekday()

print(today)

if number < 5:
    print("yes, unfortunately is a weekday.")
else:
    print("it is the weekend, yay!")