import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

import warnings; warnings.simplefilter('ignore')

md = pd.read_csv('./movies_metadata.csv')

md['genres']= md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

md['spoken_languages'] = md['spoken_languages'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

md['belongs_to_collection'] = md['belongs_to_collection'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

md['production_countries']= md['production_countries'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

with pd.ExcelWriter('./movies.xlsx') as writer:
    md.to_excel(writer)

