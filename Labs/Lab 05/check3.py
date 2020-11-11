'''
Lab 5 Checkpoint 3
CSCI1100 Spring 2018
Author: Samuel Marks
'''
import lab05_util
import webbrowser

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

print("What would you like to do next?")
print("1. Visit the homepage")
print("2. Show of Google Maps")
print("3. Show directions to this restaurant")
choice = int(input("Your choice (1-3)? ==> "))

if choice == 1:
    webbrowser.open(restaurants[restaurant_id-1][4])
elif choice == 2:
    webbrowser.open("http://www.google.com/maps/place/{}".format(restaurants[restaurant_id-1][3]))
elif choice == 3:
    webbrowser.open("http://www.google.com/maps/dir/110 8th Street Troy NY/{}".format(restaurants[restaurant_id-1][3]))
