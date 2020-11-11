'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self,year=1900,month=1,day=1):
        self.year = year
        self.month = month
        self.day = day
        
    def __str__(self):
        return "{}/{:02d}/{}".format(self.year, self.month, self.day)
    
    def same_day_in_year(self,self1):
        if self.day == self1.day and self.month == self1.month:
            return True
        else:
            return False
        
    def is_leap_year(self):
        if self.year%4==0: 
            if self.year%100==0 and self.year%400!=0:
                return False
            return True
        return False         
    
    def __lt__(self,self1):
        if self.year < self1.year:
            return True
        elif self.year == self1.year:
            if self.month < self1.month:
                return True
            elif self.month == self1.month:
                if self.day < self1.day:
                    return True
        else:
            return False
            
if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print ()    
    d1 = Date(2000, 3, 27)
    d2 = Date(2004, 4, 13)
    d3 = Date(2008, 3, 17)
    d4 = Date(1900, 8, 23)
    d5 = Date(2002, 6, 26)
    d6 = Date(2011, 5, 11)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d4: " + str(d4))
    print("d5: " + str(d5))
    print("d6: " + str(d6))
    print("D1 is leap year:", d1.is_leap_year())
    print("D2 is leap year:", d2.is_leap_year())
    print("D3 is leap year:", d3.is_leap_year())
    print("D4 is leap year:", d4.is_leap_year())
    print("D5 is leap year:", d5.is_leap_year())
    print("D6 is leap year:", d6.is_leap_year())
    print ()
    print("d1<d2", d1<d2)
    print("d2<d3", d2.__lt__(d3))
    print("d3<d4", d3.__lt__(d4))
    print("d4<d5", d4.__lt__(d5))  
    print("d5<d6", d5.__lt__(d6))  
    