# /*
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs:
#  * https://github.com/public-apis/public-apis
#  */
import json
import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=32.6278&longitude=-115.4545&daily=temperature_2m_max,temperature_2m_min,uv_index_max,precipitation_probability_max&timezone=GMT&forecast_days=1'
datos = requests.get(url)

# json.loads('json') sirve para pasar la info del json a un diccionario

if datos.status_code == 200:
    datos_diccionario = json.loads(datos.content)
    datos_diccionario = datos_diccionario["daily"]

    mensaje = f"Maxima: {datos_diccionario['temperature_2m_max']}C. Minima: {datos_diccionario['temperature_2m_min']}C. Precipitacion: {datos_diccionario['precipitation_probability_max']}%"

    print(mensaje)
