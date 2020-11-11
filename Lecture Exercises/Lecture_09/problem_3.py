value = int(input("Enter a value (0 to end): "))
print(value)

list = []

while not value == 0:
    list.append(value)
    value = int(input("Enter a value (0 to end): "))
    print(value)
    
if value == 0:
    print("Min: {}".format(min(list)))
    print("Max: {}".format(max(list)))
    print("Avg: {:.1f}".format(sum(list)/len(list)))
