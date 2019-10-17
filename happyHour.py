# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:08:27 2019

@author: Nafis
"""

firstName = str(input("Enter First Name "))
dayOfTheWeek = str(input("What is the day of the week "))
timeInHours = int(input("Time in hours "))
timeInMinutes = int(input("What minute? "))
amOrPm = str(input("AM or PM ?: "))

""" 
Happy hours
monday - 6pm to 8pm
thursday - 5pm to 9pm
saturday - all day
"""

if dayOfTheWeek == "monday" and (timeInHours >= 6 and timeInHours <8) and amOrPm == "PM" :
    print("It is Happy Hour !!! ")
    
elif dayOfTheWeek == "thursday" and (timeInHours >= 5 and timeInHours <9) and amOrPm == "PM":
    print("It is Happy Hour !!! ")
    
elif dayOfTheWeek == "saturday":
    print("It is Happy Hour !!! ")
    
else:
    print("It is NOT Happy Hour")
    