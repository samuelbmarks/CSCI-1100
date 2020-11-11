"""
Lab 6 Checkpoint 2
Author: Sam Marks
CSCI1100 Spring 2018
"""
def ok_to_add(row, column, number):
    if row>8 or column>8:
        return False
    if bd[row][column]!='.':
        return False
    if bd[row].count(number)!= 0:
        return False
    for x in range(len(bd)):
        if bd[x][column]==number:
            return False
    nrow, ncol = (row//3)*3,(column//3)*3
    for a in range(nrow,ncol+3):
        for b in range(ncol, nrow+3):
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
    empty =""
    for i in range(len(bd[x])):
        if i==0:
            empty+="|"
        empty+=" "+bd[x][i] 
        if (i+1)%3==0:
            empty+=" |"  
    print(empty)
    if (x+1)%3==0:
        print(lines)

r = int(input("Enter a row: "))
c = int(input("Enter a column: "))
n = (input("Enter a number: "))

r=r-1
c=c-1

if ok_to_add(r,c,n)==False:
    print("This number cannot be added")
elif ok_to_add(r,c,n)==True:
    bd[r][c]=n
    print(lines)
    for x in range(len(bd)):
        empty =""
        for i in range(len(bd[x])):
            if i==0:
                empty+="|"
            empty+=" "+bd[x][i] 
            if (i+1)%3==0:
                empty+=" |"  
        print(empty)
        if (x+1)%3==0:
            print(lines)
    