import hw4_util
import math

def zip_codes(zip_codes, location):
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
    zip_codes = hw4_util.read_zip_all()
    i = 0
    while i < len(zip_codes):
        if zip_codes[i][0] == code:
            return zip_codes[i][1], zip_codes[i][2], zip_codes[i][3], zip_codes[i][4], zip_codes[i][5]
        i+=1
            
def convert_lat(lat):
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
    lat1 = math.pi/180*lat_deg1
    long1 = math.pi/180*long_deg1
    lat2 = math.pi/180*lat_deg2
    long2 = math.pi/180*long_deg2
    change_lat = lat2 - lat1
    change_long = long2 - long1
    R = 3959.191
    a = (math.sin(change_lat/2)**2)+math.cos(lat1)*math.cos(lat2)*(math.sin(change_long/2)**2)
    distance = 2*R*math.asin(a)
    return distance
               
command = input("Command ('loc', 'zip', 'dist', 'end') => ")
print(command)

all_zips = []
zip_codes = hw4_util.read_zip_all()
i = 0
while i < len(zip_codes):
    all_zips.append(zip_codes[i][0])
i+=1 

if command.lower() == 'loc':
    zip_code = str(input("Enter a ZIP code to lookup => "))
    print(zip_code)     
    if all_zips.count(zip_code) == 0:
        print("Invalid or unknown ZIP code")
    elif all_zips.count(zip_code) > 0:
        results = location_by_zip(zip_codes, zip_code)
        print("ZIP code {} is in {}, {}, {} county,\n\t coordinates: ({},{})".format(zip_code,results[2],results[3], results[4], convert_lat(results[0]), convert_long(results[1])))
        
elif command.lower() == 'zip':
    city = str(input("Enter a city name to lookup => "))
    print(city)
    city = city.title()
    state = str(input("Enter a state name to lookup => "))
    print(state)
    state = state.upper()
    list_codes = ', '.join(zip_codes(zip_codes, (city, state)))
    if len(list_codes) == 0:
        print("No ZIP code found for {}, {}".format(city, state))
    elif len(list_codes) > 0:
        print("The following ZIP code(s) found for {}, {}: {}".format(city, state, list_codes))

elif command.lower() == 'dist':
    first_code = str(input("Enter the first ZIP code: "))
    print(first_code)
    second_code = str(input("Enter the second ZIP code: "))
    print(second_code)
    first_results = location_by_zip(zip_codes, first_code)
    second_results = location_by_zip(zip_codes, second_code)
    lat1 = first_results[0]
    long1 = first_results[1]
    lat2 = second_results[0]
    long2 = second_results[1]
    distance = distance(lat1,long1,lat2,long2)
    print("The distance between {} and {} is {:.2f} miles".format(first_code,second_code,distance))

