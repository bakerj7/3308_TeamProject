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

import create
import search


#Function to call create or search
def pickMode(mode): #mode is user input string selecting create or search
    call = False
    while call == False: #keep asking for input until correct input is found
        if (mode[0] == "c"):
            create.main()
            call = True #stop looping
        elif (mode[0] == "s"):
            search.main()
            call = True #stop looping
        else:
            #incorrect input, ask for new input
            mode = input('Unknown Input\nType "c" for create or "s" for search: ')

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
            <link rel="stylesheet" href="index_style.css" />
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            <script src="index.js" defer></script>
          </head>
          <body>
            <div style="position: fixed; z-index: -99; width: 100%; height: 100%">
              <iframe frameborder="0" height="100%" width="100%" opacity="0.6"
              src="https://youtube.com/embed/Y8D63cJGAr4?start=55&autoplay=1&controls=0&showinfo=0&autohide=1&mute=1&loop=1&playlist=Y8D63cJGAr4">
              </iframe>
            </div>
            <div id="bg_filter" style="position: fixed; z-index: -90; width: 100%; height: 100%">
            </div>

            <div id="banner">
              <div id="banner_logo">
                <embed id="logo" type="image/svg+xml" src="Logo.svg"/>
              </div>
              <div id="banner_title">
                <h1>MOVIE QUEUE</h1>
                <h2>What's Up Next!</h2>
              </div>
            </div>
            <div id="main">
              <div class="nav">
                <div id="nav_buttons">
                  <div class="page_button" id="create">
                    <p class="page_button_txt">CREATE</p>
                  </div>
                  <form id="create_nav" method='post' action='create.py'></form>
                  <div class="page_button" id="explore">
                    <p class="page_button_txt">EXPLORE</p>
                  </div>
                  <form id="explore_nav" method='post' action='search.py'></form>
                </div>
              </div>
            </div>
          </body>
        </html>
    ''')

#---------------------------------------------------
# command line used
# get user input

def getInput():
    print("Welcome to the world's greatest movie tool!")
    mode = input('Would you like to create a list ("c") or search for a pre-existing list ("s")? ')
    pickMode(mode)


#---------------------------------------------------
def main():
    if (len(sys.argv) == 1):
        getInput()
        return
    else:
        web()
        return



if __name__ == "__main__":
    main()
