'''
Lecture Exercises 11: Problem 2
CSCI1100 Spring 2018
Author: Samuel Marks
'''
hd = int(input("Enter Dale's height: "))
print(hd)
he = int(input("Enter Erin's height: "))
print(he)
hs = int(input("Enter Sam's height: "))
print(hs)

if hd > he and hd > hs and he > hs:
    print("Dale")
    print("Erin")
    print("Sam")  
elif hd > he and hd > hs and hs > he:
    print("Dale")
    print("Sam")
    print("Erin")
elif hs > hd and hs > he and he > hd:
    print("Sam")
    print("Erin")
    print("Dale")
elif hs > hd and hs > he and hd > he:
    print("Sam")
    print("Dale")
    print("Erin")  
elif he > hd and he > hs and hs > hd:
    print("Erin")
    print("Sam")
    print("Dale")  
elif he > hd and he > hs and hd > hs:
    print("Erin")
    print("Dale")
    print("Sam")