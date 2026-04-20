import csv
import logging

def save_to_csv(data, filepath):
    try:
        logging.info("Guardando datos en CSV...")
        keys = data[0].keys()

        with open(filepath, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)

        logging.info(f"Datos guardados correctamente en {filepath}")
    except Exception as e:
        logging.error(f"Error al guardar datos: {e}")