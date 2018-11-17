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
def pickMode(mode):
    call = False
    while call == False:
        if (mode[0] == "c"):
            createList()
            call = True
        elif (mode[0] == "s"):
            search()
            call = True
        else:
            mode = input('Unknown Input\nType "c" for create or "s" for search: ')
        
#---------------------------------------------------
def createList():
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
def search():
    username = input("What is your username? ")
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    '''
    fileName = username+".txt"
    filePath = os.path.join(fileDir, fileName)
    file = open(filePath,"r")
    '''
    fileName = "./Lists/"+username+".txt"
    if os.path.exists(fileName):
        view = input('List found\nWould you like to view the list now ("y" or "n")? ')
        y_n = False
        while y_n == False:
            if (view[0] == "y"):
                file = open(fileName,"r")
                for line in file:
                    print(line)
                y_n = True
            elif (view[0] == "n"):
                mode = input('Would you like to create a list ("c") or search for another list ("s")? ')
                pickMode(mode)
                y_n = True
            else:
                view = input('Unknown Input/nType "y" for yes or "n" for n: ')
    else:
        print("Sorry, list not found")
        mode = input('Would you like to create a list ("c") or search for another list ("s")? ')
        pickMode(mode) 
    '''
    for root, dirs, files in os.walk("./Lists"):
        for file in files:
            print(os.path.join(root, file))
    '''
    
#---------------------------------------------------
        
print("Welcome to the world's greatest movie tool!")
mode = input('Would you like to create a list ("c") or search for a pre-existing list ("s")? ')
pickMode(mode)

