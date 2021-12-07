"""
contains various implementations for recommending movies
"""

import pandas as pd
from utils import movies, model
import numpy as np


def recommend_random(query, k=10):
    """
    Recommends a list of k random movie ids
    """
    return [1, 20, 34, 25]


def recommend_popular(query, k=10):
    """
    Recommend a list of k movie ids that are the most popular
    """
    return []


def recommend_nmf(query, k=10):
    """
    Filters and recommends the top k movies for any given input query based on a trained NMF model. 
    Returns a list of k movie ids.
    """
    
    
    
    # 1. candiate generation
    # construct a user vector
    user_vec = np.repeat(0, 193610)
    user_vec[query] = 5
    
   
    # 2. scoring
  
    # calculate the score with the NMF model
    scores = model.inverse_transform(model.transform([user_vec]))
    scores = pd.Series(scores[0])
    
    
    # 3. ranking
    
    # set zero score to movies allready seen by the user
    scores[query] = 0
    
    # return the top-k highst rated movie ids or titles
    scores = scores.sort_values(ascending=False)
    recommendations = scores.head(10).index
    
    return recommendations


def recommend_neighbors(query, k=10):
    """
    Recommend a list of k movie ids based on the most similar users
    """
    return []



# list of liked movies
query = [1, 34, 56, 21]
print(recommend_random(query))
