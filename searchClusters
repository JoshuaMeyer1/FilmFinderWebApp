from scipy.spatial.distance import euclidean
import pandas as pd
import sys
import warnings


#returns full cols of movies, movie is a string title, df pickle
def find_similar_movies_by_genre(movie, df, k=10):
    movie_cluster = df.loc[df['title'] == movie, 'genre_cluster'].iloc[0]
    combined_genres_input = df.loc[df['title'] == movie, 'combined_genres'].iloc[0]
    clustered_movies = df[df['genre_cluster'] == movie_cluster]
    clustered_movies['distance'] = clustered_movies['combined_genres'].apply(
        lambda x: euclidean(combined_genres_input, x)
    )
    similar_movies = clustered_movies.nsmallest(k, 'distance')
    return similar_movies[['title', 'distance']]


def find_similar_movies_by_summary(movie, df, k=10):
    movie_cluster = df.loc[df['title'] == movie, 'overview_cluster'].iloc[0]
    combined_summary_input = df.loc[df['title'] == movie, 'embedded_overview'].iloc[0]
    cluster_movies = df[df['overview_cluster'] == movie_cluster]
    cluster_movies['distance'] = cluster_movies['embedded_overview'].apply(
        lambda x: euclidean(combined_summary_input, x)
    )
    similar_movies = cluster_movies.nsmallest(k, 'distance')
    return similar_movies[['title', "distance"]]


def find_similar_movies_by_keywords(movie, df, k=10):
    movie_cluster = df.loc[df['title'] == movie, 'keyword_cluster'].iloc[0]
    combined_keyword_input = df.loc[df['title'] == movie, 'combined_keywords'].iloc[0]
    cluster_movies = df[df['keyword_cluster'] == movie_cluster]
    cluster_movies['distance'] = cluster_movies['combined_keywords'].apply(
        lambda x: euclidean(combined_keyword_input, x)
    )
    similar_movies = cluster_movies.nsmallest(k, 'distance')
    return similar_movies[['title', 'distance']]

'''
def main():
    warnings.filterwarnings("ignore")
    file_name = "movie_pickle.pkl"
    df = pd.read_pickle(file_name)



if __name__ == "__main__":
    main()
'''