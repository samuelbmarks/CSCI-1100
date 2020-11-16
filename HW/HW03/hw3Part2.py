'''
The purpose of this code is to first ask for the name of a file containing the contents of a cash register and read from that file the list of all coins you have. The contents of the register will be reported and then the user will be asked for the cost of the item they are purchasing. Assuming they are paying will $1.00, calculated is the change they should receive using the coins in the register, using the largest value coins first.
CSCI1100 Spring 2018
Author: Samuel Marks
'''
import hw3_util

##user inputs coin file and the cost of the item
file_name = input("Enter the coin file name => ")
coins = hw3_util.read_change(file_name)
print(file_name)
cost = int(input("Enter the item cost in cents (0-100) => "))
print(cost)
print()
print("I have the following coins:")
print(coins)

##assigning variables to the count of each coin in the coin file
h = coins.count(50)
q = coins.count(25)
d = coins.count(10)
n = coins.count(5)
p = coins.count(1)

##creating variables for how many of each coin is being used to cover the change
counth = 0
countq = 0
countd= 0
countn = 0
countp = 0
finished = 0

##change is calculated and printed
change = 100 - cost
print("Change from $1.00 is {} cents".format(change))

##the following if statements determine the change that the user should receive using the coins in the register, using the largest value coins first (also determined is if the register contains coins that are able to supply the correct change)
if change > sum(coins):
    additional_cents = change - sum(coins)
    print("I cannot make change with my current coins.")
    print("I need an additional {} cents.".format(additional_cents))
    finished += 1
        
if (change//50 >= 1) and h > 0:
    if h >= (change//50): 
        counth = counth + change//50
        change = change - ((change//50)*50)
    else:
        counth = counth + h
        change = change- h*50
    
if (change//25 >= 1) and q > 0:
    if q >= (change//25): 
        countq = countq + change//25
        change = change - ((change//25)*25)
    else:
        countq = countq + q
        change = change - q*25
    
if (change//10 >= 1) and d > 0:
    if d >= (change//10): 
        countd = countd + change//10
        change = change - ((change//10)*10)
    else:
        countd = countd + d
        change = change - d*10

if (change//5 >= 1) and n > 0:
    if n >= (change//5): 
        countn = countn + change//5
        change = change - ((change//5)*5)
    else:
        countn = countn + n
        change = change - n*5       
    
if (change//1 >= 1) and p > 0:
    if p >= (change//1): 
        countp += change//1
        change = change - ((change//1)*1)
    else:
        countp = countp + p
        change = change - p*1       
   
##if statement containing print statements for if the register does not contain coins that are able to supply the correct change    
if change!=0 and finished == 0:
    print("I cannot make change with my current coins.")
    print("I need an additional {} cents.".format(change))
    
##prints the counts of each coins that satisfy the amount of change that needs to be returned the user
if change == 0:
    print("{} Half Dollars, {} Quarters, {} Dimes, {} Nickels, {} Pennies".format(counth, countq, countd, countn,countp))
    
    
        
    
    
    
    
    