#!/usr/bin/env python3
# enter the genre
# search through list

# Possible futre things
# Weighting
# cleaning inputs
#
print("Welcome to the world's greatest movie tool!")

username = input("Please enter a username: ")
while not username:
    username = input("Please enter a valid username")
foundGenre = False
genreList = ["Drama", "Action", "Comedy", "SciFi", "Documentary", "Romance", \
             "Fantasy"]
while not foundGenre:
    print(genreList)
    genre = input("What is your favorite genre? ")
    if genre not in genreList:
        print("bad input")
    else:
        foundGenre = True
actor = input("Who is your favorite actor? ")
for line in open('movieData.csv'):
    if genre in line or actor in line:
        print(line)

output_file = open(username + '.txt', 'w')
output_file.write("Username: " + username + '\n')
output_file.write("Genres: " + genre + '\n')
output_file.write("Actors: " + actor + '\n')
output_file.close()
