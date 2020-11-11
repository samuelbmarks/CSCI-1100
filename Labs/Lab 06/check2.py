"""
Lab 6 Checkpoint 2
Author: Samuel Marks
CSCI1100 Spring 2018
"""
def ok_to_add(grid,row,column,number):
    if row < 1 or row > 9 or column < 1 or column > 9 or number < 1 or number > 9 :
        return False
    
    if grid[row-1][column-1] != ".":
        return False
    
    if grid[row-1].count(number) != 0:
        return False
    
    for i in range(len(grid)):
        if grid[i][column] == number:
            return False
    
    row3,col3 = (row//3)*3,(column//3)*3
    for a in range(row3,col3+3):
        for b in range(col3,row3+3):
            if bd[a][b] == number:
                return False
    return True

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]

lines = "-------------------------"
print(lines)
for x in range(len(bd)):
    empty = ""
    for i in range(len(bd[x])):
        if i == 0:
            empty += "|"
        empty += " " + bd[x][i]
        if (i+1)%3 == 0:
            empty += " |"  
    print(empty)
    if (x+1)%3 == 0:
        print(lines)

row = int(input("Enter a row: "))
print(row)
column = int(input("Enter a column: "))
print(column)
number = int(input("Enter a number: "))
print(number)

if ok_to_add(bd,row,column,number) == False:
    print("This number cannot be added")
elif ok_to_add(bd,row,column,number) == True:
    bd[row-1][column-1] = number
    print(lines)
    for x in range(len(bd)):
        empty = ""
        for i in range(len(bd[x])):
            if i == 0:
                empty += "|"
            empty += " " + str(bd[x][i])
            if (i+1)%3 == 0:
                empty += " |"  
        print(empty)
        if (x+1)%3 == 0:
            print(lines)    