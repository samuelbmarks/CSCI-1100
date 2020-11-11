imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    
    if movie in movies:
        movies[movie].add(name)
    else:
        movies[movie] = set()
        movies[movie].add(name)
        
singlets = 0
most = 0
for movie in movies:
    movie_ct = len(movies[movie])
    if movie_ct == 1:
        singlets += 1
    if movie_ct > most:
        most = movie_ct
        person = movie
                
print(most)
print(person)
print((singlets))