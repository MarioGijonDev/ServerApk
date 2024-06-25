from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
  return {
    "id" : "38",
    "txt": "asdasdjhajkfhsiofbnasñkldfbaskjdfbañsifhajkñsdfkajñsdhfajksfh"
  }

