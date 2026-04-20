import requests
import logging

def fetch_weather(lat, lon):
    try:
        logging.info("Iniciando extracción de datos climáticos...")
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        logging.info("Datos obtenidos correctamente")
        return data
    except Exception as e:
        logging.error(f"Error en extracción: {e}")
        return None