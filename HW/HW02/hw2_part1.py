'''
The goal is to calculate the appropriate size of a cube gum ball machine so that it is completey full at the start of the week, it does not runs out of gum balls before the end of the week, and it does not have too many gum balls left at the end of the week to go stale.
Author: Samuel Marks
CSCI1100 Spring 2018
Version 1
'''
import math

def find_volume_sphere(radius):
    '''
    Return the volume of the sphere given the radius, radius.
    '''
    volume_sphere = (4/3)*math.pi*radius**3
    return volume_sphere

def find_volume_cube(side):
    '''
    Return the volume of the cube given the side length, side.
    '''
    volume_cube = side**3
    return volume_cube

radius = (input("Enter the gum ball radius (in.) => "))
print(radius)
radius = float(radius)
weekly_sales = input("Enter the weekly sales => ")
print(weekly_sales)

total_gumballs = math.ceil(1.25*float(weekly_sales))
side_gumballs = math.ceil(math.pow(total_gumballs,(1/3)))
edge_length = float(radius)*float(side_gumballs)*2
target_sales = float(total_gumballs)
extra_gumballs = (float(side_gumballs)**3)-float(target_sales)

volume_cube = find_volume_cube(edge_length)
wasted_target = volume_cube - target_sales*find_volume_sphere(radius)
wasted_full = volume_cube - (total_gumballs+extra_gumballs)*find_volume_sphere(radius)

print()
print("The machine needs to hold {} gum balls along each edge.".format(side_gumballs))
print("Total edge length is {:.2f} inches.".format(edge_length))
print("Target sales were {:.0f}, but the machine will hold {:.0f} extra gum balls.".format(target_sales, extra_gumballs))
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,\nor {:.2f} cubic inches if you fill up the machine.".format(wasted_target, wasted_full))