PI_1-MLOps Juegos Steam - Modelo de Recomendación
Este repositorio se corresponde con el Proyecto Individual 1 del bootcamp de Machine Learning en Henry.

Descripción del Proyecto:
El objetivo principal de este proyecto es emular las funciones de un MLOps Engineer, que amalgama las responsabilidades de un Data Engineer y un Data Scientist, dentro del entorno de la plataforma de juegos Steam. El reto empresarial planteado radica en desarrollar un Producto Mínimo Viable (MVP)que incorpora una APIfuncional y un modelo de Machine Learningpara analizar sentimientos basados ​​en comentarios de usuarios y proporcionar un sistema de recomendación de videojuegos para la plataforma.

Datos:
El proyecto se fundamenta en tres archivos en formato JSON:

output_steam_games.json : Contiene información detallada sobre los juegos, incluyendo nombre, desarrollador, género y etiquetas.

australian_users_items.json : Ofrece datos sobre los juegos utilizados por los usuarios y el tiempo dedicado a cada juego.

australian_users_reviews.json : Contiene comentarios y recomendaciones de usuarios sobre los juegos, junto con las fechas de los comentarios.

Tareas Desarrolladas:
ETL (Extracción, Transformación y Carga)
Se han creado los Notebooks ETL_JSON(output_steam_games) , ETL_JSON(australian_users_items) , y ETL_JSON(australian_user_reviews) .

En esta fase, se extrajo y limpió la información de los dataframes iniciales para facilitar su comprensión. Se aplicaron directrices definidas en el enunciado del proyecto, eliminando información redundante para alcanzar los objetivos establecidos.

Se utilizó la librería 'NLTK' para realizar un análisis de sentimientos en la columna 'reviews' del conjunto de datos correspondiente. Se categorizaron los comentarios según su polaridad en positivos (2), neutrales (1) y negativos (0), y se generó una nueva columna llamada 'sentiment_analysis'.

Una vez concluida la fase de limpieza, se prepararon los conjuntos de datos para la etapa siguiente, almacenándolos en formato 'parquet'.

EDA (Análisis Exploratorio de Datos)
Durante esta etapa, se analizaron los tres conjuntos de datos posteriores al proceso ETL para visualizar de forma más precisa cada variable categórica y numérica. El objetivo principal fue identificar las variables esenciales para los endpoints y el modelo de recomendación, elementos clave en el objetivo final del aprendizaje automático. Asimismo, se crearon nuevos conjuntos de datos para la fase de 'ingeniería de características'.

Cuaderno Análisis Exploratorio

Creación de funciones
Después de depurar la información, se seleccionan los conjuntos de datos necesarios para abordar cada función específica. Esta estrategia se implementó para optimizar significativamente el desempeño y mejorar los tiempos computacionales asociados a cada tarea.

Las funciones desarrolladas son:

PlayTimeGenre: Recibe un género como parámetro y devuelve el año con más horas jugadas para dicho género.

UserForGenre: Recibe un género y devuelve el usuario con mayor tiempo de juego, generando un diccionario que muestra la acumulación de tiempo de juego por año.

UserRecommend: Recibe un año y devuelve el Top 3 de juegos recomendados para ese período.

UsersWorstDeveloper: Recibe un año y retorna el Top 3 de peores empresas desarrolladoras basándose en el análisis de sentimientos de las reseñas.

sentiment_analysis: Toma el año de lanzamiento de un juego como parámetro y devuelve una lista con la cantidad de registros de reseñas de usuarios clasificados por análisis de sentimientos (Negativo, Neutral o Positivo) correspondientes a ese año.

Funciones del Notebook_Endpoints

Aprendizaje automático modelado
Se utilizan los conjuntos de datos obtenidos en las fases de ETL y EDA, centrándose particularmente en el conjunto de datos llamado modelo_item, el cual incluye información sobre géneros de videojuegos, títulos e identificaciones.

recomendacion_juego: Recibe el parámetro "item_id" de un título de juego y genera una lista con los cinco juegos más similares, proporcionando recomendaciones basadas en la similitud de género. Este enfoque ofrece sugerencias relevantes y específicas considerando las preferencias de género del juego proporcionadas mediante la comparación item_item.
Cuaderno Modelado_ML

API rápida
El código para generar la API está contenido en el archivo Main . Para ejecutar la API desde localHost, sigue estos pasos:

Clona el proyecto con git clone https://github.com/capitanfeeder/Modelo_ML_STEAM.git.
Prepare el entorno en Visual Studio Code:
Crea el entorno conpython -m venv env
Activa el entorno conenv\Scripts\activate
Instale las dependencias conpip install -r requirements.txt
Ejecuta main.pydesde la consola activando uvicorn. Para ello, uvicorn main:app --host 127.0.0.1 --port 8000EE.UU.
Haz Ctrl + clic en la dirección http://XXX.X.X.X:XXXX(se muestra en la consola).
En el navegador, añade /docsal final de la URL para acceder a la documentación.
En cada función, haga clic en Pruébelo , introduzca los datos requeridos o utilice los ejemplos por defecto. Finalmente, haz clic en Ejecutar para ver la respuesta.
Despliegue
Despliegue en Railway: Se optó por la plataforma Railway para implementar la API debido a su integración y despliegue automático desde GitHub, lo que agiliza y simplifica el proceso de implementación.
