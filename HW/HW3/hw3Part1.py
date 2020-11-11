'''
The purpose of this code is to print data about both a male and female name of an inputed rank and year. A more specific description of the data that is printed is outlined in the function descriptions.
CSCI1100 Spring 2018
Author: Samuel Marks
'''
import read_names

def female(year, rank):
    '''
    This function prints some statistics about the female name of an inputed rank, rank in an specific, inputed year, year. Statistics include the number of people with that name that year, the total names in the top 250 list that year, and the percentage of children in the list with the given name. Also printed is a histogram of '*'s for the inputed year, a year prior, and a year after where each '*' corresponds to 0.1 of a percent.
    '''
    read_names.read_from_file("top_names_1880_to_2014.txt")
    
    ##finds name of a given rank and year, defines that name in variable "name"
    (female_names,female_counts) = read_names.top_in_year(year,'F')
    print("The rank {} most popular female name in {} is {}".format(rank, year, female_names[rank-1]))
    print("\t{} out of {} or {:.2f}%".format(female_counts[rank-1],sum(read_names.all_female_counts[year-1880]),(female_counts[rank-1]/sum(read_names.all_female_counts[year-1880])*100)))
    print("Histogram for {}".format(female_names[rank-1]))
    name = female_names[rank-1]
   
    ##redefines female_names and female_counts to the year before the inputed year, finds the index (position) of the targeted name, finds the percent of the name used in that year, calculates the number of asterisks, prints histogram for that year
    (female_names,female_counts) = read_names.top_in_year((year-1),'F')
    ##if statement for if name does not appear in the list for a year
    if female_names.count(name) == 0:
        percent = 0
    else:
        position = read_names.all_female_names[(year-1)-1880].index(name)
        percent = female_counts[position]/sum(read_names.all_female_counts[(year-1)-1880])*100    
    ast = (int(percent*10))*'*'
    print("{}:\t{}\t({:.2f}%)".format(year-1,ast,percent))
    
    ##redefines female_names and female_counts to the inputed year, finds the index (position) of the targeted name, finds the percent of the name used in that year, calculates the number of asterisks, prints histogram for that year
    (female_names,female_counts) = read_names.top_in_year(year,'F')
    position = read_names.all_female_names[year-1880].index(name)
    percent = female_counts[position]/sum(read_names.all_female_counts[year-1880])*100
    ast = (int(percent*10))*'*'
    print("{}:\t{}\t({:.2f}%)".format(year,ast,percent))
    
    ##redefines female_names and female_counts to the year after the inputed year, finds the index (position) of the targeted name, finds the percent of the name used in that year, calculates the number of asterisks, prints histogram for that year 
    (female_names,female_counts) = read_names.top_in_year((year+1),'F')
    ##if statement for if name does not appear in the list for a year
    if female_names.count(name) == 0:
        percent = 0
    else:
        position = read_names.all_female_names[(year+1)-1880].index(name)
        percent = female_counts[position]/sum(read_names.all_female_counts[(year+1)-1880])*100           
    ast = (int(percent*10))*'*'
    print("{}:\t{}\t({:.2f}%)".format(year+1,ast,percent))
    
def male(year, rank):
    '''
    This function prints some statistics about the male name of an inputed rank, rank in an specific, inputed year, year. Statistics include the number of people with that name that year, the total names in the top 250 list that year, and the percentage of children in the list with the given name. Also printed is a histogram of '*'s for the inputed year, a year prior, and a year after where each '*' corresponds to 0.1 of a percent.
    '''
    read_names.read_from_file("top_names_1880_to_2014.txt")
    
    ##finds name of a given rank and year, defines that name in variable "name"
    (male_names,male_counts) = read_names.top_in_year(year,'M')
    print("The rank {} most popular male name in {} is {}".format(rank, year, male_names[rank-1]))
    print("\t{} out of {} or {:.2f}%".format(male_counts[rank-1],sum(read_names.all_male_counts[year-1880]),(male_counts[rank-1]/sum(read_names.all_male_counts[year-1880])*100)))
    print("Histogram for {}".format(male_names[rank-1]))
    name = male_names[rank-1]
    
    ##redefines male_names and male_counts to the year before the inputed year, finds the index (position) of the targeted name, finds the percent of the name used in that year, calculates the number of asterisks, prints histogram for that year
    (male_names,male_counts) = read_names.top_in_year((year-1),'M')
    
    ##if statement for if name does not appear in the list for a year
    if male_names.count(name) == 0:
        percent = 0
    else:
        position = read_names.all_male_names[(year-1)-1880].index(name)        
        percent = male_counts[position]/sum(read_names.all_male_counts[(year-1)-1880])*100
    
    ast = (int(percent*10))*'*'
    print("{}:\t{}\t({:.2f}%)".format(year-1,ast,percent))
    
    ##redefines male_names and male_counts to the inputed year, finds the index (position) of the targeted name, finds the percent of the name used in that year, calculates the number of asterisks, prints histogram for that year
    (male_names,male_counts) = read_names.top_in_year(year,'M')
    position = read_names.all_male_names[year-1880].index(name)
    percent = male_counts[position]/sum(read_names.all_male_counts[year-1880])*100
    ast = (int(percent*10))*'*'
    print("{}:\t{}\t({:.2f}%)".format(year,ast,percent))
    
    ##redefines male_names and male_counts to the year after the inputed year, finds the index (position) of the targeted name, finds the percent of the name used in that year, calculates the number of asterisks, prints histogram for that year 
    (male_names,male_counts) = read_names.top_in_year((year+1),'M')
    
    ##if statement for if name does not appear in the list for a year
    if male_names.count(name) == 0:
        percent = 0
    else:
        position = read_names.all_male_names[(year+1)-1880].index(name)
        percent = male_counts[position]/sum(read_names.all_male_counts[(year+1)-1880])*100     
    
    ast = (int(percent*10))*'*'
    print("{}:\t{}\t({:.2f}%)".format(year+1,ast,percent))
    
##input statements
year = int(input("Enter a year (1881-2013) => "))
print(year)
rank = int(input("Enter a rank (1-250) => "))
print(rank) 

if year > 2013 or year < 1881 or rank > 250 or rank < 1:
    print("{} is not in the range 1881-2013 or {} is not in the range 1-250".format(year,rank))
elif year >= 1881 and year <= 2013 and rank >= 1 and rank <= 250:
    female(year,rank)
    print()
    male(year,rank)