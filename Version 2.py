#Version 2!
import datetime
import calendar

event = input("Enter the name of the event: ")
year = int(input("Enter the year: "))
mon = int(input("Enter the month: "))
day = int(input("Enter the day: "))

month = calendar.month_name[mon]
event = event.upper()
date = datetime.datetime(year, mon, day)
event_date = date.strftime("%B %d, %Y")
week = date.strftime("%A")

print()
print("Formatted output:")
print("Event:", event)
print("Date:", event_date)
print("Year:", year)
print("Month:", mon)
print("Day:", day)
print("Weekday:", week)
