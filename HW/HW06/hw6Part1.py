"""
Homework 6 Part 1
The purpose of this program is to read the name of two files: the first containing a dictionary of words and the second containing a list of words to autocorrect. The program will go through the list of words of the input file and decide whether the word preexists in the dictionary file, a letter in the word must be dropped, letters in the word must be swapped, a letter in the word must be replaced, or if there is no match whatsoever.
Author: Samuel Marks
CSCI 1100 Spring 2018
Version 1
"""
def found(dictionary,word):
    '''
    This function takes as argunments the dictionary inputted by the user, dictionary, and the current word being read by the input file, word, amd returns True if the word preexists in the dictionary and False otherwise. 
    '''
    if word in dictionary:
        return True
    else:
        return False
    
def drop(dictionary,word):
    '''
    This function takes as argunments the dictionary inputted by the user, dictionary, and the current word being read by the input file, word, and creates a new set of "words" by dropping a letter from that word and checks if any of those new "words" are present in the dictionary. If so, a print statement indicating that a letter was dropped is printed and True is returned. Otherwise, False is returned.
    '''
    ##converting the dictionary list into a set and creating a new set for new "words" created after a letter is dropped
    dictionary = set(dictionary)
    drop_words = set()
    
    ##for lopp to create new "words" by dropping a letter from word and to add them to drop_words
    for i in range(len(word)):
        drop = word[:i] + word[i+1:]
        drop_words.add(drop)
        
    ##if statement checks to see if any words in drop_words are present in the dictionary
    if len(drop_words & dictionary) >= 1:
        correct = list(drop_words & dictionary)
        print("{:15s} -> {:15s} :DROP".format(word,correct[0]))
        return True
    else:
        return False

def swap(dictionary,word):
    '''
    This function takes as argunments the dictionary inputted by the user, dictionary, and the current word being read by the input file, word, and creates a new set of "words" by swapping two consecutive letters from that word and checks if any of those new "words" are present in the dictionary. If so, a print statement indicating that letters were swapped is printed and True is returned. Otherwise, False is returned.
    '''    
    ##converting the dictionary list into a set and creating a new set for new "words" created after consecutive letters are swapped
    dictionary = set(dictionary)
    swap_words = set()
   
    ##for loop to create new "words" by swapping consecutive letters and to add them to swap_words
    for i in range(len(word)-1):
        if i == 0:
            swap_words.add(word[i+1]+word[i]+word[2:])
        else:
            swap_words.add(word[:i]+word[i+1]+word[i]+word[i+2:])
        
    ##if statement checks to see if any words in swap_words are present in the dictionary
    if len(swap_words & dictionary) >= 1:
        correct = list(swap_words & dictionary)
        print("{:15s} -> {:15s} :SWAP".format(word,correct[0]))
        return True
    else:
        return False

def replace(dictionary,word):
    '''
    This function takes as argunments the dictionary inputted by the user, dictionary, and the current word being read by the input file, word, and creates a new set of "words" by replacing a letter from that word (starting from the end of the word) with all the letters in the alphabet and checks if any of those new "words" are present in the dictionary. If so, a print statement indicating that a letter was replaced is printed and True is returned. Otherwise, False is returned.
    '''    
    ##creating a list of all letter in the alphabet, converting the dictionary list into a set, and creating a new set for new "words" created after letters are replaced
    letters =  [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'y', 'z' ]
    dictionary = set(dictionary)
    replace_words = set()
    
    ##for loop to create new "words" by replacing each letter in word with every letter in the alphabet starting fr0m the end of the word and to add those "words" to replace_words
    for i in range(len(word)-1,-1,-1):
        list_word = list(word)
        for l in range(len(letters)):
            list_word[i] = letters[l]
            new = "".join(list_word)
            replace_words.add(new)
            
            ##if statement checks to see if any words in replace_words are present in the dictionary
            if len(replace_words & dictionary) >= 1:
                correct = list(replace_words & dictionary)
                print("{:15s} -> {:15s} :REPLACE".format(word,correct[0]))
                return True
    return False

##input files
d_file = input("Dictionary file => ")
print(d_file)
i_file = input("Input file => ")
print(i_file)

##creating a list of all words present in the dictionary file (later this list will be converted to a set
dictionary = []
for line in open(d_file):
    word = line.strip()
    dictionary.append(word)

##creating a list of all words present in the input file (later this list will be converted to a set
inputs = []
for line in open(i_file):
    word = line.strip()
    inputs.append(word)

##for loop to check the proper action that should be taken for each word
for word in inputs:
    if found(dictionary, word) == True:
        print("{:15s} -> {:15s} :FOUND".format(word,word))
    elif drop(dictionary, word) == True:
        continue
    elif swap(dictionary, word) == True:
        continue
    elif replace(dictionary, word) == True:
        continue
    else:
        print( "{:15s} -> {:15s} :NO MATCH".format(word,word))   