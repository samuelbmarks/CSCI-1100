'''
Lecture Exercises 11: Problem 1
CSCI1100 Spring 2018
Author: Samuel Marks
'''
def earlier_semester(s,s1):
    '''
    Function takes two tuples as arguments and returns "True" if the first tuple represents an earlier semester and "False" otherwise. 
    '''
    semester = s[0]
    year = s[1]
    semester1 = s1[0]
    year1 = s1[1]
    if semester == "Spring" and semester1 == "Fall" and year <= year1:
        return "True"
    elif semester == "Spring" and semester1 == "Spring" and year < year1:
        return "True"
    elif semester == "Fall" and semester1 == "Fall" and year < year1:
        return "True"
    else:
        return "False"

w1 = ('Spring',2015)
w2 = ('Spring',2014)
w3 = ('Fall', 2014)
w4 = ('Fall', 2015)
print( "{} earlier than {}? {}".format( w1, w2, earlier_semester(w1,w2)))
print( "{} earlier than {}? {}".format( w1, w1, earlier_semester(w1,w1)))
print( "{} earlier than {}? {}".format( w1, w4, earlier_semester(w1,w4)))
print( "{} earlier than {}? {}".format( w4, w1, earlier_semester(w4,w1)))
print( "{} earlier than {}? {}".format( w3, w4, earlier_semester(w3,w4)))
print( "{} earlier than {}? {}".format( w1, w3, earlier_semester(w3,w2)))