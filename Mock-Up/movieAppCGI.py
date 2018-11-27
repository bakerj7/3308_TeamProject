#!/usr/bin/python
# enter the genre
# search through list

# Possible futre things
# Weighting
# cleaning inputs
#
import os
import cgi

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
def createList(username, genre, actor):
    #username = input("Please enter a username: ")
    while not username:
        username = input("Please enter a valid username")
    #foundGenre = False
    genreList = ["Action", "Adventure", "Animation", "Biography", \
                 "Comedy", "Crime", "Documentary", "Drama", "Family", "Fantasy", \
                 "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller", "Western" ]
    #Input Genre
    '''
    while not foundGenre:
        print(genreList)
        genre = input("What is your favorite genre? ")
        if genre not in genreList:
            print("bad input")
            raise ValueError
        else:
            foundGenre = True
    '''
    #Input Actor
    #actor = input("Who is your favorite actor? ")

    #Find Results
    movieList = []
    #foundActor = False
    for line in open('movieData.csv'):
        if (genre in line and actor in line) or (genre in line and actor == "None"):
            movieList.append(line)
            print(line.split(",")[0]+"<br>")
        #if actor in line and foundActor == False:
            #foundActor = True
    '''
    if(not foundActor and actor != "None"):
        raise ValueError
        print("***Actor " + actor + " was not found.  Results used 'NONE' for actor***")
        
    '''

    #Output user results to txt file
    output_file = open(username + '.txt', 'w')
    output_file.write("Username: " + username + '\n')
    output_file.write("Genres: " + genre + '\n')
    output_file.write("Actors: " + actor + '\n')
    print("***Currently exporting results***")

    #output_file = open(username + '.txt', 'w')
    #createFolder('./Lists/')
    #Output list
    output_file.write("CSV Line: " + '\n')
    for i in movieList:
        output_file.write(i + '\n')
    output_file.close()
#---------------------------------------------------
def findFile(username):
    fileName = "./Lists/"+username+".txt" #form file name from user name
    return os.path.exists(fileName)
    
#---------------------------------------------------
#Function to search for pre-made list
def search():
    username = input("What is your username? ")
    if findFile(username): #check if file exists
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

def main():
    print("Content-type:text/html\r\n\r\n")
    print("<html><body>")
    print("<h1 style='text-align:center;'>Create a List</h1>")
    form = cgi.FieldStorage()
    if form.getvalue("Username") and form.getvalue("Genre") and form.getvalue("Actor/Actress"):
        username = form.getvalue("Username")
        genre = form.getvalue("Genre")
        actor = form.getvalue("Actor/Actress")
        createList(username, genre, actor)
    print("<div style = 'border-left: 20px solid white; border-right: 70px solid white'>")
    print("<form method='post' action='movieApp.py'>")
    print("USERNAME:<br>")
    print("<input type='text' name='Username' size='32' maxlength='40'><br>")
    print("GENRE:<br>")
    print("<input type='text' name='Genre' size='32' maxlength='40'><br>")
    print("ACTOR/ACTRESS:<br>")
    print("<input type='text' name='Actor/Actress' size='32' maxlength='40'><br> <br>")
    print("<input type='submit' value='FIND IT!' />")
    #print("<button>FIND IT!</button>")
    print("</form>")
    print("</div>")
    print("</body></html>")
   # print("Welcome to the world's greatest movie tool!")
    #mode = input('Would you like to create a list ("c") or search for a pre-existing list ("s")? ')
    #pickMode(mode)
    
if __name__ == "__main__": 
    main()
