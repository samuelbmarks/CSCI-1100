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
club2 = input("Enter another club: ")
print(club2)
print()
open_club1 = open(club1+".txt")
open_club2 = open(club2+".txt")
read_club1 = open_club1.read()
read_club2 = open_club2.read()

split_club1 = read_club1.split("|")
split_club2 = read_club2.split("|")
dc1 = split_club1[1]
dc2 = split_club2[1]

word_set1 = get_words(dc1)[1]
word_set2 = get_words(dc2)[1]

same_words = word_set1 & word_set2
unique_set1 = word_set1 - word_set2
unique_set2 = word_set2 - word_set1

print("Comparing clubs {} and {}:".format(club1,club2))
print()
print("Same words:",same_words)
print()
print("Unique to {}: {}".format(club1,unique_set1))
print()
print("Unique to {}: {}".format(club2,unique_set2))