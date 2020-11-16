w = input("Word => ")
print(w)
c = int((input("#columns => ")))
print(c)
r = int((input("#rows => ")))
print(r)
print("Your word is:",w)
print()

print("(a)")
c1 = "*** "*c
print(r*(c1+"\n"))

print("(b)")
c2 = "*** "*(c//2)
print((r//2)*(c1+"\n")+c2+"CS1",c2+("\n"+(r//2)*(c1+"\n")))

print("(c)")
top = c2+" ^  "+c2
bottom = c2+" v  "+c2
c3 = "*** "*((c//2)-1)
scnd = (c3+" /  ***  \  "+c3)
scndtolast =(c3+" \  ***  /  "+c3)
middle =(c3+" |  ***  |  "+c3+'\n')*((r-5)//2)
words = (c3+" |  CS1  |  "+c3)

print(top)
print(scnd)
print(middle,end='')
print(words)
print(middle,end='')
print(scndtolast)
print(bottom)