class Ball(object):
    def __init__ (self,x,y,dx,dy,radius,color):
        self.x,self.y = x,y
        self.radius = radius
        self.dx,self.dy = dx,dy
        self.color = color
        self.isstopped = False 
        
    def position(self):
        return self.x,self.y

    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def bounding_box(self):
        bounding_box = (self.x-self.radius, \
                        self.y-self.radius,\
                        self.x+self.radius, \
                        self.y+self.radius)         
        return bounding_box
        
    def get_color(self):
        return self.color
        
    def some_inside(self,maxx,maxy):
        if 0 < self.x + self.radius and \
              self.x - self.radius < maxx and \
              0 < self.y + self.radius and \
              self.y - self.radius < maxy:     
            return True
        return False