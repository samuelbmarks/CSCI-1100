def get_words(description):
    description = description.replace("."," ")
    description = description.replace(","," ")
    description = description.replace("("," ")
    description = description.replace(")"," ")
    description = description.replace("\'"," ")
    description = description.lower()
            
    word_list = description.split()
    empty = ""
    for i in range(len(word_list)):
        if word_list[i].isalpha() and len(word_list[i]) >= 4:
            empty+=word_list[i]+' '

    word_set = set(empty.split())
    num_words = len(word_set)
    return num_words, word_set
        
club1 = input("Enter a club: ")
print(club1)
print()

open_club1 = open(club1+".txt")
read_club1 = open_club1.read()
split_club1 = read_club1.split("|")
dc1 = split_club1[1]
word_set1 = get_words(dc1)[1]

num_same_list = []

for club in open("allclubs.txt"):
    split_club = club.split("|")
    club_name = split_club[0]
    dc = split_club[1]
    word_set = get_words(dc)[1]
    if word_set != word_set1:
        same_words = word_set & word_set1
        num_same_list.append((len(same_words),club_name))

num_same_list.sort(reverse=True)

print("Top 5 Most Similiar Clubs:")
print(num_same_list[0][1])
print(num_same_list[1][1])
print(num_same_list[2][1])
print(num_same_list[3][1])
print(num_same_list[4][1])