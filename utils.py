'''
import data here and have utility functions that could help
'''

import pandas as pd
import pickle

movies = pd.read_csv('../data/ml-latest-small/movies.csv')
#ratings = ...
with open('./nmf_comedy_recommender.pkl', 'rb') as file:
        model = pickle.load(file)

#print(movies.head(5))

def movie_title_search(fuzzy_title, movies):
    '''
    does a fuzzy search and returns best matched movie
    '''
    return title

def movie_to_id(title):
    '''
    converts movie title to id for use in algorithms
    '''
    return movieId

def id_to_movie(movieId):
    '''
    converts movie Id to title
    '''
    return title