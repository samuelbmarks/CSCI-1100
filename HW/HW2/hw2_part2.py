'''
The goal of this program is to compute the year when a given day length in seconds (inputed by a user) would occur.
Author: Samuel Marks
CSCI1100 Spring 2018
Version 1
'''
import math
def time_to_seconds(hours,minutes,seconds):
    seconds = hours*60*60+minutes*60+seconds
    return seconds

def seconds_to_time(seconds):
    hour = seconds//(60*60)
    minutes = (seconds-(hour*(60*60)))//60
    sec = seconds-(hour*(60*60))-(minutes*60)
    return str(hour)+" hours "+str(minutes)+" minutes and "+str(sec)+" seconds"

def seconds_to_time2(seconds):
    hour = seconds//(60*60)
    minutes = (seconds-(hour*(60*60)))//60
    sec = seconds-(hour*(60*60))-(minutes*60)
    return str(hour)+" hours, "+str(minutes)+" minutes and "+str(sec)+" seconds"

def calculate_years(desired_length,current_length,rate_change):
    change_sec = desired_length-(current_length)
    if change_sec <0:
        years = int(abs((change_sec)/(rate_change)))
        years*=-1
    else:
        years = int(((change_sec)/(rate_change)))
        
    year = 2018+(years)
    
    return year

change_rate = (6*60*60)/900000000
print("The current length of a day is {} seconds.".format(time_to_seconds(23,56,4)))
desired_length = int(input("Enter the desired day length in seconds => "))
print(desired_length)
print()
print("{} seconds is a day length of {}.".format(desired_length, seconds_to_time(desired_length)))
print("A day change rate of 6 hours every 900000000 years, \nrepresents {:.6f} seconds per year.".format(change_rate))
print("A day length of {},".format(seconds_to_time2(desired_length)))
print("Would be in year {}".format((calculate_years(desired_length,time_to_seconds(23,56,4),change_rate))))