from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def index():
  return {
    "Recommends" : {
      {
        "movie" : "1011985",
        "txt": "ESTE ES EL TEXTO DE KUNG FU PANDA"
      },
      {
        "movie" : "940551",
        "txt": "ESTE ES EL TEXTO DEL PUTO PÁJARO"
      }
      
    }
    
  }

