import random
import time

""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""

def closest1(lst):
    """
    closest1(x) returns a tuple containing the two 
    closest values from a list of floats (or ints)
    
    >>> closest1([1,4,5,8,11])
    (5, 4)
    >>> closest1([24,32,35,41,50])
    (35, 32)
    >>> closest1([11])
    (None, None)
    """    
    if len(lst) < 2:
        return (None, None)
    diff = dict()
    for i in range(len(lst)):
        for x in range(len(lst)):
            l1 = lst[i]
            l2 = lst[x]
            if l1-l2 > 0:
                diff[l1-l2] = l1, l2
    return diff[min(diff)]
        
def closest2(lst1):
    """
    closest2(o) returns a tuple containing the two 
    closest values from a list of floats (or ints)
    
    >>> closest2([1,4,5,8,11])
    (5, 4)
    >>> closest2([24,32,35,41,50])
    (35, 32)
    """    
    newlist = lst1
    newlist.sort()
    diff=0
    for l in range(len(newlist)-1):
        if l==0:
            diff = newlist[1]-newlist[l]
            num= newlist[l]
            num2 = newlist[l+1]
            continue
        if (newlist[l+1]-newlist[l])<diff:
            diff = newlist[l+1]-newlist[l]
            num= newlist[l]
            num2=newlist[l+1]
    return num2,num

if __name__ == "__main__":
    pass

list1 = []
for i in range(100):
    value = random.uniform(0.0,1000.0)
    list1.append(value)
    
s = time.time()
(x,y) = closest1(list1)
e = time.time() - s
print("closest1: ({},{}), Time: {} seconds".format(x,y,e))

s = time.time()
(x,y) = closest2(list1)
e = time.time() - s
print("closest2: ({},{}), Time: {} seconds".format(x,y,e))

print()

list2 = []
for i in range(1000):
    value = random.uniform(0.0,1000.0)
    list2.append(value)
    
s = time.time()
(x,y) = closest1(list2)
e = time.time() - s
print("closest1: ({},{}), Time: {} seconds".format(x,y,e))

s = time.time()
(x,y) = closest2(list2)
e = time.time() - s
print("closest2: ({},{}), Time: {} seconds".format(x,y,e))

print()

list3 = []
for i in range(10000):
    value = random.uniform(0.0,1000.0)
    list3.append(value)
    
s = time.time()
(x,y) = closest1(list3)
e = time.time() - s
print("closest1: ({},{}), Time: {} seconds".format(x,y,e))

s = time.time()
(x,y) = closest2(list3)
e = time.time() - s
print("closest2: ({},{}), Time: {} seconds".format(x,y,e))