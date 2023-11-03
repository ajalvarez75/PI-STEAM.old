# PI-STEAM
Proyecto Individual - Steam

# Breve introduccion.

Este proyecto simula el rol de un MLOps Engineer, que desarrolla un proyecto de recomendaciones para la plataforma de videojuegos Steam.

El proyecto solicitaba realizar 5 funciones, las cuales fueron:
def PlayTimeGenre( genero : str ): Debe devolver año con mas horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

def UserForGenre( genero : str ): Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}

def UsersRecommend( año : int ): Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

def UsersNotRecommend( año : int ): Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

def sentiment_analysis( año : int ): Según el año de lanzamiento, se devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.
Ejemplo de retorno: {Negative = 182, Neutral = 120, Positive = 278}


Se solicito tambien realizar por lo menos un modelo de recomendacion de videojuegos, los cuales son:

Modelo de recomendación item-item:
def recomendacion_juego( id de producto ): Ingresando el id de producto, deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.

Modelo de recomendación user-item:
def recomendacion_usuario( id de usuario ): Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.

Para desarrollar este proyecto se proporcionaron tres archivos JSON: 

1. Australian_user_reviews.json 
2. Australian_users_items.json
3. output_steam_games.json

Se realizó el ETL(Extraction,Transformation,Loading) de los tres archivo json. de los cuales dos tenian columnas anidadas.

[ETL_games](Notebooks/ETL_games.ipynb)

[ETL_items](Notebooks/ETL_items.ipynb)

[ETL_reviews](Notebooks/ETL_reviews.ipynb)

Se realizo un EDA inicial dentro de los archivos que se transforaron dentro de la carpeta CSV.

# Elaboracion de respuestas

Se realizo el analsis de sentimientos.
[Analisis de sentimientos](Notebooks/Sentiment_analysis.ipynb)

Se realizaron las funciones solicitadas para el proyecto.
[Funciones](Notebooks/Functions.ipynb)

Para la elaboracion de la API se pasaron las funciones al archivo.
[Funciones para la api](main.py)
Las cuales fueron probadas dentro de http://127.0.0.1:8000/docs.

La api fue 
