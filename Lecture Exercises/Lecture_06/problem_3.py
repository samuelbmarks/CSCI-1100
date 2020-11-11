fn = input("Enter the first number: ")
print(fn)
fn = float(fn)
sn = input("Enter the second number: ")
print(sn)
sn = float(sn)
average = float((fn+sn)/2)
if fn > 10 and sn > 10:
    print("Both are above 10.")
elif fn <= 10 and sn <= 10:
    print("Both are below 10.")
print("Average is", round(average, 2))