'''
Lecture 19:

Implementation of a Restaurant class to represent restaurant data from
Yelp, which we originally worked with in Lab 5.
'''

from Point2d import Point2d

class Restaurant(object):
    def __init__(self, name, lat, lon, address, url, category, scores):
        '''
        Initialize an object, including a name string, two floats to
        store the latitude and longitude, a list of strings to
        represent each line of an address, a string representing the
        url, a string representing the category of restaurant, and a
        list of scores.
        '''
        self.name = name
        self.loc = Point2d(float(lon), float(lat))
        self.address = address
        self.url = url
        self.category = category
        self.reviews = scores

    def __str__(self):
        '''
        Format the information about the restaurant as a multi-line string.
        Rather than outputing the whole list of reviews, the average review
        is output.
        '''
        s =  '      Name: ' + self.name + '\n'
        s += '  Lat/Long: ' + str(self.loc) + '\n'
        s += '   Address: ' + self.address[0] + '\n'
        for i in range(1,len(self.address)):
            s += '            ' + self.address[i]  + '\n'
        s += '  Category: ' + self.category + '\n'
        s += 'Avg Review: {:.2f}'.format( self.average_review() )  + '\n'
        return s

    def is_in_city(self, city_name):
        '''
        Return True iff the restaurant is in the given city.  This is
        realized by testing the beginning of the last-line of the
        address (a list), up until the ,
        '''
        city_state = self.address[1].split(',')
        city = city_state[0]
        if city == 'Troy':
            return True
        
    def average_review(self):
        '''
        Calculate and return the average rating.  Return a -1 if there
        are none.
        '''
        if len(self.reviews) == 0:
            return -1
        elif len(self.reviews) > 0:
            sum_reviews = sum(self.reviews)
            num_reviews = len(self.reviews)
            avg_review = sum_reviews / num_reviews
            return avg_review

    def min_review(self):
        '''
        Return the minimum review, and -1 if there are no reviews
        '''
        if len(self.reviews) == 0:
            return -1
        elif len(self.reviews) > 0:
            min_review = min(self.reviews)
            return min_review

    def max_review(self):
        '''
        Return the maximum review, and -1 if there are no reviews
        '''
        if len(self.reviews) == 0:
            return -1
        elif len(self.reviews) > 0:
            max_review = max(self.reviews)
            return max_review        

    def latitude(self):
        '''
        Return the latitude stored in the Point2d object
        '''
        return self.loc.y

    def longitude(self):
        '''
        Return the longitude stored in the Point2d object
        '''
        return self.loc.x

if __name__ == "__main__":
    """
    This is relatively minimal testing code for the Restaurant class.
    Observe that when you import the Restaurant into the lecture 19
    example programs, this code is not run.
    """
    
    n = "Uncle Ricky's Bagel Heaven"
    lat = 42.73
    lon = -73.69
    address = [ '1809 5th Ave', 'Troy, NY 12180']
    url = "http://www.yelp.com/biz/uncle-rickys-bagel-heaven-troy"
    rest_type = 'Bagels'
    reviews = [ 5, 3, 5, 4, 3, 5, 4 ]
    rest1 = Restaurant( n, lat, lon, address, url, rest_type, reviews )

    n = "No Longer In Business"
    lat = 42.74
    lon = -73.7
    address = [ '123 Nowhere Street', 'Troy, NY 12180']
    url = "http://www.not_a_valid_url.biz/snafu"
    rest_type = 'Concrete'
    reviews = []
    rest2 = Restaurant( n, lat, lon, address, url, rest_type, reviews )

    print("First restaurant:")
    print("Name:", rest1.name)
    print("Latitude:", rest1.latitude() )
    print("Longitude:", rest1.longitude() )
    print("Min review:", rest1.min_review() )
    print("Max review:", rest1.max_review() )

    print("\nSecond restaurant:")
    print("Name:", rest2.name)
    print("Latitude:", rest2.latitude() )
    print("Longitude:", rest2.longitude() )
    print("Min review:", rest2.min_review() )
    print("Max review:", rest2.max_review() )
    
