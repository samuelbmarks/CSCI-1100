imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)
counts= dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
        
names = sorted(counts)
limit = min(100, len(names))
count = 0
i = 0
x = ''
for index in range(len(names)):
    name = names[index]
    if counts[name] == 1:
        count += 1
    if counts[name] > i:
        x = name
        i = counts[name]
        
    
print("{} appears most often: {} times".format(x, i))  
print("{} people appear once".format(count))       
