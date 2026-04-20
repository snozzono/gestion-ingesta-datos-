import logging
from extract import fetch_weather
from transform import transform_weather
from load import save_to_csv

# Coordenadas de Santiago, Chile
LAT = -33.45
LON = -70.66

OUTPUT = "../data/clima_santiago.csv"

logging.basicConfig(
    filename='../logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_pipeline():
    logging.info("=== INICIO PIPELINE CLIMA CHILE ===")

    raw_data = fetch_weather(LAT, LON)
    if not raw_data:
        logging.error("No se obtuvieron datos")
        return

    transformed = transform_weather(raw_data)
    save_to_csv(transformed, OUTPUT)

    logging.info(f"Registros procesados: {len(transformed)}")
    logging.info("=== FIN PIPELINE ===")

if __name__ == "__main__":
    run_pipeline()