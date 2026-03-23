from fastapi import FastAPI
import requests
import os
import random # Para gerar numeros aleatorios

app = FastAPI()

MORADOR_URL = os.getenv("MORADOR_URL")

@app.get("/apartamento/{id}")
def get_apartamento(id: int):
    try:
        response = requests.get(f"{MORADOR_URL}/morador/{id}", timeout=2)
        morador = response.json()
        num_ap = gerar_numero_ap()
        ap = {"numero": num_ap,
              "tamanho": "30m2"}
    except:
        morador = {"Error": "Serviço Indisponivel"}
        ap = None
    return {
        "id": id,
        "ap": ap,
        "morador": morador
    }

#Apenas para simular dado
def gerar_numero_ap():
    return random.randint(1,50)