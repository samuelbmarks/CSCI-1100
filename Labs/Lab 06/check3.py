"""
Lab 6 Checkpoint 3
Author: Samuel Marks
CSCI1100 Spring 2018
"""
import lab06_util

def ok_to_add(grid,row,column,number):
    if row < 1 or row > 9 or column < 1 or column > 9 :
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

def verify_board(grid):
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if grid[a][b] == ".":
                return False
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            number = grid[a][b]
            if ok_to_add(grid,a,b,number) == True:
                return False
    return True

file = input("Please enter a file name => ")
bd = lab06_util.read_sudoku(file)
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

while verify_board(bd) == False:
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
