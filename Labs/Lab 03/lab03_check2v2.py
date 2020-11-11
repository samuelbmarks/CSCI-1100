'''
The goal of this code is to create a function that computes and returns the skew of a runner's recorded times.
Author: Samuel Marks
CSCI1100 Spring 2018
Version: 1
'''
def find_skew(time_1, time_2, time_3, time_4, time_5):
    '''
    Return the skew number given the runners' recorded times, time_1, time_2, time_3, time_4, time_5.
    '''
    avg = (time_1+time_2+time_3+time_4+time_5)/5
    var = (time_1-avg)**2 + (time_2-avg)**2 + (time_3-avg)**2 + (time_4-avg)**2 + (time_5-avg)**2
    var /= 5
    skew = (time_1-avg)**3 + (time_2-avg)**3 + (time_3-avg)**3 + (time_4-avg)**3 + (time_5-avg)**3
    skew /= 5
    skew = skew/var**3**0.5
    return skew

def find_min_max_avg(name, time_1, time_2, time_3, time_4, time_5):
    '''
    Return the min, max, and avg (avg after min and max are removed for data set) given a runner's name, name, and his/her recorded times, time_1, time_2, time_3, time_4, time_5.
    '''
    min_time = min(time_1, time_2, time_3, time_4, time_5)
    max_time = max(time_1, time_2, time_3, time_4, time_5)
    avg_time = ((time_1+time_2+time_3+time_4+time_5)-(min_time+max_time))/3
    print("{}'s stats-- min: {}, max: {}, avg: {:.1f}".format(name,min_time,max_time,avg_time))
    return None

print("Stan's running times have a skew of {:.2f}".format(find_skew(34,34,35,31,29)))
print("Kyle's running times have a skew of {:.2f}".format(find_skew(30,31,29,29,28)))
print("Cartman's running times have a skew of {:.2f}".format(find_skew(36,31,32,33,33)))
print("Kenny's running times have a skew of {:.2f}".format(find_skew(33,32,34,31,35)))
print("Bebe's running times have a skew of {:.2f}".format(find_skew(27,29,29,28,30)))
print()
find_min_max_avg("Stan",34,34,35,31,29)
find_min_max_avg("Kyle",30,31,29,29,28)
find_min_max_avg("Cartman",36,31,32,33,33)
find_min_max_avg("Kenny",33,32,34,31,35)
find_min_max_avg("Bebe",27,29,29,28,30)