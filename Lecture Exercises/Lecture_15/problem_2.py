imdb_file = input("Data file name: ").strip()
print(imdb_file)
prefix = str(input("Prefix: "))
print(prefix)
name_list = []
match_prefix = []
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    last_name = name.split(',')[0]
    name_list.append(last_name)
    if last_name.startswith(prefix):
        match_prefix.append(last_name)

name_set = set(name_list)
match_set = set(match_prefix)

num_names = len(name_set)
num_matches = len(match_set)

print("{} last names".format(num_names))
print("{} start with {}".format(num_matches, prefix))