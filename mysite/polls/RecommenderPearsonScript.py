import numpy as np
import pandas as pd
import scipy.spatial.distance as dist
import scipy.stats
import operator
from sklearn.model_selection import train_test_split
#utilizo kNN, k-nearest-neighbor para ter os utilizadores mais
#similares aos utilizadores que queremos prever
from sklearn import neighbors
from sklearn.metrics import mean_squared_error 
#i use root mean square as loss function
from scipy.stats import pearsonr
#i also use Pearson coefficient
from math import sqrt 
import matplotlib.pyplot as plt

ratings = pd.read_csv("/Users/guilhermeviveiros/Desktop/ratings_small.csv", sep=',')
ratings = ratings.to_numpy()

# temos 15 utilizadores aqui, não sei porque
# vou separar cada utilizador com os seus ratings


def ratings_of_users(ratings, user_max):

    ratings_users = {}

    for i in range(1, user_max+1):
        tmp = []
        ratings_users["user_"+str(i)] = []

    for row in ratings:
        id = np.int(row[0])
        ratings_users["user_"+str(id)].append((row[2], row[1]))

    return ratings_users


def best_matches(ratings, user):

    specific_ratings_user = ratings[user]

    ratings.__delitem__(user)

    # todos os filmes referentes ao user a prever
    x = len(specific_ratings_user)
    movies_user = np.empty((1, x), np.int)
    i = 0
    for tuplo in specific_ratings_user:
        movies_user[0][i] = tuplo[1]
        i = i+1

    # agora preciso de todos os movies e ratings dos outros utilizadores
    # que avaliaram os mesmos movies que o user especifico
    ratings_users = {}

    for i in ratings:
        tmp = []
        ratings_users[i] = []

    for row in ratings:

        for tuplo in ratings[row]:
            movie = tuplo[1]

            if (movie in movies_user[0]):
                ratings_users[row].append((tuplo[0], tuplo[1]))

    return specific_ratings_user, ratings_users

# dá uma lista com as similaridades entre utilizadores
# vou ao utilizador que quero prever e para cada outro utilizador
# encontro filmes que ambos avaliaram e calculo a similaridade


def similaridade(user, group_of_users):

    # users
    ratings_similar = {}
    similarity_user = []
    similarity_between_users = []

    # specific user
    ratings_similar["user"] = []
    movies_user = []

    # para cada utilizador
    for x in group_of_users:

        # percorremos os filmes
        for tuplo in group_of_users[x]:
            # só quero os filmes que o user1 avaliou	semelhantes ao user2
            for movie in user:
                if(movie[1] == tuplo[1]):
                    ratings_similar["user"].append(movie[0])

        #print("user to predict = " + str(ratings_similar["user"]))
        #print("user to compare = " + str(group_of_users[x]));
        tmp = []
        for i in group_of_users[x]:
            tmp.append(i[0])

        group_of_users[x] = tmp

        #print("user to predict = " + str(ratings_similar["user"]))
        #print("user to compare = " + str(group_of_users[x]));

        # calcular a similaridade com a euclidian distance
        if(ratings_similar["user"] != [] and group_of_users[x] != []):
            tmp1 = ratings_similar["user"]
            tmp2 = group_of_users[x]
            if(len(tmp1) > 1 and len(tmp2) > 2):
                tmp = scipy.stats.pearsonr(tmp1, tmp2)
                similarity_between_users.append(tmp)
                similarity_user.append(x)

        ratings_similar["user"] = []
       
    return np.asarray(similarity_between_users[0]), np.asarray(similarity_user)


def TopN(similarity_between_users, N):
    i = 0

    while(N > similarity_between_users.shape[0]):
        N = N-2

    #ratings = np.dot(similarity_between_users,-1)

    ind = np.argpartition(similarity_between_users, -N)[-N:]
    return ind


def search_unranked_films(user_to_predict, topN_users, ratings_users, ratings_user_to_predict):

    list = []
    movie_list = {}
    users = {}
    for user in topN_users:
        users[user] = ratings_users[user]

    x = np.asarray(users)

    for user in users:
        for movie in users[user]:
            # verificar se o user1 não viu
            # o list serve para não estar a repetir
            if(not movie[1] in list):
                tmp = 0
                for i in ratings_user_to_predict:
                    if(i[1] == movie[1]):
                        tmp = 1

                # se chegar aqui e tmp = 0, user não viu/avaliou este filme, posso continuar com este filme
                if(tmp == 0):
                    list.append(movie[1])
                how_many = 1  # esta variável permite me identificar quantos utilizadores viram este filme
                for u in users:
                    if(not u == user):
                        for m in users[u]:
                            if(m[1] == movie[1]):
                                how_many = how_many + 1
                movie_list[movie[1]] = how_many

    return movie_list


def predict_movies(user_rating, similarity_users, ratings_user, movies,similarity):
    # media de avaliação do user a prever -> ratings_specific_user
    # similaridades entre users ->similarity_be..
    # avaliações individuais -> ratings_users
    # media das avaliacoes -> rratings_user
    # similaridade entre users -> similarity_be
    predict_movie_rating = {}
    user_rating = np.asarray(user_rating)
    ra = np.mean(user_rating[:, 0])
    #print(ra)

    numerador = []
    denominador = []

    # denominador
    for i in similarity_users:
        denominador.append(i[1])

    denominador = np.mean(denominador)

    # numerador
    for movie in movies:
        numbers_of_users_that_rate = movies[movie]

        for i in similarity:

            sim_a_b = i[1]  # similaridade entre 0 e 1
            b = i[0]  # nome do utilizador
            b = ratings_user[b]
            b = np.asarray(b)
            rb = np.mean(b[:, 0])

            # rb_p rating do user x ao filme p
            for i in b:
                if(i[1] == movie):
                    rb_p = i[0]

            tmp = sim_a_b * (rb_p - rb)
            numerador.append(tmp)

        # calculo do numerador
        numerador = np.mean(numerador)
        tmp = ra + (numerador / denominador)
        numerador = []

        predict_movie_rating[movie] = tmp


    return predict_movie_rating


# vão todas de 0 a 5, porque estou a usar Pearson Correlation
def top_by_ratings(predict_movie_rating):
    rat = 0
    movie = 0
    for i in predict_movie_rating:
        if(predict_movie_rating[i] > rat):
            rat = predict_movie_rating[i]
            movie = i

    return movie, rat


def user_based(max_users, user_to_predict):

    # ratings dos utilizadores
    ratings_users = ratings_of_users(ratings, max_users)

    # ratings de um utilizador e dos utilizadores que avalariam filmes semelhantes
    ratings_specific_user, ratings_users2 = best_matches(
        ratings_users, user_to_predict)

    # similaridade entre um utilizador e os calculados em cima
    similarity_between_users, similarity = similaridade(
        ratings_specific_user, ratings_users2)

    # verifica qual os melhores utilizadores(similaridade mais forte)
    indx = TopN(similarity_between_users, 2)
    topN_users = similarity[indx]

    # verifica quais os filmes que os utilizadores mais similares avaliaram, em que o 1 ainda não viu/avaliou
    movie_list = search_unranked_films(
        user_to_predict, topN_users, ratings_users, ratings_specific_user)

    # similaridade entre users e user em lista
    similarity = []
    for i in range(0, len(topN_users)):
        similarity.append((topN_users[i], similarity_between_users[i]))

    # faz o predict da avaliação que o utilizar deverá dar a estes filmes com base em tudo calculado anteriormente
    predict_movie_rating = predict_movies(
        ratings_specific_user, similarity, ratings_users, movie_list,similarity)

    movie, rat = top_by_ratings(predict_movie_rating)
   
    return movie, rat


def KNN(to_predict):

    ratings = pd.read_csv('/Users/guilhermeviveiros/Desktop/ratings_small.csv', sep = ',');
    ratings = ratings.to_numpy()
    
    #removo o que quero prever do x_train
    x_train = ratings[:,[0,1,3]]
    y_train = ratings[:,[2]];

   
    model = neighbors.KNeighborsRegressor(n_neighbors = 12)

    model.fit(x_train, y_train)  #fit the model
    pred=model.predict(to_predict) #make prediction on test set


    return pred


#hybrid system recebe um dados, utilizdor id movie id e timestamp e preve o rating que o utilizador iria dar através de vários métodos
#Faz a média no fim
#def hybrid_system(to_predict):
    #usa as 3
    #cluster
    #RecommenderPearson
    #KNN