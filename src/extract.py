import requests
import logging

def fetch_data(url):
    try:
        logging.info("Iniciando extracción de datos...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Datos obtenidos correctamente: {len(data)} registros")
        return data
    except Exception as e:
        logging.error(f"Error en extracción: {e}")
        return []