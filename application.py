'''
root module of the recommender app
'''

from flask import Flask, request, render_template
from recommender import recommend_nmf
from utils import movies

#where we define our Flask object to be used to render our views
app = Flask(__name__) # __name__ defines this script as the root of our movieapp

# decorator that routes the function to a specified URL
@app.route('/')
def landing_page():
    '''
    User lands on this page and enters query
    '''
    welcome_movies = movies.sample(n=7).to_dict('records')
    print(welcome_movies)
    return render_template('landing_page.html', welcome_movies=welcome_movies)

@app.route('/recommender/')
def recommender():
    '''
    queries accessed and transformed into recommendations
    '''
    print(request.args) # accesses the user query, prints in temrinal
    # example query for the .getlist method: ?q=star+wars&q=godfather&q=get+shorty
    print(request.args.getlist('q')) # accesses the user query as a list
    query = request.args.getlist('movie')
    query = [int(i) for i in query ]
    recs = recommend_nmf(query, k=10)

    movies_details = []

    for movieId in recs:
        movie = movies.set_index('movieId').loc[movieId]
        movie['movieId'] = movieId
        movies_details.append(movie)

    return render_template('recommender.html', movies_details=movies_details)

# parameterized URL
@app.route('/movie/<int:movieId>')
def movie_info(movieId):
    '''
    page for individual movie information
    '''
    movie=movies.set_index('movieId').loc[movieId]
    recs = recommend_nmf([movieId], k=10)
    print(recs)
    recommended_movies = []

    for rec_movie_id in recs:
        recommended_movie = movies.set_index('movieId').loc[rec_movie_id]
        recommended_movie['movieId'] = rec_movie_id
        recommended_movies.append(recommended_movie)
    # we also want to get similar movies based on this
    return render_template('movie_info.html', movie=movie, movieId=movieId, recommended_movies=recommended_movies) 


if __name__ == '__main__':
    # debug = True restarts servers after edits and prints verbose errors in terminal
    app.run(debug=True)
