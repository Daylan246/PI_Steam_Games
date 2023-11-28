como parámetro y devuelve una lista con la cantidad de registros de reseñas de usuarios clasificados por análisis de sentimientos (Negativo, Neutral o Positivo) correspondientes a ese año.

Funciones del Notebook_Endpoints

Aprendizaje automático modelado
Se utilizan los conjuntos de datos obtenidos en las fases de ETL y EDA, centrándose particularmente en el conjunto de datos llamado modelo_item, el cual incluye información sobre géneros de videojuegos, títulos e identificaciones.

recomendacion_juego: Recibe el parámetro "item_id" de un título de juego y genera una lista con los cinco juegos más similares, proporcionando recomendaciones basadas en la similitud de género. Este enfoque ofrece sugerencias relevantes y específicas considerando las preferencias de género del juego proporcionadas mediante la comparación item_item.
Cuaderno Modelado_ML
