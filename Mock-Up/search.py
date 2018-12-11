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
        <div id="result"></div>
        
        <script>
        // Check browser support
        if (typeof(Storage) !== "undefined") {
          // Retrieve
          document.getElementById("result").innerHTML = localStorage.getItem("'''+username+'''");
        } 
        else {
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
    username = input("What is your username? ")
    search(username, False)
    
#---------------------------------------------------
# web used
# print HTML
    
def web():
    print("Content-type:text/html\r\n\r\n")
    print("<html><body>")
    print("<h1 style='text-align:center;'>Search for a List</h1>")
    form = cgi.FieldStorage()
    if form.getvalue("Username"):
        username = form.getvalue("Username")
        search(username, True)
    print("<div style = 'border-left: 20px solid white; border-right: 70px solid white'>")
    print("<form method='post' action='search.py'>")
    print("USERNAME:<br>")
    print("<input type='text' name='Username' size='32' maxlength='40'><br>")
    print("<input type='submit' value='FIND IT!' />")
    print("</form>")
    print("</div>")
    print("</body></html>")

#---------------------------------------------------

def main():
    if (len(sys.argv) == 1):
        getInput()
        return
    else:
        web()
    
if __name__ == "__main__": 
    main()
