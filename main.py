from fastapi import FastAPI  # Importo las librerias que utilizare
import pandas as pd
import uvicorn
import numpy as np
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()


play_genre = pd.read_csv('horas_jugadas_genero.csv', low_memory=False)



# Funcion def PlayTimeGenre

@app.get("/genero1/{genres}")
def PlayTimeGenre1(genres):
    df_filtered = play_genre[play_genre['genres'] == genres]

    if df_filtered.empty:
        return {"message": f"No se encontraron datos para el género {genres}"}

    max_playtime_index = df_filtered['playtime_forever'].idxmax()

    # Obtener el año y las horas jugadas
    max_playtime_year = df_filtered.loc[max_playtime_index, 'release_date']
    max_playtime_hours = df_filtered.loc[max_playtime_index, 'playtime_forever']

    return {
        f"Genero con más horas jugadas {genres}": {
            "Año": str(max_playtime_year),
            "Horas": max_playtime_hours
        }
    }

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True) #Corro la función



# Funcion def PlayTimeGenre

@app.get("/genero2/{genres}")
def PlayTimeGenre2(genres):
    df_filtered = play_genre[play_genre['genres'] == genres]

    if df_filtered.empty:
        return {"message": f"No se encontraron datos para el género {genres}"}

    max_playtime_index = df_filtered['playtime_forever'].idxmax()

    # Obtener el año y las horas jugadas
    max_playtime_year = df_filtered.loc[max_playtime_index, 'release_date']
    max_playtime_hours = df_filtered.loc[max_playtime_index, 'playtime_forever']

    return {
        f"Genero con más horas jugadas {genres}": {
            "Año": str(max_playtime_year),
            "Horas": max_playtime_hours
        }
    }

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True) #Corro la función