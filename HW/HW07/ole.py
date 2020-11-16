def found(dictionary,word):
    if word in dictionary:
        return True
    else:
        return False

def drop(dictionary,word):  
    matches = set()
    for i in range(len(word)):
        drop = word[:i] + word[i+1:]
        if drop in dictionary:
            matches.add(drop)
    
    matches = list(matches)
    if len(matches) == 0:
        return False
    else:
        matches_dict = {}
        for i in range(len(matches)):
            matches_dict[matches[i]] = dictionary.get(matches[i])
        return matches_dict
    
def insert(dictionary,word):
    matches = set()
    letters =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
    for letter in letters:
        insert = letter+word
        if insert in dictionary:
            matches.add(insert)
    for i in range(len(word)+1):
        for letter in letters:
            insert = word[:i]+letter+word[i:]
            if insert in dictionary:
                matches.add(insert)
    matches = list(matches)
    if len(matches) == 0:
        return False
    else:
        matches_dict = {}
        for i in range(len(matches)):
            matches_dict[matches[i]] = dictionary.get(matches[i])
        return matches_dict      
    
def swap(dictionary,word):
    matches = set()
    for i in range(len(word)-1):
        if i == 0:
            swap = word[i+1]+word[i]+word[2:]
        else:
            swap = word[:i]+word[i+1]+word[i]+word[i+2:]
        
        if swap in dictionary:
            matches.add(swap)
    
    matches = list(matches)
    if len(matches) == 0:
        return False
    else:
        matches_dict = {}
        for i in range(len(matches)):
            matches_dict[matches[i]] = dictionary.get(matches[i])
        return matches_dict    
    
def replace(dictionary,word,keys):
    matches = set()
    letters = []
    for i in range(len(word)-1,-1,-1):
        letter = word[i]
        letters = keys[letter]
        for letter in letters:
            replace = word.replace(word[i],letter)
            if replace in dictionary:
                matches.add(replace)
                
    matches = list(matches)
    if len(matches) == 0:
        return False
    else:
        matches_dict = {}
        for i in range(len(matches)):
            matches_dict[matches[i]] = dictionary.get(matches[i])
        return matches_dict        
              
'''
d_file = input("Dictionary file => ")
print(d_file)
i_file = input("Input file => ")
print(i_file)
k_file = input("Keyboard file => ")
print(k_file)
'''

d_file = 'words_10percent.txt'
i_file = 'input_words.txt'
k_file = 'keyboard.txt'

dictionary = {}
for line in open(d_file):
    line = line.strip() 
    word_frequency = line.split(",")
    word = word_frequency[0]
    frequency = word_frequency[1]
    dictionary[word] = frequency   

inputs = []
for line in open(i_file):
    word = line.strip()
    inputs.append(word)

keys = {}
for line in open(k_file):
    line = line.strip()
    line = line.split(" ",1)
    key = line[0]
    alt = line[1].split(" ")
    keys[key] = alt
    
for word in inputs:
    if found(dictionary,word) == True:
        print("{:15s} -> {:15s} :FOUND".format(word,word))
    else:
        all_matches = {}
        if drop(dictionary,word) != False:
            match = drop(dictionary,word)
            all_matches.update(match)
        if insert(dictionary,word) != False:
            match = insert(dictionary,word)
            all_matches.update(match)
        if swap(dictionary,word) != False:
            match = swap(dictionary,word)
            all_matches.update(match)
        if replace(dictionary,word,keys) != False:
            match = replace(dictionary,word,keys)
            all_matches.update(match)
        if len(all_matches) > 0:
            all_matches = sorted(all_matches.items(),key=lambda x:(x[1],x[0]),reverse=True)
            i = 0
            while(i < 3 and i < len(all_matches)):
                print("{:15s} -> {:15s} :".format(word,all_matches[i][0])+"MACTH %d" %(i+1))
                i+=1
        else:
            print("{:15s} -> {:15s} :NO MATCH".format(word,word))
