from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def index():
  return {
    "id" : "38",
    "txt": "asdasdjhajkfhsiofbnasñkldfbaskjdfbañsifhajkñsdfkajñsdhfajksfh"
  }

