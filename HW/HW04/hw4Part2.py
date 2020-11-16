'''
HW 4 Part 2
The purpose of the program is to allow users to lookup locations by ZIP code, lookup ZIP codes by city and state, and determine the distance between two locations designated by their ZIP codes. The program interacts with the user by printing a prompt and allowing them to enter commands until they enter 'end' at which point the program prints Done and finishes. If an invalid command is entered, the program prints Invalid command, ignoring and is ready to take the next command.
CSCI1100 Spring 2018
Author: Samuel Marks
'''
##import statements -> math module needed to make distance calculations
import hw4_util
import math

def zip_by_location(zip_codes, location):
    '''
    The purpose of this function is to return a list of zip codes, zip_list, for a inputted location, location, which is a tuple created from a given city and state. The other argument for this function is zip_codes, a list of ZIP codes data in the format, returned by read_zip_all().
    '''
    zip_codes = hw4_util.read_zip_all()
    (city, state) = location
    zip_list = []
    i = 0
    while i < len(zip_codes):
        if zip_codes[i][3] == city and zip_codes[i][4] == state:
            zip_list.append(zip_codes[i][0])
        i+=1
    return zip_list
            
def location_by_zip(zip_codes, code):
    '''
    The purpose of this fuction is to find location information corresponding to the
    specified ZIP code, code. The other argument for this function is zip_codes, a list of ZIP codes data in the format, returned by read_zip_all().
    '''
    zip_codes = hw4_util.read_zip_all()
    i = 0
    while i < len(zip_codes):
        if zip_codes[i][0] == code:
            return zip_codes[i][1], zip_codes[i][2], zip_codes[i][3], zip_codes[i][4], zip_codes[i][5]
        i+=1
            
def convert_lat(lat):
    '''
    The purpose of this function is to take a specified latitude in decimal format, lat, and calculate and return that latitude in DMS format (see return statements).
    '''
    if lat > 0:
        degrees = int(lat)
        minutes = int((lat - degrees) * 60)
        seconds = (lat - degrees - minutes / 60) * 3600
        return "{:03d}\xb0{}'{:.2f}\"N".format(degrees,minutes,seconds)
    elif lat < 0:
        lat = -lat
        degrees = int(lat)
        minutes = int((lat - degrees) * 60)
        seconds = (lat - degrees - minutes / 60) * 3600
        return "{:03d}\xb0{}'{:.2f}\"S".format(degrees,minutes,seconds)
    elif lat == 0:
        degrees = 0
        minutes = 0
        seconds = 0 
        return "{:03d}\xb0{}'{:.2f}\"S".format(degrees,minutes,seconds)

def convert_long(long):
    '''
    The purpose of this function is to take a specified longitude in decimal format, long, and calculate and return that longitude in DMS format (see return statements).
    '''    
    if long > 0:
        degrees = int(long)
        minutes = int((long - degrees) * 60)
        seconds = (long - degrees - minutes / 60) * 3600
        return "{:03d}\xb0{}'{:.2f}\"E".format(degrees,minutes,seconds)
    elif long < 0:
        long = -long
        degrees = int(long)
        minutes = int((long - degrees) * 60)
        seconds = (long - degrees - minutes / 60) * 3600
        return "{:03d}\xb0{}'{:.2f}\"W".format(degrees,minutes,seconds)
    elif long == 0:
        degrees = 0
        minutes = 0
        seconds = 0 
        return "{:03d}\xb0{}'{:.2f}\"S".format(degrees,minutes,seconds)
    
def distance(lat_deg1,long_deg1,lat_deg2,long_deg2):
    '''
    The purpose of this fuction is to take the latitude in degrees of the first coordinate, lat_deg1, the longitude in degrees of the first coordinate, long_deg1, the latitude in degrees of the second coordinate, lat_deg2, and the longitude in degrees of the first second, long_deg2, convert them from degrees to radians, and to calculate the distance between the locations of the coordinates. Returned is the distance, distance.
    '''
    lat1 = math.pi/180*lat_deg1
    long1 = math.pi/180*long_deg1
    lat2 = math.pi/180*lat_deg2
    long2 = math.pi/180*long_deg2
    change_lat = lat2 - lat1
    change_long = long2 - long1
    R = 3959.191
    a = (math.sin(change_lat/2)**2)+math.cos(lat1)*math.cos(lat2)*(math.sin(change_long/2)**2)
    distance = 2*R*math.asin(math.sqrt(a))
    return distance
               
##arbitrary string (in this case, the word selected is "begin") used in order to begin the while loop
command = "begin"
               
##while loop used to continue to ask the user for command inputs until they enter the command "end"
while not command.lower() == 'end':
    command = input("Command ('loc', 'zip', 'dist', 'end') => ")
    print(command)    
    
    ##if statement for if the user enters "loc" (case insentive, hence the lower())
    if command.lower() == 'loc':
        zip_code = str(input("Enter a ZIP code to lookup => "))
        print(zip_code)
        i = 0
        all_zips = []
        zip_codes = hw4_util.read_zip_all()
        ##while loop used to append all of the zip codes from the lists in zip_codes into the list all_zips, creating a list of all of the zip codes
        while i < len(zip_codes):
            all_zips.append(zip_codes[i][0])
            i+=1      
        ##the created list all_zips is being used to check if the inputted code is valid, or is present in the all_zips list
        if all_zips.count(zip_code) == 0:
            print("Invalid or unknown ZIP code")
        elif all_zips.count(zip_code) > 0:
            results = location_by_zip(zip_codes, zip_code)
            print("ZIP code {} is in {}, {}, {} county,".format(zip_code,results[2],results[3], results[4]))
            print("\tcoordinates: ({},{})".format(convert_lat(results[0]), convert_long(results[1])))
        print()
        
    ##elif statement for if the user enters "zip" (case insentive, hence the lower())
    elif command.lower() == 'zip':
        city = input("Enter a city name to lookup => ")
        print(city)
        city = city.title()
        state = input("Enter the state name to lookup => ")
        print(state)
        state = state.upper()
        ##creates of list, list_codes of codes returned by calling the function zip_by_location
        list_codes = list(zip_by_location(zip_codes, (city, state)))
        ##list_codes used in the if statement to check whether the location entered by the user returns any zip codes
        if len(list_codes) == 0:
            print("No ZIP code found for {}, {}".format(city, state))
        elif len(list_codes) > 0:
            list_codes = ", ".join(list_codes)
            print("The following ZIP code(s) found for {}, {}: {}".format(city, state, list_codes))
        print()

    ##elif statement for if the user enters "dist" (case insentive, hence the lower())
    elif command.lower() == 'dist':
        first_code = str(input("Enter the first ZIP code => "))
        print(first_code)
        second_code = str(input("Enter the second ZIP code => "))
        print(second_code)
        i = 0
        all_zips = []
        zip_codes = hw4_util.read_zip_all()
        ##while loop used to append all of the zip codes from the lists in zip_codes into the list all_zips, creating a list of all of the zip codes
        while i < len(zip_codes):
            all_zips.append(zip_codes[i][0])
            i+=1      
        ##the created list all_zips is being used to check if the inputted zip codes are valid, or is present in the all_zips list
        if all_zips.count(first_code) == 0 or all_zips.count(second_code) == 0:
            print("The distance between {} and {} cannot be determined".format(first_code,second_code))
        elif all_zips.count(first_code) > 0 and all_zips.count(second_code) > 0:    
            first_results = location_by_zip(zip_codes, first_code)
            second_results = location_by_zip(zip_codes, second_code)
            lat1 = first_results[0]
            long1 = first_results[1]
            lat2 = second_results[0]
            long2 = second_results[1]
            distance = distance(lat1,long1,lat2,long2)        
            print("The distance between {} and {} is {:.2f} miles".format(first_code,second_code,distance))
        print()
        
    ##elif statement for if the user enters "end" (case insentive, hence the lower())
    elif command.lower() == 'end':
        print()
        print("Done")
        
    ##else statement for if the user enters anything other than 4 commands listed
    else:
        print("Invalid command, ignoring")
        print()