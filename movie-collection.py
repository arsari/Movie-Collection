#!/usr/local/bin/python3
# this script is not compatible with python2


# encoding definition
"""coding=utf-8"""


# import modules
import os
import platform


# function definition to determine os system to clear screen
def clear_screen():
    my_os = platform.system()
    if my_os == 'Windows':
        os.system('cls')  # on windows
    else:
        os.system('clear')  # on linux / os x


# Build a dictionary containing the specified movie collection
movie_collection = {
    '2005': ['Munich', 'Steven Spielberg'],
    '2006': [['The Prestige', 'Christopher Nolan'],
             ['The Departed', 'Martin Scorsese']],
    '2008': ['The Dark Knight', 'Christopher Nolan'],
    '2009': ['Mary and Max', 'Adam Elliot'],
    '2010': ['The King\'s Speech', 'Tom Hooper'],
    '2007': ['Into the Wild', 'Sean Penn'],
    '2011': [['The Artist', 'Michel Hazanavicius'],
             ['The Help', 'Tate Taylor']],
    '2012': ['Argo', 'Ben Affleck'],
    '2013': ['12 Years a Slave', 'Steve McQueen'],
    '2014': ['Birdman', 'Alejandro G. Inarritu'],
    '2015': ['Spotlight', 'Tom McCarthy'],
    '2016': ['The BFG', 'Steven Spielberg']
}

# Prompt the user for a year
clear_screen()
year = input('Enter a year between 2005 and 2016:\n')

# Displaying the title(s) and directors(s) from that year
if year not in movie_collection:
    print('N/A\n')
else:
    if type(movie_collection[year][0]) is list:
        for year in movie_collection[year]:
            print('%s, %s' % (year[0], year[1]))
    else:
        print('%s, %s' % (movie_collection[year][0], movie_collection[year][1]))
    print()

# Display menu
menu_option = ''
while menu_option != 'q':
    print('MENU')
    print('Sort by:')
    print('y - Year')
    print('d - Director')
    print('t - Movie title')
    print('q - Quit')
    menu_option = input('\nChoose an option:\n').lower()

    # Carry out the desired option: Display movies by year,
    if menu_option == 'y':
        clear_screen()  # call to clear screen function
        list_year = sorted(movie_collection.keys())
        for year in list_year:
            print('%s:' % year)
            if type(movie_collection[year][0]) is list:
                for year in movie_collection[year]:
                    print('\t%s, %s' % (year[0], year[1]))
                print()
            else:
                print('\t%s, %s' % (movie_collection[year][0], movie_collection[year][1]))
                print()
        continue
    # display movies by director, display movies by movie title, or quit
    elif menu_option == 'd':
        clear_screen()
        list_directors = []
        for value in movie_collection.values():
            if type(value[0]) is list:
                for director in value:
                    if director[1] not in list_directors:
                        list_directors.append(director[1])
            else:
                if value[1] not in list_directors:
                    list_directors.append(value[1])
        sort_directors = sorted(list_directors)

        for director in sort_directors:
            print('%s:' % (director))
            years = sorted(movie_collection.keys())
            for year in years:
                if type(movie_collection[year][0]) is list:
                    for d in movie_collection[year]:
                        if d[1] == director:
                            print('\t%s, %s' % (d[0], year))
                else:
                    if movie_collection[year][1] == director:
                        print('\t%s, %s' % (movie_collection[year][0], year))
            print()
        continue
    # display movies by movie title, or quit
    elif menu_option == 't':
        clear_screen()
        list_movies = []
        for value in movie_collection.values():
            if type(value[0]) is list:
                for movie in value:
                    if movie[0] not in list_movies:
                        list_movies.append(movie[0])
            else:
                if value[0] not in list_movies:
                    list_movies.append(value[0])
        sort_movies = sorted(list_movies)

        for movie in sort_movies:
            print('%s:' % (movie))
            years = sorted(movie_collection.keys())
            for year in years:
                if type(movie_collection[year][0]) is list:
                    for m in movie_collection[year]:
                        if m[0] == movie:
                            print('\t%s, %s' % (m[1], year))
                else:
                    if movie_collection[year][0] == movie:
                        print('\t%s, %s' % (movie_collection[year][1], year))
            print()
        continue
    # quit
    elif menu_option == 'q':
        break
    else:
        print('Invalid menu option.')
        print()
        continue
