"""
   Utility functions for Homework #3 Fall 2014

   To use this module, first import it

   import hw3_util

"""

def read_change(filename):
    """This function is to be used for part2 of the homework.

    Read a file containing one coin type per line, and each line containing
    the type of coin and the number, separated by a comma. It returns a list
    for all the coins read from the file.
    
    Call this function as:

    mycoins = hw3_util.read_coins(filename)
    
    where mycoins is a list of all your legos.

    For example, if you are given the following file contents:

    50, 6
    25, 2
    10, 2
    5, 1
    1, 2

    The above call will return the following list:

    [50, 50, 50, 50, 50, 50, 
     25, 25, 10, 10, 5, 1, 1]
    
    """
    
    all_coins = []
    for line in open(filename):
        line = line.strip("\n")
        coin_info = line.split(",")
        coin_type = int(coin_info[0].strip())
        coin_count = int(coin_info[1])
        for i in range(coin_count):
            all_coins.append(coin_type)
    return all_coins
        


if __name__ == "__main__":
    coins = read_change("coins.txt")
    print(coins)
