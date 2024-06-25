from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
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

