"""
Lecture Exercise 12 Part 3
Author: Samuel Marks
CSCI1100 Spring 2018
"""
def find_min(list_of_lists):
    min_list = []
    for list in list_of_lists:
        for number in list:
            min_list.append(number)
    minimum = min(min_list)
    return minimum

if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], \
              [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )