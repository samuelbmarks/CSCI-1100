import math

class Point2d(object):
    def __init__( self, x0=0, y0=0 ):
        self.x = x0
        self.y = y0
    
    def __str__(self):
        
        return "({},{})".format(self.x,self.y)
       
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dist(self, o):
        return math.sqrt( (self.x-o.x)**2 + (self.y-o.y)**2 )
    
    def scale(self,val):
        self.x =self.x*val
        self.y = self.y*val
    def dominates(self, other):
        if self.x>other.x and self.y>other.y:
            return True
        else:
            return False
    
    def __sub__(self,other):
        return str(Point2d(self.x - other.x, self.y-other.y))   
    def __mult__(self,other):
        return str(Point2d(self.x * other, self.y*other)) 
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
    
if __name__ == "__main__":
    p = Point2d(0,4)
    q = Point2d(5,10)
    leng = q.magnitude()
    leng = Point2d.magnitude(q)
    print("Magnitude {:.2f}".format( leng ))
    print("Distance is {:.2f}".format( p.dist(q) ))

    # Exercise 1 tests:
    p.scale(3)
    print('After scaling p = ({},{})'.format(p.x, p.y) )
    r = Point2d(3,5.5)
    r.scale(2)
    
    print('After scaling r = ({},{})'.format(r.x, r.y) )
    print('p dominates r:', p.dominates(r))
    print('r dominates p:', r.dominates(p))
    print('r dominates q:', r.dominates(q))
    
    # Exercise 2:  __str__ tests
    print("As a string p is " + str(p))
    print("As a string r is " + str(r))
    
    # Exercise 2:  other tests
    print('p - q =', str(Point2d.__sub__(p,q)) )
    print('q - r =', str(Point2d.__sub__(q,r)) )
    new_q = Point2d.__mult__(q,4)
    print('new_q is', str(new_q) )
    t = Point2d(0,12)
    u = Point2d(0,5)
    v = Point2d(5,12)
    print('p == t', str(Point2d.__eq__(p,t)))
    print('t == u', str(Point2d.__eq__(t,u)))
    print('t == v', str(Point2d.__eq__(t,v)))