from Date import month_names
from Date import Date


def list_dates(file):
    for line in open(file):
        line = line.split(' ')
        date = Date(int(line[0]),int(line[1]),int(line[2]))
        dates_list.append(date)
    return dates_list
    
dates_list = []
list_dates("birthdays.txt")

oldest = dates_list[0]
for i in range(1,len(dates_list)):
    if oldest > dates_list[i]:
        oldest = dates_list[i]

youngest = dates_list[0]
for i in range(1,len(dates_list)):
    if youngest < dates_list[i]:
        youngest = dates_list[i]

counts = [0]*13
for i in range(len(dates_list)):
    counts[dates_list[i].month] += 1
    
month = month_names[counts.index(max(counts))]

print("Earliest birthday:",str(oldest))
print("Latest birthday:",str(youngest))
print("Month that has the most birthdays:",month)

    