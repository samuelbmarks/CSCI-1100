'''
HW 4 Part 1
The purpose of this code is to have a user enter a word and check whether the word has at least 8 characters, has alternating consonants and vowels, and the vowels are in non-decreasing alphabetical order. The program will continuously ask the user for additional words until an empty string is inputted.
CSCI1100 Spring 2018
Author: Samuel Marks
'''
def is_alternating(word1):
    '''
    The purpose of this function is to test if the conditions outlined in the program description are met in and returns True if they are and False otherwise. This fuction takes only one argument, word1, which is the word inputted by the user.
    '''
    ##Because the program is case insensitive, the inputted word is changed to all lowercase
    word = word1.lower()
    num_characters = len(word)
    
    ##If statement used to check that the word has at least 8 characters
    if num_characters < 8:
        print("The word '{}' is not alternating".format(word1))
        return False
    
    ##for loop used to check that the word contains only letters
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in range(num_characters-1):
        if word[i] not in letters:
            print("The word '{}' is not alternating".format(word1))
            return False
        i+=1
    
    ##for loop to check that the word has alternating consonants and vowels by assuring that at a given letter in the word, if that letter is a vowel (or is present in the created vowels list), the following letter is not a vowel, or if that letter is not a vowel (or is not present in the created vowels list), the following letter is a vowel
    vowels = ['a','e','i','o','u']
    for i in range(num_characters-1):
        if word[i] in vowels:
            if word[i+1] in vowels:
                print("The word '{}' is not alternating".format(word1))
                return False
        if word[i] not in vowels:
            if word[i+1] not in vowels:
                print("The word '{}' is not alternating".format(word1))
                return False
    
    ##for loop that alternating vowels are in non-decreasing alphabetical order
    vowel = ""
    for i in range(num_characters):
        if word[i] in vowels and vowel == "":
            vowel += word[i]
            continue
        if word[i] in vowels and word[i] >= vowel:
            vowel = word[i]
            continue
        if word[i] in vowels and word[i] < vowel:
            print("The word '{}' is not alternating".format(word1))
            return False
    
    ##print and return statement for if the word meets all of the conditions
    print("The word '{}' is alternating".format(word1))
    return True

##arbitrary string (in this case, the word selected is "begin") used in order to begin the while loop
word = "begin"

##while loop used in order to continue to ask the user to input a word until the user enters an empty string
while word != "":
    word = str(input("Enter a word: "))
    print(word)
    if word != "":
        is_alternating(word)
        print()