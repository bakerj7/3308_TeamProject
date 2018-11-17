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
#Function to call create or search
def pickMode(mode): #mode is user input string selecting create or search
    call = False
    while call == False: #keep asking for input until correct input is found
        if (mode[0] == "c"):
            createList()
            call = True #stop looping
        elif (mode[0] == "s"):
            search()
            call = True #stop looping
        else:
            #incorrect input, ask for new input
            mode = input('Unknown Input\nType "c" for create or "s" for search: ')
        
#---------------------------------------------------
#Function to create a new list
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
#Function to search for pre-made list
def search():
    username = input("What is your username? ")
    fileName = "./Lists/"+username+".txt" #form file name from user name
    if os.path.exists(fileName): #check if file exists
        #would user like to see list or just checking exists
        view = input('List found\nWould you like to view the list now ("y" or "n")? ')
        y_n = False
        while y_n == False: #loop until correct input found
            if (view[0] == "y"): #print list
                file = open(fileName,"r")
                for line in file:
                    print(line)
                y_n = True
            elif (view[0] == "n"): #ask user what they would like to do next
                mode = input('Would you like to create a list ("c") or search for another list ("s")? ')
                pickMode(mode) #function to call create or search based on user input
                y_n = True
            else:
                #incorrect input, ask for new input
                view = input('Unknown Input/nType "y" for yes or "n" for n: ')
    else: #list not found
        print("Sorry, list not found")
        mode = input('Would you like to create a list ("c") or search for another list ("s")? ')
        pickMode(mode) #function to call create or search based on user input
    
#---------------------------------------------------
        
print("Welcome to the world's greatest movie tool!")
mode = input('Would you like to create a list ("c") or search for a pre-existing list ("s")? ')
pickMode(mode)

