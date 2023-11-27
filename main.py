from fastapi import FastAPI  # Importo las librerias que utilizare
import pandas as pd
import uvicorn
from sklearn.metrics.pairwise import cosine_similarity

app = FastAPI()

# Lectura de todos los CSV
play_genre = pd.read_csv('PlayTimeGenre.csv', low_memory=False)
user_genre= pd.read_csv('UserForGenre.csv', low_memory=False)
user_recommend= pd.read_csv('UsersRecommend.csv', low_memory=False)
juegos_no_recom= pd.read_csv('UsersWorstDeveloper.csv', low_memory=False)
df_sentimiento_analisis= pd.read_csv('sentiment_analysis.csv', low_memory=False)
render_model= pd.read_csv('Model_render.csv',low_memory=False)


# Funcion def PlayTimeGenre

@app.get("/PlayTimeGenre/{genres}")
def PlayTimeGenre(genres):
    df_filtered = play_genre[play_genre['genres'] == genres]

    if df_filtered.empty:
        return {"message": f"No se encontraron datos para el género {genres}"}

    max_playtime_index = df_filtered['playtime_forever'].idxmax()

    # Obtener el año y las horas jugadas
    max_playtime_year = df_filtered.loc[max_playtime_index, 'release_date']
    max_playtime_hours = df_filtered.loc[max_playtime_index, 'playtime_forever']
    max_playtime_year_only = max_playtime_year.dt.year

    return {
        f"Genero con más horas jugadas {genres}": {
            "Año": max_playtime_year_only,
            "Horas": max_playtime_hours
        }
    }

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True) 
    
    
# Funcion def UserForGenre

@app.get("/UserForGenre/{genres}")

def UserForGenre(genres: str):
    '''Función que devuelve al usuario con más horas jugadas por genero y año'''

    df_filtered = user_genre[user_genre['genres'] == genres]

    df_filtered = df_filtered[df_filtered['release_date'].str.match(r'\d{4}-\d{2}-\d{2}', na=False)]

    df_filtered['release_date'] = pd.to_datetime(df_filtered['release_date'], format='%Y-%m-%d')
    
    user_year_playtime = df_filtered.groupby(['user_id', df_filtered['release_date'].dt.year])['playtime_forever'].sum().reset_index()

    max_user = user_year_playtime.groupby('user_id')['playtime_forever'].sum().idxmax()

    df_max_user = user_year_playtime[user_year_playtime['user_id'] == max_user]

    max_user_year_playtime = df_max_user.groupby('release_date')['playtime_forever'].sum()

    max_user_year_playtime_list = [{"Año": year, "Horas": hours} for year, hours in zip(max_user_year_playtime.index, max_user_year_playtime)]

    return {
        f"Usuario con más horas jugadas para {genres}": max_user,
        "Horas jugadas": max_user_year_playtime_list
    }

# Funcion def UsersRecommend

@app.get("/UsersRecommend")

def UsersRecommend(year: int):
    '''Devuelve los 3 juegos más recomendados por usuarios 
        para el año dado por un usuario específico.'''

    filtered_reviews = user_recommend[(user_recommend['release_date'].str.contains(str(year), regex=False, na=False)) & (user_recommend['recommend'] == True)]

    top_games = (
        filtered_reviews['title']
        .value_counts()
        .head(3)
        .reset_index()
        .rename(columns={'index': 'title', 'title': 'count'})
    )

    top_3_games_list = [{f"Puesto {i+1}: {game}": count} for i, (game, count) in top_games.iterrows()]

    return top_3_games_list

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
    
    
# Funcion def juegosNoRecomendados

@app.get("/UsersWorstDeveloper")

def UsersWorstDeveloper(year: int):
    '''Devuelve los juegos Menos recomendados por usuarios para el año dado.'''

    filtered_reviews = juegos_no_recom[(juegos_no_recom['release_date'].str.contains(str(year), regex=False, na=False)) & (juegos_no_recom['recommend'] == False)]

    less_rated_games = (
        filtered_reviews['title']
        .value_counts()
        .head(3)
        .reset_index()
        .rename(columns={'index': 'title', 'title': 'count'})
    )

    less_3_games_list = [{f"Puesto {i+1}: {game}": count} for i, (game, count) in less_rated_games.iterrows()]

    return less_3_games_list


if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
    
    
# Función de Sentimiento   

@app.get("/SentimentAnalysis")

def sentiment_analysis(desarrolladora: str) -> dict:
    df = df_sentimiento_analisis
    
    # Filtra las filas que corresponden a la empresa desarrolladora
    df_filtrado = df[df['developer'] == desarrolladora]
    
    # Cuenta la cantidad de registros de cada categoría de análisis de sentimiento
    cantidad_negativos = df_filtrado[df_filtrado['sentiment_analysis'] < 0].shape[0]
    cantidad_neutrales = df_filtrado[df_filtrado['sentiment_analysis'] == 0].shape[0]
    cantidad_positivos = df_filtrado[df_filtrado['sentiment_analysis'] > 0].shape[0]
    
    # Crea el diccionario de salida
    salida = {desarrolladora: {'Negative': cantidad_negativos, 'Neutral': cantidad_neutrales, 'Positive': cantidad_positivos}}
    
    return salida


if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
    


#user items 


@app.get("/JuegoML/{user_id}")

def recomendacion_usuario(user_id: str):
    # Encuentra con el user_id los juegos recomendados
    if user_id in render_model['user_id'].values:
        juegos = render_model.index[render_model['user_id'] == user_id].tolist()[0]
        
        juego_caracteristicas = render_model.iloc[juegos, 3:].values.reshape(1, -1)
        
        render_similitud = cosine_similarity(render_model.iloc[:, 3:], juego_caracteristicas)
        juegos_similaresrecomend = render_similitud.argsort(axis=0)[::-1][1:6]
        juegos_similaresrecomend = juegos_similaresrecomend.flatten()[1:]
        juegos_similares = render_model.iloc[juegos_similaresrecomend]['app_name']
        
        return juegos_similares  
    else:
        return "El juego con el user_id especificado no existe en la base de datos."
    


# Ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)