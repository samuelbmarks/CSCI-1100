
points = [ (4,2), (1,-3), (-4, -6), (4,9), (-7,8), (-5,2), (6,2) ]
by_x = sorted((points),reverse=True)
y= sorted( by_x, key = lambda p: abs(p[1])+abs(p[0]), reverse=True)
##s_points = sorted( map(lambda x: (x[0]**2 + x[1]**2)**0.5, points))
##print(s_points)
print(y)