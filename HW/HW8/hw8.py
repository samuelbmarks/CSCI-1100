'''
HW8 Main Code
The purpose of this code is to implement two classes, Person and Universe, to run a simulation where individuals with different characterists and locations move along multiple universes with varying rewards and portals. The characteristics of the universes and individuals are given in an input file.
Author: Samuel Marks
CSCI Spring 2018
'''
#import statement
from Person import *
from Universe import *
import json
import math

if __name__ == "__main__":    
    #allows user to input file
    fname = input("Input file => ")
    print(fname)
    
    #reads all the information in file
    data = json.loads(open(fname).read())    
    
    #people will be used to store information on each person in file
    people = []
    #universe dictionary will be used to store information on each universe
    universe = dict()
    print('All universes')
    print("----------------------------------------")
    #for loop to set universe keys to the universe name and the values to information on rewards, portals, and individuals in that universe
    #for loop also prints information about universe using Universe class
    for i in range(len(data)):
        uname = data[i]['universe_name']
        rewards = data[i]['rewards']
        portals = data[i]['portals']
        individuals = data[i]['individuals']
        universe[uname] = rewards,portals,individuals
        print(Universe(uname,rewards,portals))
        print()

        #for loop goes through each individual in the currently specified universe and assigns each piece of information about the individual to a variable which is then put into the Person class, then each class object is appended to the people list
        for o in range(len(data[i]['individuals'])):
            name = data[i]['individuals'][o][0]
            radius = data[i]['individuals'][o][1]
            current = uname
            x = data[i]['individuals'][o][2]
            y = data[i]['individuals'][o][3]
            dx = data[i]['individuals'][o][4]
            dy = data[i]['individuals'][o][5]
            people.append(Person(name,radius,uname,x,y,dx,dy))
    
    print('All individuals')
    print("----------------------------------------")     
    #printing information about each individual by printing each class object in people list
    for person in people:
        print(person)   
            
    print()        
    print('Start simulation')
    print("----------------------------------------")
    
    #creating variables that will track different counts as simulation runs
    step_count = 0
    stop_count = 0 
    crashed_at = 0
    crashed_with = ''
    
    #while loop that will run until the number of steps reaches 100 or until all individuals stop moving
    while step_count < 100 and stop_count < len(people):
        #for loop that will go through each person in the list of Person class objects (people list)
        for person in people:
            count = 0
            #if statement checks if person is out of bounds
            if person.x <= 0 or person.x >= 1000 or person.y <= 0 or person.x >= 1000:
                #if statement checks if perosn is not moving
                if person.dx != 0 or person.dy != 0:
                    #if both if statements are true, a statement stating that the individual has stopped at a specified location, and their final speed is recorded and their current speed is set to 0
                    print('{} stopped at simulation step {} at location ({:.1f},{:.1f})'.format(person.name, step_count, person.x, person.y))
                    print()                  
                    person.final_dx = person.dx
                    person.final_dy = person.dy
                    person.dx = 0
                    person.dy = 0
                    stop_count += 1
            
            #for loop goes through each list of reward information in the universe dictionary and if individual gets close enough to the reward, they pick up the reward and a statement stating the reward name as well as the step that the individual picked the reward up at is printed
            for reward in universe[person.current][0]:
                if math.sqrt((person.x-reward[0])**2+(person.y-reward[1])**2) <= person.radius and person.dx != 0 and person.dy != 0:
                    person.reward(reward[0],reward[1],reward[2],reward[3],person.current)
                    universe[person.current][0].pop(count)
                    print('{} picked up "{}" at simulation step {}'.format(person.name,reward[3],step_count))
                    print(person)
                    print()
                count += 1
                
            #if statement checks if the absolute value of persons speed is less than 10 
            if abs(person.dx) < 10 or abs(person.dy) < 10:
                #if statement checks if perosn is not moving
                if person.dx != 0 or person.dy != 0:
                    #if both if statements are true, a statement stating that the individual has stopped at a specified location, and their final speed is recorded and their current speed is set to 0
                    print('{} stopped at simulation step {} at location ({:.1f},{:.1f})'.format(person.name, step_count, person.x, person.y))
                    print()                  
                    person.final_dx = person.dx
                    person.final_dy = person.dy
                    person.dx = 0
                    person.dy = 0
                    stop_count += 1          
            
            #for loop that goes though each person in people list
            for person1 in people:
                #if number of steps is 0, loop is broken
                if step_count == 0:
                    break
                if crashed_at == step_count and crashed_with == person:
                    continue                 
                #if statement checks if the current person in the list of people is not the currently specified person in the people list of the outermost for loop
                if person1 != person:
                    #if statement checks if the two inidividuals are going to collide
                    if math.sqrt((person.x-person1.x)**2+(person.y-person1.y)**2) <= person.radius+person1.radius and person.current == person1.current and person.dx != 0 and person.dy != 0 and person1.dx != 0 and person1.dy != 0:
                        #if both if statements are true, a statement stating that the two individuals crashed the current step in the current universe is printed
                        crashed_at = step_count
                        crashed_with = person1
                        print('{} and {} crashed at simulation step {} in universe {}'.format(person.name, person1.name, step_count, person.current))
                        #if statement that has the individual drop a reward if they have more than zero rewards after collision and prints what reward was returned
                        if len(person.rewards) > 0:
                            drop = person.collision()
                            universe[drop[1]][0].append((drop[2],drop[3],drop[4],drop[0]))
                            print('{} dropped "{}", reward returned to {} at ({},{})'.format(person.name,drop[0],drop[1],drop[2],drop[3]))
                        #if statement that has the individual drop a reward if they have more than zero rewards after collision and prints what reward was returned
                        if len(person1.rewards) > 0:
                            drop = person1.collision()
                            universe[drop[1]][0].append((drop[2],drop[3],drop[4],drop[0]))
                            print('{} dropped "{}", reward returned to {} at ({},{})'.format(person1.name,drop[0],drop[1],drop[2],drop[3]))
                        #updated information about both people is printed
                        print(person)
                        print(person1)
                        print()
                    
            #if statement checks if the absolute value of persons speed is less than 10 
            if abs(person.dx) < 10 or abs(person.dy) < 10:
                #if statement checks if perosn is not moving
                if person.dx != 0 or person.dy != 0:
                    #if both if statements are true, a statement stating that the individual has stopped at a specified location, and their final speed is recorded and their current speed is set to 0
                    print('{} stopped at simulation step {} at location ({:.1f},{:.1f})'.format(person.name, step_count, person.x, person.y))
                    print()                  
                    person.dx = 0
                    person.dy = 0
                    stop_count += 1            
                    
            #for loop goes through each list of portal information in the universe dictionary
            for portal in universe[person.current][1]:
                #if the number of steps is 0, the loop is broken
                if step_count == 0:
                    break
                else:
                    #if individual gets close enough to a portal and is still moving, the Person class method portal() is applied and the appropriate print statement is printed
                    if math.sqrt(((person.x-portal[0])**2)+((person.y-portal[1])**2)) <= person.radius and person.dx != 0 and person.dy != 0:
                        person.portal(portal)
                        print('{} passed through a portal at simulation step {}'.format(person.name, step_count))
                        #updated information about the individual is printed
                        print(person)
                        print()
        
        #if statement that breaks outer for loop if all individuals are stopped
        if stop_count == len(people):
            break
        
        #for loop that goes through each person in people list and uses Person class method move() to move each individual
        for person in people:
            person.move()        
        #step_count tracks number of steps
        step_count += 1      
    
    #creating list remaining tracks the amount of people left moving
    remaining = []
    #for loop goes through each person in people list
    for person in people:
        #if statement checks if perosn is not moving
        if person.dx != 0 and person.dy != 0:
            #if statement checks if person is not in bounds
            if person.x > 1000 or person.x < 0 or person.y > 1000 or person.y < 0:
                #if both if statements are true, a statement stating that the individual has stopped at a specified location
                print('{} stopped at simulation step {} at location ({:.1f},{:.1f})'.format(person.name, step_count, person.x, person.y))
                print()
            else:
                remaining.append(person.name)
    
    print()
    print("----------------------------------------")
    print('Simulation stopped at step',step_count)
    
    #if individuals are remaining after 100 steps, they are printed here
    if len(remaining) > 0:
        print(len(people) - stop_count,'individuals still moving:')
        for i in remaining:
            print(i)
        print()
    #if not, this is indicated in this print statement
    else:
        print('0 individuals still moving')
    
    #high represents highest score
    high = 0
    #winners list is created so that the inidividual(s) with the highest score can be appended to it
    winners = []
    
    #for loop goes through each person in people list and sets high to the highest score of all individuals
    for person in people:
        if person.points >= high:
            high = person.points
    
    #for loop goes through each person in people list and appends the individual(s) with the highest score to winners list
    for person in people:
        if person.points == high:
            winners.append(person)
    
    print('Winners:')
    #for loop that goes through each class object that was appended to winners and prints out their information as well as their rewards
    for person in winners:
        print(person.winner())
        print('Rewards:')
        for reward in person.rewards:
            print('    '+reward)
        print()