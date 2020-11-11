#function that used to drop letter one by one from a word and store them into a set
def drop(word):
    drop_set = set()
    for index in range(len(word)):
        new_s = word[0:index] + word[index+1:]
        drop_set.add(new_s)
    return drop_set

#function that used to insert letters one by one in front or after the letters in word, sotre them in a set
def insert(word):
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z' ]
    insert_set = set()
    for index1 in range(len(word)):
        for index2 in range(len(letters)):
            new_s = word[0:index1] + letters[index2] + word[index1:]
            insert_set.add(new_s)
    for index2 in range(len(letters)):
        new_s = word + letters[index2]
        insert_set.add(new_s)            
    return insert_set
    
    
#function that used to swap adjacent letters one by one and store them into a set
def swap(word):
    swap_set = set()
    for index in range(len(word)-1):
        new_s = word[0:index] + word[index+1] + word[index] + word[index+2:]
        swap_set.add(new_s)
    return swap_set
    
#function that used to replace letter one by one with 24 letters and store them into a set
def replace(word):
    replace_set = set()
    for index1 in range(len(word)):
        for index2 in range(len(keyboard[word[index1]])):
            new_s = word[0:index1] + keyboard[word[index1]][index2] + word[index1+1:]
            replace_set.add(new_s)
    return replace_set

#transfer the data of dictionary into a dictionary
dic_file = input('Dictionary file => ')
print(dic_file)
inp_file = input('Input file => ')
print(inp_file)
key_file = input('Keyboard file => ')
print(key_file)

dictionary = dict()
for line in open(dic_file):
    line = line.split(',')
    dictionary[line[0]] = float(line[1])
    
#transfer the data of dictionary into a set
d = set()
for word in dictionary:
    d.add(word)

#store the letters in keyboard.txt into a dictionary
#the first letter is key, and the rest of them are values
keyboard = dict()
for line in open(key_file):
    line = line.strip().replace(' ','')
    keyboard[line[0]] = line[1:]

for word in open(inp_file):
    found = set()
    match = []
    word = word.strip()
    
    #if the word is correct
    if word in dictionary:
        print('{0:15} -> {1:15} :FOUND'.format(word, word))
    
    #if the word is wrong
    else:
        #if the word can be corrected by drop
        if len(drop(word) & d) != 0:
            found = found | (drop(word) & d)
        #if the word can be corrected by insert
        if len(insert(word) & d) != 0:
            found = found | (insert(word) & d)
        #if the word can be corrected by swap
        if len(swap(word) & d) != 0:
            found = found | (swap(word) & d)
        #if the word can be corrected by replace
        if len(replace(word) & d) != 0:
            found = found | (replace(word) & d)

        #if the word can not be corrected 
        if len(found) == 0:
            print('{0:15} -> {1:15} :NO MATCH'.format(word,word))
            
    for key in found:
        match.append((dictionary[key], key))
    
    #sort and find the three (or fewer) words with highiest frequency 
    match = sorted(match, reverse = True)   
    match = match[0:3]
    
    for index in range(len(match)):
        print('{0:15} -> {1:15} :MATCH {2}'.format(word, match[index][1], index+1))