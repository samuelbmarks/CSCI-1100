'''
HW8 Universe Class
Author: Samuel Marks
CSCI Spring 2018
'''
class Universe(object):
    '''
    The purpose of this class is to organize information about a specific universe. 
    '''
    def __init__(self,uname,rewards,portals):
        '''
        This initialization function takes the universe name, a list of rewards, and a list of portals as arguments and assigns them each to a class instance variable.
        '''
        self.uname = uname
        self.rewards = rewards
        self.portals = portals
        
    def __str__(self):
        '''
        This method returns a string representation of the information provided about a specific universe.
        '''
        universe = "Universe: {} ({} rewards and {} portals)".format(self.uname,len(self.rewards),len(self.portals))
            
        if len(self.rewards) == 0:
            rewards = "Rewards:\nNone"
        else:
            rewards = "Rewards:"
            for i in range(len(self.rewards)):
                x = self.rewards[i][0]
                y = self.rewards[i][1]
                points = self.rewards[i][2]
                uname = self.rewards[i][3]
                add = "\nat ({},{}) for {} points: {}".format(x,y,points,uname)
                rewards += add
        
        if len(self.portals) == 0:
            portals = "Portals:\nNone"
        else:
            portals = "Portals:"
            for i in range(len(self.portals)):
                from_name = self.uname
                from_x = self.portals[i][0]
                from_y = self.portals[i][1]
                to_name = self.portals[i][2]
                to_x = self.portals[i][3]
                to_y = self.portals[i][4]
                add = "\n{}:({},{}) -> {}:({},{})".format(from_name,from_x,from_y,to_name,to_x,to_y)
                portals += add
        
        return "{}\n{}\n{}".format(universe,rewards,portals)