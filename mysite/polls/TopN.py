import pandas as pd
import numpy as np
import Levenshtein
import csv
#from .models import Movie


def topN(N):
    
    movies = pd.read_csv('/Users/guilhermeviveiros/Desktop/data_to_site.csv',sep=",")
    movies = movies.to_numpy()
    popularity = movies[:,6]
    ind = np.argpartition(popularity, -N)[-N:]

    movies = movies[:,[1]];
    
    return movies[ind];

def similarity_movies(input_user):

    movies = pd.read_csv('/Users/guilhermeviveiros/Desktop/data_to_site.csv',sep=",")
    movies = movies.to_numpy()
    list_movies = []
    for movie in movies:
        if(Levenshtein.distance(input_user,movie[1]) <= 2):
            list_movies.append([movie[1]]);

    return list_movies;

def info_movie(movie):
    movies = pd.read_csv('/Users/guilhermeviveiros/Desktop/data_to_site.csv',sep=",")
    movies = movies.to_numpy()
    for i in movies:
       if (i[12] ==  movie):
           #movie_name
           #ano
           #mes
           #lingua
           #temas
           #runtime
           return i[[12,2,3,8,10,13,15]];

def newUser():
    movies = pd.read_csv('/Users/guilhermeviveiros/Desktop/ratings_small.csv', sep = ',');
    movies = movies.to_numpy();
    user_id = int (np.amax(movies[:,0])+1);
    user_name = "user_" + str(user_id)
    
    return user_name, user_id;

def User_max():
    ratings = pd.read_csv('/Users/guilhermeviveiros/Desktop/ratings_small.csv', sep = ',');
    ratings = ratings.to_numpy();

    list = []

    for row in ratings:
        if (not row[0] in list): list.append(row[0]);

    return len(list)

def add_new_rate(user_id,rate,movie_name,time):
    movies = pd.read_csv('/Users/guilhermeviveiros/Desktop/data_to_site.csv', sep = ',');
    movies = movies.to_numpy()
    movie_id = -1;

    for row in movies:
        if (row[1] == movie_name):
            movie_id = row[0]    
            #break;
    
    if(movie_id != -1):
        fields=[user_id,movie_id,rate,time]
        with open('/Users/guilhermeviveiros/Desktop/ratings_small.csv','a') as fd:
            writer = csv.writer(fd)
            writer.writerow(fields)

def get_movie(movie_id):
    movies = pd.read_csv('/Users/guilhermeviveiros/Desktop/data_to_site.csv', sep = ',');
    movies = movies.to_numpy()

    for row in movies:
        if(row[0]==movie_id): return row[1];

def check_for_ratings_user_based(user_id):
    ratings = pd.read_csv('/Users/guilhermeviveiros/Desktop/ratings_small.csv', sep = ',');
    ratings = ratings.to_numpy();
    i = 0;

    for row in ratings:
        if(row[0] == user_id): i = i+1;
    
    return i;
