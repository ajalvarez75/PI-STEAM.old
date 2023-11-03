from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()
# uvicorn main:app --reload

# carga de archivos
df_1_2_functions = pd.read_csv('Notebooks/Datasets/function_1_2.csv')
df_function_3_4_5 = pd.read_csv('Notebooks/Datasets/function_3_4_5.csv')

# Primera funcion.
@app.get("/PlayTimeGenre/{genre}")
def PlayTimeGenre(genre:str):
    genre = genre.lower()

    df_1_2_functions['playtime_forever'] = df_1_2_functions['playtime_forever'] / 60

    df_filtrado = df_1_2_functions[df_1_2_functions['genres'] == genre]

    grouped = df_filtrado.groupby(['release_year'])['playtime_forever'].sum().reset_index()

    max_played_year = grouped.loc[grouped['playtime_forever'].idxmax()]['release_year']

    result = {"Año de lanzamiento con más horas jugadas para Género " + genre: int(max_played_year)}

    return result

# Segunda funcion.
@app.get("/UserForGenre/{genre}")
def UserForGenre(genre:str):
    df_filter = df_1_2_functions[df_1_2_functions['genres'].str.lower() == genre.lower()]

    if df_filter.empty:
        return {"Mensaje": f"No se encontraron datos para el género {genre}"}

    # Agrupar por usuario y año
    grouped = df_filter.groupby(['user_id', 'release_year'])['playtime_forever'].sum().reset_index()
    grouped['playtime_forever'] = grouped['playtime_forever'] / 60  # Convertir minutos a horas

    # El usuario + horas jugadas por género
    max_user = grouped.groupby('user_id')['playtime_forever'].sum().idxmax()
    max_user_hours = grouped[grouped['user_id'] == max_user]

    # Obtener la lista de acumulación de horas jugadas por año
    hours_per_year = max_user_hours[['release_year', 'playtime_forever']]
    hours_list = [{"Año": int(year), "Horas": int(hours)} for year, hours in zip(hours_per_year['release_year'], hours_per_year['playtime_forever'])]

    result = {"Usuario con más horas jugadas para Género " + genre: max_user, "Horas jugadas": hours_list}
    return result

# Tercera funcion.
@app.get("/UsersRecommend/{year}")
def UsersRecommend(year:int):
    df_filter = df_function_3_4_5[df_function_3_4_5['release_year'] == year]

    if df_filter.empty:
        return {"Mensaje": f"No se encontraron juegos recomendados para el año {year}"}

    recommended_games = df_filter[df_filter['reviews_recommend'] == 2].groupby('title').size().reset_index()
    
    top_games = recommended_games.rename(columns={0: 'count'}).sort_values(by='count', ascending=False).head(3)

    top_3 = [{"Puesto " + str(i + 1): game} for i, game in enumerate(top_games['title'])]

    return top_3

# Cuarta funcion
@app.get("/UsersNotRecommend/{year}")
def UsersNotRecommend(year:int):
    df_filter = df_function_3_4_5[df_function_3_4_5['release_year'] == year]

    if df_filter.empty:
        return {"Mensaje": f"No se encontraron juegos recomendados para el año {year}"}

    not_recommended_games = df_filter[df_filter['reviews_recommend'] == 1].groupby('title').size().reset_index()

    top_games = not_recommended_games.rename(columns={0: 'count'}).sort_values(by='count', ascending=False).head(3)

    top_3 = [{"Puesto " + str(i + 1): game} for i, game in enumerate(top_games['title'])]

    return top_3

# Quinta funcion
@app.get("/sentiment_analysis/{year}")
def sentiment_analysis(year:int):
    df_filter = df_function_3_4_5[df_function_3_4_5['release_year'] == year]

    if df_filter.empty:
        return {"Mensaje": f"No se encontraron registros para el año {year}"}

    # Remapear los valores de análisis de sentimiento a etiquetas.
    df_filter.loc[:, 'sentiment_analysis'] = df_filter['sentiment_analysis'].map({0: "Negative", 1: "Neutral", 2: "Positive"})

    # Agrupar y cuenta los grupos.
    analysis_count = df_filter['sentiment_analysis'].value_counts().to_dict()

    # Diccionario con las categorías y recuento.
    result = {key: value for key, value in analysis_count.items()}

    return result
