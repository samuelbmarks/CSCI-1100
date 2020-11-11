
f_list = [ 19.4, 45.8, 25.2, -16, 82.19, 63.6, 45.1 ]
c_list = [((word-32)*(5/9)) for word in f_list]
line = ''
for c in c_list:
    if c > 0:
        line += '{:.2f}'.format(c) + ' '
print(line.strip())
