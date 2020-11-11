'''
The goal of this program is to assess the tone of an inputed sentence as either happy, sad, or neutral.
Author: Samuel Marks
CSCI1100 Spring 2018
Version 1
'''
def number_happy(sentence):
    num_happy = sentence.lower().count("laugh")+sentence.lower().count("happiness")+sentence.lower().count("love")+sentence.lower().count("excellent")+sentence.lower().count("good")+sentence.lower().count("smile")
    return int(num_happy)

def number_sad(sentence):
    num_sad = sentence.lower().count("bad")+sentence.lower().count("sad")+sentence.lower().count("terrible")+sentence.lower().count("horrible")+sentence.lower().count("problem")+sentence.lower().count("hate")
    return int(num_sad)

sentence = input("Enter a sentence => ")
print(sentence)
print("Sentiment: {}{}".format("+"*number_happy(sentence),"-"*number_sad(sentence)))

if(number_happy(sentence)>number_sad(sentence)):
    print("This is a happy sentence.")
elif(number_happy(sentence)<number_sad(sentence)):
    print("This is a sad sentence.")
elif(number_happy(sentence)==number_sad(sentence)):
    print("This is a neutral sentence.")