from fastapi import FastAPI
import pandas as pd
import pyarrow
import json
from typing import List, Dict, Union, Any
user_games_final = pd.read_parquet("user_games_final.parquet")
user_items_final = pd.read_parquet('user_items_final.parquet')
user_reviews_final = pd.read_parquet('user_reviews_final.parquet')
    
app = FastAPI()

@app.get("/playtime/{genre}")
def PlayTimeGenre(genre: str):

    # Fusionar los DataFrames en el "ID del elemento"
    merged_data = pd.merge(user_games_final, user_items_final, left_on='Item ID', right_on='Item ID')

    # Filtrar los datos por el género proporcionado
    genre_data = merged_data[merged_data['Genres'] == genre]

    # Agrupar por año de lanzamiento y calcular el tiempo total de juego para cada año
    year_playtime = genre_data.groupby('Release Date')['Play Time Forever'].sum() / 60

    # Encontrar el año con más tiempo de juego
    max_year = year_playtime.idxmax()

    # Crear el diccionario de retorno
    result = {f"Año de lanzamiento con más horas jugadas para {genre}": max_year}

    return result

@app.get("/user_for_genre/{genre}")
def UserForGenre(genre: str):

    # Fusionar los DataFrames en el "ID del elemento"
    merged_data = pd.merge(user_games_final, user_items_final, left_on='Item ID', right_on='Item ID')

    # Filtrar los datos por el género proporcionado
    genre_data = merged_data[merged_data['Genres'] == genre]

    # Encontrar el usuario con más tiempo de juego
    max_user = genre_data.groupby('User ID')['Play Time Forever'].sum().idxmax()

    # Agrupar por año de lanzamiento y calcular el tiempo total de juego para cada año
    year_playtime = genre_data.groupby('Release Date')['Play Time Forever'].sum().reset_index()

    # Crear la lista de horas jugadas por año
    hours_played: List[dict] = [{"Año": row['Release Date'], "Horas": row['Play Time Forever']} for _, row in year_playtime.iterrows()]

    # Crear el diccionario de retorno
    result = {"Usuario con más horas jugadas para Género X": max_user, "Horas jugadas": hours_played}

    return result



