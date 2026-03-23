from fastapi import FastAPI

app = FastAPI()

@app.get("/morador/{id}")
def get_morador(id:int):
    return {
        "id": id,
        "Nome": "Fulano",
        "Telefone": "+55 11 40028922"
    }