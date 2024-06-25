from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
  return {
    "FilmId" : "38",
    "TextFilm": "asdasdjhajkfhsiofbnasñkldfbaskjdfbañsifhajkñsdfkajñsdhfajksfh"
  }

