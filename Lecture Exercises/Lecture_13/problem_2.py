file  = input("Enter the scores file: ")
print(file)
file2 = input("Enter the output file: ")
print(file2)

f = open(file)
s = f.read().strip().split('\n')

for var in range(len(s)):
    s[var] = int(s[var])
s.sort()

second = open(file2,'w')
for var2 in range(len(s)):
    second.write("{:2d}: {:3d}\n".format(var2, s[var2]))