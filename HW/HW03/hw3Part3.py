'''
The purpose of this code is to track the position and power level of a Pikachu as a user enters ten commands that directs the Pikachu to take certain actions. At the end of the code, printed is the final position and power level of the Pikachu, a list of all the commands entered, and a sorted list of all the commands entered.
CSCI1100 Spring 2018
Author: Samuel Marks
'''
def move(x,y,direction):
    '''
    The function takes the current x position, x, the current y position, y, and the direction the user directs the Pikachu to move, direction, and returns the next location of the Pikachu as an (x,y) tuple. The if statements assure that the coordinates are not less than 0 or greater than 150.
    '''
    if direction.lower() == "n":
        y = y - 20
        if y < 0:
            y = 0
        return (x,y)
    elif direction.lower() == "e":
        x = x + 20
        if x > 150:
            x = 150
        return (x,y)
    elif direction.lower() == "s":
        y = y + 20
        if y > 150:
            y = 150
        return (x,y)
    elif direction.lower() == "w":
        x = x - 20
        if x < 0:
            x = 0
        return (x,y)

##initial values for the coordinates and power
coordinates = (75, 75)
power = 10
##all_commands is the list where the actions inputed by the user will be appended
all_commands = []

##while loop will run until the user enters 10 commands, if statements ensure power levels are no negative and the appropriate output is printed when power level is 0
while len(all_commands) < 10:
    print("Pikachu at {} with power {}".format(coordinates, power))
    action = input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
    print(action)
    if action.lower() == "n" or action.lower() == "s" or action.lower() == "e" or action.lower() == "w":
        power = power - 1
        if power >= 0:
            (x,y) = coordinates
            coordinates = move(x,y,action)
        elif power < 0:
            power = 0
            print("Pikachu is too tired!")
        all_commands.append(action)
    elif action.lower() == "attack":
        power = power - 5
        if power >= 0:
            print("Bzzzt, Pikachu zaps its foe!")
        elif power < 0:
            power = 0
            print("Pffft, It's a dud ...")
        all_commands.append(action)
    elif action.lower() == "rest":
        power = 10
        all_commands.append(action)
    elif not action.lower() == "n" or action.lower() == "s" or action.lower() == "e" or action.lower() == "s" or action.lower() == "attack" or action.lower() == "rest":
        power = power - 1
        if power < 0:
            power = 0
            print("Pikachu is too tired!")
        all_commands.append(action)

##print statements print final position and power level, the list of all commands, and the sorted list of all the commands        
print("Pikachu at {} with power {}".format(coordinates, power))  
print()
print("All commands entered:")
print(all_commands)
print("All commands sorted:")
print(sorted(all_commands))