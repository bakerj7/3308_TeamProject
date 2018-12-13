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

import index



# locate file on computer
def findFile(username):
    fileName = "./Lists/"+username+".txt" #form file name from user name
    if os.path.exists(fileName):
        return fileName
    else:
        return ""

#---------------------------------------------------
#Function to search for pre-made list
def search(username, webBool):
    if webBool == False: #search computer is command line used
        fileName = findFile(username) #check if file exists
        if username in fileName:
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
                    index.pickMode(mode) #function to call create or search based on user input
                    y_n = True
                else:
                    #incorrect input, ask for new input
                    view = input('Unknown Input/nType "y" for yes or "n" for n: ')
        else: #list not found
            print("Sorry, list not found")
            mode = input('Would you like to create a list ("c") or search for another list ("s")? ')
            index.pickMode(mode) #function to call create or search based on user input
    else: # search local storage if web used
        print('''
        <div id="store"></div>

        <script>
        // Check browser support
        if (typeof(Storage) !== "undefined") {
          // Retrieve
          document.getElementById("store").innerHTML = localStorage.getItem("'''+username+'''");
        }
        else {
          document.getElementById("store").innerHTML = "Sorry, your browser does not support Web Storage...";
        }
        </script>

        </body>
        </html>
        ''')


#---------------------------------------------------
# command line used
# get user input

def getInput():
    username = input("What is your username? ")
    search(username, False)


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
                <link rel="stylesheet" href="explore_style.css" />
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                <script src="movie_explore.js" defer></script>
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
                    <div id="search_title">SEARCH:</div>
                    <div class="search_group">
                      <div class="search_title">LIST NAME:</div>
                      <input id="list_name_input" type="text" name="Title" placeholder="<Enter List Name>" maxlength="60" onfocus="this.placeholder = ''" onblur="this.placeholder = '<Enter List Name>'">
                    </div>
                    <div id="find_it"><div class="button_text">FIND IT!</div></div>
                    <div id="get_lucky"><div class="button_text">GET LUCKY!</div></div>
                </div>


                <div id="saved_lists_box">
                    <div id="lists_title">SAVED LISTS:</div>
                    <div id="lists_table">
    ''')

                        #<div class="list">Dark Comedies</div>
                        #<div class="list">Leonardo DiCaprio</div>
                        #<div class="list">Feel Good Flix</div>
                        #<div class="list">Thrillers with Strong Female Lead</div>
                        #<div class="list">Beach Weekend</div>
                        #<div class="list">Family Friendly</div>
                        #<div class="list">Marvel and DC Universe</div>
                        #<div class="list">Indie Comedies</div>
                        #<div class="list">Realistic Horror Films</div>
                        #<div class="list">Chill Movies</div>
                        #<div class="list">Highschool Football</div>
                        #<div class="list">Throw-backs</div>
                        #<div class="list">John Doe's Favorites</div>
                        #<div class="list">Mary's Awesome List</div>
    print('''
                    </div>
                </div>

                <!-- The Pop Up -->
                <div id="myListPop" class="pop">
                  <!-- Pop Up content -->
                  <div class="pop-content">
                    <span class="close">&times;</span>
                    <div id="list_box">
                      <div id="list_title">NONE:</div>
                      <div id="list_table">
                          <div id="424694" class="result">The Matrix</div>
                          <div id="424694" class="result">Clueless</div>
                          <div id="424694" class="result">The Wizard of Oz</div>
                          <div id="424694" class="result">The Godfather</div>
                          <div id="424694" class="result">Black Panther</div>
                          <div id="424694" class="result">The Shining</div>
                          <div id="424694" class="result">Casablanca</div>
                          <div id="424694" class="result">Lady Bird</div>
                          <div id="424694" class="result">The Dark Night</div>
                          <div id="424694" class="result">Robin Hood</div>
                          <div id="424694" class="result">Star Wars</div>
                          <div id="424694" class="result">Fantastic Beasts</div>
                          <div id="424694" class="result">The Avengers</div>
                          <div id="424694" class="result">A Star Was Born</div>
                      </div>
                    </div>
                  </div>
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

            </body>
        </html>
    ''')

    #form = cgi.FieldStorage()
    #if form.getvalue("Username"):
        #username = form.getvalue("Username")
        #search(username, True)

#---------------------------------------------------

def main():
    if (len(sys.argv) == 1):
        getInput()
        return
    else:
        web()

if __name__ == "__main__":
    main()
