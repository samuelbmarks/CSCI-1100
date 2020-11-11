values = [ 14, 10, 8, 19, 7, 13 ]

new_value1 = int(input("Enter a value: "))
print(new_value1)
values.append(new_value1)

new_value2 = int(input("Enter another value: "))
print(new_value2)
values.insert(2, new_value2)

print(values[3],values[-1])

difference = max(values) - min(values)
print("Difference: {}".format(difference))

avg = sum(values) / len(values)
print("Average: {:.1f}".format(avg))

values.sort()
middle1 = values[len(values)//2-1]
middle2 = values[len(values)//2]
median = (middle1+middle2)/2
print("Median: {:.1f}".format(median))
