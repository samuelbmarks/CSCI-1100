'''
Lab 5 Checkpoint 1
CSCI1100 Spring 2018
Author: Samuel Marks
'''
import lab05_util

def print_info(restaurant):
    print(restaurant[0]+" ("+restaurant[5]+")")
    street_city = restaurant[3].split("+")
    print("\t"+street_city[0])
    print("\t"+street_city[1])
    print("Average Score: {:.2f}".format(sum(restaurant[6])/len(restaurant[6])))
    
restaurants = lab05_util.read_yelp('yelp.txt')
print_info(restaurants[0])
print()
print_info(restaurants[4])