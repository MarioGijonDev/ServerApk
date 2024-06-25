from fastapi import FastAPI

import requests

API_URL = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
API_KEY = "29558a4bd1bceae95502ae68301038eb"

listOfAllMovies = []

app = FastAPI()
page = 1
def getMoviesFromTmdbApi():
  headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyOTU1OGE0YmQxYmNlYWU5NTUwMmFlNjgzMDEwMzhlYiIsIm5iZiI6MTcxOTMyODAxMi43NTk2OTYsInN1YiI6IjY2MjFhZTRjYmIxMDU3MDE4OWQyNGY4MiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.B-Ad3TSiycU0-qSZsE8w4p9x2dpWZ0BP9WZaf5y0Xfw",
    "with_genres": "10751",
    "language": "en-US",
    "page": str(page)
  }

  response = requests.get(API_URL, headers=headers)

  if response.status_code == 200:
    if page < 190:
      listOfAllMovies.append(response.json())
      page = page+1
      return getMoviesFromTmdbApi()
    else:
      return true
  else:
    return false
    print("Imposible conectar con el servidor")

if getMoviesFromTmdbApi():
  print("FIN")
  print(listOfAllMovies)
else:
  print("Error")
  

""" @app.get("/test")
def index():
    return {
        "Recommends": [
            {
                "id": "1011985",
                "txt": "Este es el texto de la pelicula Kung fu Panda con el id 1011985 describiendo la razón de la recomendación"
            },
            {
                "id": "940551",
                "txt": "Este es el texto de la pelicula Migration con el id 940551 describiendo la razón de la recomendación"
            }
        ]
    }

 """