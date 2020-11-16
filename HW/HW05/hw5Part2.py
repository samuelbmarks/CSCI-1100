'''
HW 5 Part 2
The purpose of this program is to randomly simulate the movements and performance of a pokemon trainer that is initially placed on the center of a grid of an inputted size.
Author: Samuel Marks
CSCI1100 Spring 2018
Version 1
'''
##importing random, as the random module is needed to make this simulation
import random

def move_trainer():
    '''
    This function has no arguments and randomly chooses a direction, N, E, S, or W, and the probability that a pokemon will be seen at a specific turn between 0 and 1 (which is rounded to two decimal places). Returned are the randomly selected direction, direction, and the probability, seen.
    '''    
    possible_directions = ['N','E','S','W']
    direction = str(random.choice(possible_directions))
    seen = round(random.random(),2)
    return (direction, seen)
    
def throw_pokeball(num_false,num_true):
    '''
    This function takes the arguments num_true, the number of boolean False values that will appear in a list, and num_true, the number of boolean True values that will appear in a list, and randomly choices a boolean in that list. Returned is the randomly selected boolean, true_false.
    '''    
    booleans = "False "*num_false+"True "*num_true
    booleans = booleans.split()
    true_false = random.choice(booleans)
    return true_false
    
##input statements
size = int(input("Enter the integer grid size => "))
print(size)
probability = input("Enter a probability (0.0 - 1.0) => ")
print(probability)
probability = float(probability)

##setting the random seed value
seed = size*10+size
random.seed(seed)

##defining variables that will be used in the while loop
x_position = size//2
y_position = size//2
num_turns = 0

##initially, the number of falses start at 3 and the number of trues start at 1
falses = 3
trues = 1

##the variables total_seen and captured are set at zero and will be added to in the loop when certain conditions apply
total_seen = 0
captured = 0

##while loop used to change position of the trainer on the grid based on what direction is randomly returned, track the number of turns taken, decide whether or not a pokemon is seen, and decide whether the pokemon is caught or not
while x_position > 0 and y_position > 0 and x_position < size-1 and y_position < size-1:
    (direction,seen) = move_trainer()
    if direction == 'N':
        x_position -= 1
        num_turns += 1
    elif direction == 'S':
        x_position += 1
        num_turns += 1
    elif direction == 'W':
        y_position -= 1
        num_turns += 1
    elif direction == 'E':
        y_position += 1
        num_turns += 1
        
    if seen < probability:
        print("Saw a pokemon at turn {}, location ({}, {})".format(num_turns,x_position,y_position))
        true_false = throw_pokeball(falses,trues)
        if true_false == "False":
            print("Missed ...")
            total_seen += 1
        elif true_false == "True":
            print("Caught it!")
            trues += 1
            captured +=1
            total_seen += 1

##print statements including stats about the trainer's performance
print("Trainer left the field at turn {}, location ({}, {}).".format(num_turns,x_position,y_position))
print("{} pokemon were seen, {} of which were captured.".format(total_seen,captured))