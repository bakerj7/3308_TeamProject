#!/usr/bin/env python3
# enter the genre
# search through list
print("Welcome to the world's greatest movie tool!")
genre = input("What is your favorite genre? ")
for line in open('movieData.csv'):
    if genre in line:
        print(line)
