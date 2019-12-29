import numpy as np
import pandas as pd
import scipy.spatial.distance as dist
import scipy.stats
import operator


def ContentBased(id_user):
    ratings = pd.read_csv('/Users/guilhermeviveiros/Desktop/ratings_small.csv', sep = ',');
    ratings = ratings.to_numpy();
    
    i = 0;
    movie_id = -1;
    list_movies = [];
    new_movies = [];
    for row in ratings:
        if(row[0] == id_user):        
            movie_id = int (row[1]);
            list_movies.append(movie_id);
    

    #caso em que o utilizador não tem ratings
    if(movie_id == -1):
        return None;

    
    else:
        movies = pd.read_csv('/Users/guilhermeviveiros/Desktop/movie_Data.csv', sep = ',');
        movies = movies.to_numpy()

        cluster = "";
        for movie in list_movies:

            for row in movies:
                if(row[0] == movie_id):
                    cluster = row[1];

                #caso em que o filme foi removido devido a datacleaning
            if(cluster == ""):
                break;
            
            else:
                for row in movies:
                    if(row[1] == cluster):
                        new_movies.append([row[2]]);
                        i = i+1;

                    if(i == 10): break;

    return new_movies;
    