'''
Lab 5 Checkpoint 2
CSCI1100 Spring 2018
Author: Samuel Marks
'''
import lab05_util

def print_info(restaurant):
    print(restaurant[0]+" ("+restaurant[5]+")")
    street_city = restaurant[3].split("+")
    print("\t"+street_city[0])
    print("\t"+street_city[1])
    
    if len(restaurant[6]) <= 2:
        average_score = sum(restaurant[6])/len(restaurant[6])
    else:
        sum_avg = sum(restaurant[6]) - (max(restaurant[6]) + min(restaurant[6]))
        len_avg = len(restaurant[6])-2
        average_score = sum_avg/len_avg
        
    if average_score >= 0 and average_score < 2:
        print("This restaurant is rated bad, based on {} reviews.".format(len(restaurant[6])))
    elif average_score >= 2 and average_score < 3:
        print("This restaurant is rated average, based on {} reviews.".format(len(restaurant[6]))) 
    elif average_score >= 3 and average_score < 4:
        print("This restaurant is rated above average, based on {} reviews.".format(len(restaurant[6])))
    elif average_score >= 4 and average_score < 5:
        print("This restaurant is rated very good, based on {} reviews.".format(len(restaurant[6])))        
    
restaurants = lab05_util.read_yelp('yelp.txt')

restaurant_id = int(input("Enter Restaurant ID: "))

if restaurant_id <= 0 or restaurant_id > len(restaurants):
    print("Warning, ID entered is not a valid ID.")
elif restaurant_id > 0 and restaurant_id <= len(restaurants):
    print_info(restaurants[restaurant_id-1])
    