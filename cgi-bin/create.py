#!/usr/bin/env python3
# enter the genre
# search through list

# Possible futre things
# Weighting
# cleaning inputs
#
import os
import cgi
import urllib.request
import json
import sys

api_key = "a09a65714522b9ac6c337dd5feb7a7a3"

#---------------------------------------------------
#Function to create folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

#---------------------------------------------------
#Generate genre list from TMDB API
genre_response = urllib.request.urlopen(f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}')

genre_dict = {}
genre_data = json.load(genre_response)
for entry in genre_data['genres']:
    genre_dict[entry['name']] = entry['id']

#---------------------------------------------------
#Function to create a new list
def saveList(name, list, webBool):

    #Format
    movieList = []
    
    if (webBool == True):
        for entry in list.split(','):
            movieList.append(entry)
    else:
        movielist = list


    createFolder('./Lists/')
    output_file = open('./Lists/' + name + '.txt', 'w')
    output_file.write("List Name: " + name + '\n')
    output_file.write('\n')
    #Output list
    output_file.write("Movies: " + '\n')
    movies = ""
    for i in movieList:
        output_file.write(i + '\n')
        movies += i+"<br>" #built list for web search
    output_file.close()

    #save list to local storage
    if webBool == True:
        print('''
        <div id="store" style='display: none'></div>

        <script>
        // Check browser support
        if (typeof(Storage) !== "undefined") {
          // Store
          localStorage.setItem("'''+name+'''", "'''+movies+'''");
          // Retrieve
          document.getElementById("store").innerHTML = localStorage.getItem("'''+name+'''");
        } else {
          document.getElementById("store").innerHTML = "Sorry, your browser does not support Web Storage...";
        }
        </script>

        </body>
        </html>
        ''')

#---------------------------------------------------
#Function to create a new list
def createList(username, genre, actor, webBool):
    #This replaces spaces with '+' for API call
    actorplus = actor.replace(" ", "+")

    #Find Results
    movieList = []
    #foundActor = False
    genre_id = genre_dict[genre]

    #Query API
    actor_response = urllib.request.urlopen(f'https://api.themoviedb.org/3/search/person?api_key={api_key}&query={actorplus}')
    movie_response = urllib.request.urlopen(f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres={genre_id}')

    actor_data = json.load(actor_response)

    #print("\nMovies featuring " + actor +":\n")
    #if webBool == True:
                #print("<br>")
    for entry in actor_data['results']:
        for movie in entry['known_for']:
            if (webBool == True):
                print("<div class='result' id='"+ str(movie['id']) +"' >")
            print(movie['title'])
            if (webBool == True):
                print("</div>")
            movieList.append(movie['title'])
            #if webBool == True:
                #print("<br>")

    #if webBool == True:
                #print("<br>")
    movie_data = json.load(movie_response)
    #print("\n" + genre + " movies:\n")
    #if webBool == True:
                #print("<br>")
    for entry in movie_data['results']:
        if (webBool == True):
            print("<div class='result' id='"+ str(entry['id']) +"' >")
        print(entry['title'])
        if (webBool == True):
            print("</div>")
        movieList.append(entry['title'])
            
    if (webBool == False):
        saveList(username, movieList, False)
        
        
        #if webBool == True:
                #print("<br>")
        #movieList.append(entry['title'])

    #Output user results to txt file
    #print("\n")
    #print("***Currently exporting results***")
    #if webBool == True:
                #print("<br>")

    #output_file = open(username + '.txt', 'w')
    #createFolder('./Lists/')
    #output_file = open('./Lists/' + username + '.txt', 'w')
    #output_file.write("List Name: " + username + '\n')
    #output_file.write("Genres: " + genre + '\n')
    #output_file.write("Actors: " + actor + '\n')
    #Output list
    #output_file.write("Movies: " + '\n')
    #movies = ""
    #for i in movieList:
        #output_file.write(i + '\n')
        #movies += i+"<br>" #built list for web search
    #output_file.close()
    #save list to local storage
    #if webBool == True:
        #print('''
        #<div id="store" style='display: none'></div>

        #<script>
        #// Check browser support
        #if (typeof(Storage) !== "undefined") {
          #// Store
          #localStorage.setItem("'''+username+'''", "'''+movies+'''");
          #// Retrieve
          #document.getElementById("store").innerHTML = localStorage.getItem("'''+username+'''");
        #} else {
          #document.getElementById("store").innerHTML = "Sorry, your browser does not support Web Storage...";
        #}
        #</script>

        #</body>
        #</html>
        #''')

#---------------------------------------------------
# command line used
# get user input

def getInput():
    username = input("Please enter a username: ")
    while not username:
        username = input("Please enter a valid username")
    foundGenre = False

    #Input Genre
    while not foundGenre:
        print("\nGenre List: \n")
        for genre in genre_dict:
            print(genre)
        genre = input("\nWhat is your favorite genre? ")
        if genre not in genre_dict:
            print("bad input")
            raise ValueError
        else:
            foundGenre = True
    #Input Actor
    actor = input("Who is your favorite actor? ")
    #This replaces spaces with '+' for API call
    createList(username, genre, actor, False)

#---------------------------------------------------
# find file containing user's list

def findFile(username):
    fileName = "./Lists/"+username+".txt" #form file name from user name
    return os.path.exists(fileName)

#---------------------------------------------------
# web used
# print HTML

def web():
    print("Content-type: text/html")
    print("")
    print('''
    <!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="create_style.css" />
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <script src="movie_create.js" defer></script>
    </head>
    <body>
        <div id="banner">
              <form id="index_nav" method='post' action='index.py'></form>
              <div id="banner_logo">
                <embed id="logo" type="image/svg+xml" src="Logo.svg"/>
              </div>
              <div id="banner_title">
                <h1>MOVIE QUEUE</h1>
                <h2>What's Up Next!</h2>
              </div>
        </div>

        <div id="search_box">
            <form id="find_it_form" method='post' action='create.py'>
            <div id="search_title">SEARCH:</div>
            <div class="search_group">
              <div class="search_title">TITLE:</div>
              <input type="text" name="Title" placeholder="<None>" maxlength="60" onfocus="this.placeholder = ''" onblur="this.placeholder = '<None>'">
            </div>
            <div class="search_group">
              <div class="search_title">GENRE:</div>
              <input type="text" name="Genre" placeholder="<None>" maxlength="60" onfocus="this.placeholder = ''" onblur="this.placeholder = '<None>'">
            </div>
            <div class="search_group">
              <div class="search_title">ACTOR/ACTRESS:</div>
              <input type="text" name="Actor/Actress" placeholder="<None>" maxlength="60" onfocus="this.placeholder = ''" onblur="this.placeholder = '<None>'">
            </div>
            <div class="search_group">
              <div class="search_title">LOCATION:</div>
              <input type="text" name="Location" placeholder="<None>" maxlength="60" onfocus="this.placeholder = ''" onblur="this.placeholder = '<None>'">
            </div>
            <div class="search_group">
              <div class="search_title">RATING:</div>
              <input type="text" name="Rating" placeholder="<None>" maxlength="60" onfocus="this.placeholder = ''" onblur="this.placeholder = '<None>'">
            </div>
            <div class="search_group">
              <div class="search_title">YEAR:</div>
              <input type="text" name="Year" placeholder="<None>" maxlength="60" onfocus="this.placeholder = ''" onblur="this.placeholder = '<None>'">
            </div>
            <div class="search_group">
              <div class="search_title">KEYWORD(S):</div>
              <input type="text" name="Keyword(s)" placeholder="<None>" maxlength="60" onfocus="this.placeholder = ''" onblur="this.placeholder = '<None>'">
            </div>
            <div id="find_it"><div class="button_text">FIND IT!</div></div>
            </form>
        </div>

        <div id="results_box">
            <div id="results_title">SEARCH RESULTS:</div>
            <div id="results_table">
    ''')

    form = cgi.FieldStorage()
    if form.getvalue("Genre") and form.getvalue("Actor/Actress"):
        #username = form.getvalue("Username")
        username = "Test"
        genre = form.getvalue("Genre")
        actor = form.getvalue("Actor/Actress")
        #print("<div>SUCCESS!</div>")
        createList(username, genre, actor, True)

    if form.getvalue("SaveName") and form.getvalue("Movie_List"):
        name = form.getvalue("SaveName")
        list = form.getvalue("Movie_List")
        saveList(name, list, True)



    print('''
            </div>
            <!-- <div id="results_controls">
              <div id="results_select_all" class="control">SELECT ALL</div>
              <div id="results_select_none" class="control">SELECT NONE</div>
            </div> -->
            <div id="add_it"><div class="button_text">ADD IT!</div></div>
        </div>

        <div id="list_box">
            <div id="list_title">CURRENT LIST:</div>
            <div id="list_table">

            </div>
            <div id="list_controls">
              <!-- <div id="list_select_all" class="control">SELECT ALL</div>
              <div id="list_select_none" class="control">SELECT NONE</div> -->
              <div id="list_undo" class="control">UNDO SELECTED</div>
            </div>
            <div id="save_it"><div class="button_text">SAVE IT!</div></div>
        </div>

        <!-- The Pop Up -->
        <div id="myPop" class="pop">
          <!-- Pop Up content -->
          <div class="pop-content">
            <span class="close">&times;</span>
            <div id="poster">
              <img id="poster_img" src="https://image.tmdb.org/t/p/w185/kqjL17yufvn9OVLyXYpvtyrFfak.jpg" alt="Image Not Available">
            </div>
            <div id="movie_info">
              <div class="info_title">Title:</div>
              <div id="title" class="info">Filler Text</div>

              <div class="info_title">Tagline:</div>
              <div id="tagline" class="info">Filler Text</div>

              <div class="info_title">Overview:</div>
              <div id="overview" class="info">Filler Text</div>

              <div class="info_title">Actors:</div>
              <div id="actors" class="info">Filler Text</div>

              <div class="info_title">Length:</div>
              <div id="length" class="info">Filler Text</div>

              <div class="info_title">Release:</div>
              <div id="release" class="info">Filler Text</div>

              <div class="info_title">Genre:</div>
              <div id="genre" class="info">Filler Text</div>

              <div class="info_title">Rating:</div>
              <div id="rating" class="info">Filler Text</div>

              <div class="info_title">Website:</div>
              <a id="website" href="url" target="_blank">url</a>
            </div>
          </div>
        </div>

        <!-- Save Pop Up -->
        <div id="savePop" class="spop">
          <!-- Pop Up content -->
          <div class="spop-content">
            <span class="close">&times;</span>
            <div>Please Enter a Name for Your List:</div>
            <form id="movie_list_submit" method='post' action='create.py'>
                <input id="save_name" type="text" name="SaveName" placeholder="<My List Name>" maxlength="60" onfocus="this.placeholder = ''" onblur="this.placeholder = '<My List Name>'">
                <div id="final_save"><div class="button_text">SAVE LIST!</div></div>
                <input id="save_input" type="text" name="Movie_List" style='display: none'>
            </form>
          </div>
        </div>
    ''')
    print("</body></html>")



def main():
    if (len(sys.argv) == 1):
        getInput()
        return
    else:
        web()

if __name__ == "__main__":
    main()
