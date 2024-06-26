
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import logging
import requests
import pandas as pd

page = 1
listOfAllMovies = []
listOfKeywords = []
listOfReviews = []
dataset = []

def getMoviesFromTmdbApi():
    global page
    global listOfAllMovies
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyOTU1OGE0YmQxYmNlYWU5NTUwMmFlNjgzMDEwMzhlYiIsIm5iZiI6MTcxOTQzMDQxNS42NDc5NTIsInN1YiI6IjY2MjFhZTRjYmIxMDU3MDE4OWQyNGY4MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NlNxso6YVdLFXXOZXZK9ZzEDXYuDD2HUuTz0P67eKXY",
    }
    response = requests.get(f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}", headers=headers)
    if response.status_code == 200:
        if page < 2:
            listOfAllMovies.extend(response.json()['results'])
            print(f"Page {page} success")
            page += 1
            return getMoviesFromTmdbApi()
        else:
            return True
    else:
        print("Rejected connection")
        return False

def getKeywordsById(movieId):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyOTU1OGE0YmQxYmNlYWU5NTUwMmFlNjgzMDEwMzhlYiIsIm5iZiI6MTcxOTQzMDQxNS42NDc5NTIsInN1YiI6IjY2MjFhZTRjYmIxMDU3MDE4OWQyNGY4MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NlNxso6YVdLFXXOZXZK9ZzEDXYuDD2HUuTz0P67eKXY"
    }
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movieId}/keywords", headers=headers)
    if response.status_code == 200:
        listOfKeywords.append(response.json())
        print(f"Keyword from {movieId} success")
        return True
    else:
        print(f"Rejected connection for keywords -> {response.text}")
        return False

def getReviewsById(movieId):
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyOTU1OGE0YmQxYmNlYWU5NTUwMmFlNjgzMDEwMzhlYiIsIm5iZiI6MTcxOTQzMDQxNS42NDc5NTIsInN1YiI6IjY2MjFhZTRjYmIxMDU3MDE4OWQyNGY4MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.NlNxso6YVdLFXXOZXZK9ZzEDXYuDD2HUuTz0P67eKXY"
    }
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movieId}/reviews", headers=headers)
    if response.status_code == 200:
        listOfReviews.append(response.json())
        print(f"Reviews from {movieId} success")
        return True
    else:
        print(f"Rejected connection for reviews -> {response.text}")
        return False

getMoviesFromTmdbApi()

for movie in listOfAllMovies:
    getKeywordsById(movie['id'])
    getReviewsById(movie['id'])

for movie in listOfAllMovies:
    movie_id = movie['id']
    keywords = next((item['keywords'] for item in listOfKeywords if item['id'] == movie_id), [])
    reviews = next((item['results'] for item in listOfReviews if item['id'] == movie_id), [])
    
    movie_data = {
        'id': movie_id,
        'title': movie['title'],
        'overview': movie['overview'],
        'release_date': movie['release_date'],
        'genres': movie['genre_ids'],
        'vote_average': movie['vote_average'],
        'vote_count': movie['vote_count'],
        'keywords': [keyword['name'] for keyword in keywords],
        'reviews': [{'author': review['author'], 'content': review['content'], 'rating': review['author_details'].get('rating')} for review in reviews]
    }
    
    dataset.append(movie_data)


df = pd.DataFrame(dataset)

df.to_csv('movies_dataset.csv', index=False)
