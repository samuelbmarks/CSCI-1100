import json
#import data from file and store them in two dictionaries
movies = json.loads(open("movies.json").read()) 
ratings = json.loads(open("ratings.json").read())

#function that used to calculated the average rate of a single movie
def average_rate(w1,w2,ID):
    imbd_rating = movies[ID]['rating']
    avg_twitter_rating = sum(ratings[ID])/len(ratings[ID])
    avg_rate = (w1 * imbd_rating + w2 * avg_twitter_rating) / (w1+w2)
    return avg_rate

#function that used to find tha appropriate movies with suitable movie year and genre(same with input genre)
def movies_in_limit(min_y,max_y,key_for_both,genre):
    m = dict()
    for ID in key_for_both:
        if movies[ID]['movie_year'] >= min_y and movies[ID]['movie_year'] <= max_y:
            for g in movies[ID]['genre']:
                if g.lower() == genre:
                    m[ID] = movies[ID]
    return m

#find out the ids that in both dictionaries
key_in_both = set()
key_in_imdb = set()
key_in_twitter = set()
for key in movies:
    key_in_imdb.add(key)
for key in ratings:
    if len(ratings[key]) >= 3:
        key_in_twitter.add(key)
key_in_both = key_in_imdb & key_in_twitter

#input needed information
min_y = int(input('Min year => '))
print(min_y)
max_y = int(input('Max year => '))
print(max_y)
w_imbd = input('Weight for IMDB => ')
print(w_imbd)
w_imbd = float(w_imbd)
w_twit = input('Weight for Twitter => ')
print(w_twit)
w_twit = float(w_twit)

print('')

while True:
    genre = input('What genre do you want to see? ')
    print(genre)
    genre = genre.lower()
    data = movies_in_limit(min_y,max_y,key_in_both,genre)
    
    #break the loop if the user enter 'stop'  
    if genre == 'stop':
        break
    
    else:
        print('')
        
        #if the entered gerne can not be found in the dictionary
        if len(data) == 0:
            print('No {} movie found in {} through {}'.format(genre.title(), min_y, max_y))
            print('')
            
        else:
            rank = []
            for ID in data:
                avg_rate = average_rate(w_imbd,w_twit,ID)
                rank.append((avg_rate,data[ID]['name'],data[ID]['movie_year']))
            
            #sort and find the best and the worst movies with calculated average rate
            rank.sort()
            best = rank[-1]
            worst = rank[0]
            
            print('Best:')
            print('\tReleased in {}, {} has a rating of {:.2f}'.format(best[2],best[1],best[0]))
            print('')
            print('Worst:')
            print('\tReleased in {}, {} has a rating of {:.2f}'.format(worst[2],worst[1],worst[0]))
            print('')