import csv
import logging
import requests
import pandas as pd
from datetime import datetime

# Configuración de logging
logging.basicConfig(filename='ingesta_datos.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# URL de ejemplo de API pública
API_URL = "https://jsonplaceholder.typicode.com/posts"

# Función para obtener datos de una API pública
def obtener_datos_api():
    try:
        logging.info('Iniciando la obtención de datos desde la API...')
        response = requests.get(API_URL)
        response.raise_for_status()  # Si hay un error HTTP, se lanza una excepción
        datos = response.json()
        logging.info(f'{len(datos)} registros obtenidos correctamente de la API.')
        return datos
    except requests.exceptions.RequestException as e:
        logging.error(f"Error al obtener datos de la API: {e}")
        return []

# Función para guardar los datos en un archivo CSV
def guardar_datos_csv(datos, archivo_salida):
    try:
        logging.info(f'Guardando {len(datos)} registros en el archivo {archivo_salida}...')
        df = pd.DataFrame(datos)
        df.to_csv(archivo_salida, mode='a', header=not pd.io.common.file_exists(archivo_salida), index=False)
        logging.info(f'{len(datos)} registros guardados en el archivo {archivo_salida}.')
    except Exception as e:
        logging.error(f"Error al guardar los datos en el archivo: {e}")

# Función principal que automatiza el proceso
def main():
    # Paso 1: Obtener los datos
    datos = obtener_datos_api()
    
    if datos:
        # Paso 2: Guardar los datos
        archivo_salida = 'datos_ingresados.csv'
        guardar_datos_csv(datos, archivo_salida)
    else:
        logging.error("No se obtuvieron datos para guardar.")

if __name__ == '__main__':
    main()
