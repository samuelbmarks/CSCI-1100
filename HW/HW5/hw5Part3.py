'''
HW 5 Part 3
The purpose of this program is to repeat the simulation a user-specified number of times, and output several summary statistics including the average number of turns in a simulation, the maximum number of turns, the minimum number of turns, the best net missed pokemon versus caught pokeon, and the worst net missed pokemon versus caught pokemon. 
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
    seen = random.random()
    return (direction, seen)
    
def throw_pokeball(num_false,num_true):
    '''
    This function takes the arguments num_true, the number of boolean False values that will appear in a list, and num_true, the number of boolean True values that will appear in a list, and randomly choices a boolean in that list. Returned is the randomly selected boolean, true_false.
    '''     
    booleans = "False "*num_false+"True "*num_true
    booleans = booleans.split()
    true_false = random.choice(booleans)
    return true_false

def run_one_simulation(grid,prob,size):
    '''
    This function takes the arguments grid, the list of lists that will keep track of the number of pokemon caught on each space in the grid versus the number seen but missed, prob, the probability a pokemon will be seen at each turn, and size, the size of the grid. The function will append the number of turns in one simulation to a list track the number of turns for all simulations. The function will return the number of turns required to reach the edge of the grid, num_turns.
    '''
    ##defining variables that will be used in the while loop
    x_position = size//2
    y_position = size//2
    num_turns = 0
    
    ##initially, the number of falses start at 3 and the number of trues start at 1
    falses = 3
    trues = 1
    total_seen = 0
    captured = 0    
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
        
        if seen < prob:
            true_false = throw_pokeball(falses,trues)
            if true_false == "False":
                total_seen += 1
                grid[x_position][y_position] -= 1
            elif true_false == "True":
                trues += 1
                grid[x_position][y_position] += 1
                captured +=1
                total_seen += 1

    turn_counter.append(num_turns)
    return num_turns

##input statements
size = int(input("Enter the integer grid size => "))
print(size)
probability = input("Enter a probability (0.0 - 1.0) => ")
print(probability)
probability = float(probability)
num_sim = int(input("Enter the number of simulations to run => "))
print(num_sim)
print()

##setting the random seed value
seed = size*11
random.seed(seed)

##setting up the grid
grid = [[] for x in range(size)]
for i in range(size):
    grid[i]=[0 for x in range(size)]

##creating an empty list turn_counter to keep record of the total amount of turns the trainer makes over the user imputted number of simulations
turn_counter = []

##for loop calls the function run_one_simulation once for each imputted number of siulations
for i in range(num_sim):
    run_one_simulation(grid, probability, size)
    
##printing the grib in proper format
for i in range(size):
    for x in range(size):
        print("{:5d}".format(grid[i][x]), end="")
    print()

##calculating statistics (avg,mins,max)
avg_turns = sum(turn_counter)/num_sim
max_turns = max(turn_counter)
max_index = turn_counter.index(max_turns)+1
min_turns = min(turn_counter)
min_index = turn_counter.index(min_turns)+1
max_list = []
for i in range(len(grid)):
    max_list.append(max(grid[i]))
best_net_missed = max(max_list)
min_list = []
for i in range(len(grid)):
    min_list.append(min(grid[i]))
worst_net_missed = min(min_list)

##print statements presenting the calculated statistics
print("Average number of turns in a simulation was {:.2f}".format(avg_turns))
print("Maximum number of turns was {} in simulation {}".format(max_turns,max_index))
print("Minimum number of turns was {} in simulation {}".format(min_turns,min_index))
print("Best net missed pokemon versus caught pokemon is {}".format(best_net_missed))
print("Worst net missed pokemon versus caught pokemon is {}".format(worst_net_missed))