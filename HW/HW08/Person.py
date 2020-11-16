'''
HW8 Person Class
Author: Samuel Marks
CSCI Spring 2018
'''
class Person(object):
    '''
    The purpose of this class is to organize information about a specific person.
    '''
    def __init__(self,name,radius,home,x,y,dx,dy):
        '''
        This initialization function takes the peron's name, their radius, thier home universe, their current x and y coordinates, and their current speed as arguments and assigns them each to a class instance variable.
        '''        
        self.name = name
        self.radius = radius
        self.home = home
        self.current = home
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.final_dx = 0
        self.final_dy = 0
        self.rewards = []
        self.rewardinfo = []
        self.points = 0
        
    def __str__(self):
        '''
        This method returns a string representation of the information provided about a specific person.
        '''
        return "{} of {} in universe {}\n    at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points".format(self.name,self.home,self.current,self.x,self.y,self.dx,self.dy,len(self.rewards),self.points)
    
    def winner(self):
        '''
        This method returns a string representation of the information provided about a specific person after they complete the simulation -- the speeds represent the speeds at which the individual was traveling right before they stopped.
        '''        
        return "{} of {} in universe {}\n    at ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points".format(self.name,self.home,self.current,self.x,self.y,self.final_dx,self.final_dy,len(self.rewards),self.points)
    
    def move(self):
        '''
        This method moves the individual by adding their 'speed' to their current position.
        '''
        self.x += self.dx
        self.y += self.dy
    
    def reward(self,x,y,points,name,universe):
        '''
        This method keeps track of an individual's rewards, the information about those rewards, and the individuals points, and new speed of the individual as a result of collecting a reward.  
        '''        
        self.rewards.append(name)
        self.points += points
        self.dx = self.dx-(len(self.rewards)%2)*(len(self.rewards)/6)*self.dx
        self.dy = self.dy-((len(self.rewards)+1)%2)*(len(self.rewards)/6)*self.dy
        info = name, universe, x, y, points
        self.rewardinfo.append(info)
    
    def collision(self):
        '''
        This method takes away an individuals reward when called (called when two individuals collide) and reverses the individuals speed/direction. Returned is the information about the reward that was dropped.
        '''
        drop = self.rewardinfo[0]
        self.rewardinfo.pop(0)
        self.points -= drop[4]
        self.rewards.pop(0)
        self.dx = -(self.dx+((len(self.rewards)%2)*(len(self.rewards)/6)*self.dx))
        self.dy = -(self.dy+(((len(self.rewards)+1)%2)*(len(self.rewards)/6)*self.dy))
        return drop[0], drop[1], drop[2], drop[3], drop[4]
    
    def portal(self, portal):
        '''
        This method changes an individuals current universe, x-coordinate in that universe, and y-coordinate in that universe to the universe specified by a portal.
        '''        
        self.current = portal[2]
        self.x = portal[3]
        self.y = portal[4]