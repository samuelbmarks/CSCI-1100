'''
Homework 6 Part 2
The purpose of this program is to read the name of a title from the user. The user will enter any part of the title (in any case, upper or lower). It will find the first title in the list that contains the input string. If no match is found, the message will be printed. If a match is found, the following will happen: All the beasts that were featured in this title will be printed in lexicographical order, all the other titles that have at least one beast in common with this title will be printed in lexicographical order, and all the beasts that were featured only in this title (i.e. no other title has these beasts) will be printed, again in lexicographical order. Once the input is done being processed, the program will ask the user for another input until the user inputs "stop".
Author: Samuel Marks
CSCI 1100 Spring 2018
Version 1
'''
##import statement: need textwrap module to format print statements
import textwrap

##splitting titles.txt into a list [[movie,beasts],[movie,beast],...]
movies = []
for line in open("titles.txt"):
    line = line.strip()
    line = line.split("|",1)
    movies.append(line)
       
##setting input title not equal to "stop" to begin while loop
input_title = "begin"
##while loop to run until user inputs "stop"
while input_title != "stop":
    input_title = input("Enter a title (stop to end) => ")
    if input_title == "stop":
        print('stop')
        break
    print(input_title)
    print()
    input_title = input_title.title()
    
    ##for loop to find movie that the inputted title is apart of as well as created a list/set/string of beasts that appear in that movie
    for i in range(len(movies)):
        if input_title in movies[i][0]:
            match = movies[i][0]
            beasts_list = movies[i][1].split("|")
            beasts_list.sort()
            beasts_set = set(beasts_list)
            beasts = ", ".join(beasts_list)
    
            ##printing the found title
            print("Found the following title: {}".format(match))
            
            ##formatting beasts in the found title using textwrap module
            beasts_print_list = textwrap.wrap("Beasts in this title: {}".format(beasts))
            for i in range(len(beasts_print_list)):
                print(beasts_print_list[i])
                
            ##finding movies that have beasts that also appear in the found title
            movies_same = []
            for i in range(len(movies)):
                creatures = set()
                animals = movies[i][1].split("|")
                for j in range(len(animals)):
                    creatures.add(animals[j])
                if len(creatures & beasts_set) > 0 and match not in movies[i][0]: 
                    movies_same.append(movies[i][0])
                    movies_same.sort()
            
            ##finding beasts that appear only in the found title
            empty = set()
            for i in range(len(movies)):
                animals2 = movies[i][1].split("|")
                if match not in movies[i][0]:
                    for j in range(len(animals2)):
                        empty.add(animals2[j])
            beasts_different = beasts_set - empty
            beasts_different = list(beasts_different)
            beasts_different = sorted(beasts_different)
            
            ##making the list of the movies that have beasts that are the same into a string
            movies_same = ", ".join(movies_same)
            print()
            
            ##formatting movies that have beasts that are the same using textwrap module
            movies_same_print_list = textwrap.wrap("Other titles containing beasts in common: {}".format(movies_same))
            for i in range(len(movies_same_print_list)):
                print(movies_same_print_list[i])
            
            ##making the list of beasts that are unique to the found movie into a string
            beasts_different = ", ".join(beasts_different)
            print()
                
            ##formatting beasts that are unique to the found movie using the textwrap module
            beasts_different_print_list = textwrap.wrap("Beasts appearing only in this title: {}".format(beasts_different))
            for i in range(len(beasts_different_print_list)):
                print(beasts_different_print_list[i])
                
            print()
            break
    else:
        ##print statement if no title is found based on the user input
        print('This title is not found!')