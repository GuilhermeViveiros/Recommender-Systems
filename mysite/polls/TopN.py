import pandas as pd
import numpy as np
from .models import Movie


def topN(N):
    #movies = pd.read_csv('dataset.csv',sep=",")
    
    for i in Movie.objects.all():
        print(i);

    q = Movie.objects.filter(name='avatar').get()
    #temos uma função que faz o orderby por mim já
    print(q)
    print(q.tipo)
    
    #movies = movies.to_numpy()
    #popularity = movies[:,6]
    #ind = np.argpartition(popularity, -N)[-N:]

    #movies = movies[:,[1]];
    #return movies[ind];
