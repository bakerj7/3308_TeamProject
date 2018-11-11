#!/usr/bin/env python3
# enter the genre
# search through list

# Possible futre things
# Weighting
# cleaning inputs
#
import os

#---------------------------------------------------
#Function to create folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
#---------------------------------------------------

print("Welcome to the world's greatest movie tool!")

username = input("Please enter a username: ")
while not username:
    username = input("Please enter a valid username")
foundGenre = False
genreList = ["Action", "Adventure", "Animation", "Biography", \
             "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", \
             "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller", "Western" ]
#Input Genre
while not foundGenre:
    print(genreList)
    genre = input("What is your favorite genre? ")
    if genre not in genreList:
        print("bad input")
    else:
        foundGenre = True
#Input Actor
actor = input("Who is your favorite actor? ")

#Find Results
movieList = []
foundActor = False
for line in open('movieData.csv'):
    if genre in line or actor in line:
        print(line)
        movieList.append(line)
        if actor in line and foundActor == False:
            foundActor = True

if( not foundActor):
    print("***Actor " + actor + " was not found.  Results used 'NONE' for actor***")

#Output user results to txt file
print("***Currently exporting results***")

#output_file = open(username + '.txt', 'w')
createFolder('./Lists/')
output_file = open('./Lists/' + username + '.txt', 'w')
output_file.write("Username: " + username + '\n')
output_file.write("Genres: " + genre + '\n')
output_file.write("Actors: " + actor + '\n')
#Output list
output_file.write("CSV Line: " + '\n')
for i in movieList:
    output_file.write(i + '\n')
output_file.close()

#---------------------------------------------------
#Function to create folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
