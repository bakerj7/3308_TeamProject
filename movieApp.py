#!/usr/bin/env python3
# enter the genre
# search through list

# Possible futre things
# Weighting
# cleaning inputs
#
print("Welcome to the world's greatest movie tool!")
foundGenre = False
genreList = ["Drama", "Action", "Comedy"]
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
