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

    print("\nMovies featuring " + actor +":\n")
    if webBool == True:
                print("<br>")
    for entry in actor_data['results']:
        for movie in entry['known_for']:
            print(movie['title'])
            if webBool == True:
                print("<br>")
            movieList.append(movie['title'])

    if webBool == True:
                print("<br>")
    movie_data = json.load(movie_response)
    print("\n" + genre + " movies:\n")
    if webBool == True:
                print("<br>")
    for entry in movie_data['results']:
        print(entry['title'])
        if webBool == True:
                print("<br>")
        movieList.append(entry['title'])

    #Output user results to txt file
    print("\n")
    print("***Currently exporting results***")
    if webBool == True:
                print("<br>")

    #output_file = open(username + '.txt', 'w')
    createFolder('./Lists/')
    output_file = open('./Lists/' + username + '.txt', 'w')
    output_file.write("List Name: " + username + '\n')
    output_file.write("Genres: " + genre + '\n')
    output_file.write("Actors: " + actor + '\n')
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
        <div id="result"></div>

        <script>
        // Check browser support
        if (typeof(Storage) !== "undefined") {
          // Store
          localStorage.setItem("'''+username+'''", "'''+movies+'''");
          // Retrieve
          document.getElementById("result").innerHTML = localStorage.getItem("'''+username+'''");
        } else {
          document.getElementById("result").innerHTML = "Sorry, your browser does not support Web Storage...";
        }
        </script>

        </body>
        </html>
        ''')

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
    print("Content-type:text/html\r\n\r\n")
    print("<html><body>")
    print("<h1 style='text-align:center;'>Create a List</h1>")
    form = cgi.FieldStorage()
    if form.getvalue("Username") and form.getvalue("Genre") and form.getvalue("Actor/Actress"):
        username = form.getvalue("Username")
        genre = form.getvalue("Genre")
        actor = form.getvalue("Actor/Actress")
        createList(username, genre, actor, True)
    print("<div style = 'border-left: 20px solid white; border-right: 70px solid white'>")
    print("<form method='post' action='create.py'>")
    print("USERNAME:<br>")
    print("<input type='text' name='Username' size='32' maxlength='40'><br>")
    print("GENRE:<br>")
    print("<input type='text' name='Genre' size='32' maxlength='40'><br>")
    print("ACTOR/ACTRESS:<br>")
    print("<input type='text' name='Actor/Actress' size='32' maxlength='40'><br> <br>")
    print("<input type='submit' value='FIND IT!' />")
    print("</form>")
    print("</div>")
    print("</body></html>")


def main():
    if (len(sys.argv) == 1):
        getInput()
        return
    else:
        web()

if __name__ == "__main__":
    main()
