'''
HW 5 Part 1
The purpose of this program is to set up the framework for Part 2 and Part 3, which will simulate a wandering Pokemon trainer searching for pokemon. 
Author: Samuel Marks
CSCI1100 Spring 2018
Version 1
'''
##importing random, as the random module is needed to make this simulation
import random

def move_trainer():
    '''
    This function has no arguments and randomly chooses a direction, N, E, S, or W, and a value between 0 and 1 (which is rounded to two decimal places). Returned are the randomly selected direction, direction, and value, value.
    '''
    possible_directions = ['N', 'E', 'S', 'W']
    direction = str(random.choice(possible_directions))
    value = round(random.random(),2)
    return direction, value
    
def throw_pokeball(num_false,num_true):
    '''
    This function takes the arguments num_true, the number of boolean False values that will appear in a list, and num_true, the number of boolean True values that will appear in a list, and randomly choices a boolean in that list. Returned are the list of booleans, booleans, and the randomly selected boolean, true_false.
    '''
    booleans = []
    for i in range(num_false):
        booleans.append(False)
    for i in range(num_true):
        booleans.append(True)
    true_false = random.choice(booleans)
    return booleans, true_false
    
##input statements
size = int(input("Enter the integer grid size => "))
print(size)
falses = int(input("Enter the integer number of Falses => "))
print(falses)
trues = int(input("Enter the integer number of Trues => "))
print(trues)

##setting the random seed value
seed = size*11
random.seed(seed)
print("Setting seed to {}".format(seed))

##for loop selects a random direction and value 5 times using the move_tranier() function
for i in range(5):
    print("Directions: ['N', 'E', 'S', 'W']")
    direction,value = move_trainer()
    print("Selected {}, value {:.2f}".format(direction,value))
    
##for loop prints the list of booleans as well as the randomly selected booleans 5 times using the throw_pokeball() function
for i in range(5):
    booleans, true_false = throw_pokeball(falses,trues)
    print("Booleans: {}".format(booleans))
    print("Selected {}".format(true_false))