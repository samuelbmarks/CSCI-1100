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
        
file_name = input("Enter file name: ")
open_file = open(file_name)
read_file = open_file.read()

split_text = read_file.split("|")
dc = split_text[1]

print("File {} {} words".format(file_name,get_words(dc)[0]))
print(get_words(dc)[1])
