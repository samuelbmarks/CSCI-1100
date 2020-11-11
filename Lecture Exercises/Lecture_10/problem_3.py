co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
               348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

sum_levels = sum(co2_levels)
num_levels = len(co2_levels)
avg_level = sum_levels / num_levels

print("Average: {:.2f}".format(avg_level))

over_avg = []

for x in co2_levels:
    if x > avg_level:
        over_avg.append(x)
print("Num above average: {}".format(len(over_avg)))
        