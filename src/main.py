import logging
from extract import fetch_data
from transform import transform_data
from load import save_to_csv

# Configuración de logging
logging.basicConfig(
    filename='../logs/pipeline.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT = "../data/users.csv"

def run_pipeline():
    logging.info("=== INICIO DEL PIPELINE ===")

    data = fetch_data(URL)
    if not data:
        logging.error("No se obtuvieron datos")
        return

    transformed = transform_data(data)
    save_to_csv(transformed, OUTPUT)

    logging.info("=== FIN DEL PIPELINE ===")

if __name__ == "__main__":
    run_pipeline()