# 🌎 Pipeline de Datos Climáticos - Chile

## 📌 Descripción del Proyecto

Este proyecto implementa un pipeline de datos básico en Python enfocado en la **ingesta automatizada de datos climáticos en Chile**, específicamente en Santiago.

El objetivo es demostrar la primera etapa de un pipeline de datos: la extracción, transformación y almacenamiento de información desde una fuente externa, asegurando trazabilidad y automatización del proceso.

---

## 🧠 ¿Qué es un Pipeline de Datos?

Un pipeline de datos es un conjunto de procesos automatizados que permiten extraer, transformar y almacenar datos desde una fuente de origen hacia un destino estructurado, facilitando su análisis posterior.

---

## 🔹 Rol de la Ingesta de Datos

La ingesta corresponde a la primera etapa del pipeline y tiene como propósito obtener datos desde una fuente externa y almacenarlos de forma organizada, garantizando:

- Disponibilidad  
- Consistencia  
- Trazabilidad  

---

## 🌐 Fuente de Datos

Se utiliza la API de Open-Meteo, la cual proporciona datos climáticos en tiempo real.

### ✔ Justificación
- Datos reales  
- Acceso gratuito (sin API Key)  
- Formato JSON estructurado  
- Fácil integración con Python  

---

## ⚙️ Diseño del Pipeline

El flujo implementado consta de tres etapas principales:

### 1. Extracción
Se realiza una solicitud HTTP a la API para obtener datos climáticos de Santiago, Chile.

### 2. Transformación
Se seleccionan y estructuran las variables relevantes:
- Temperatura  
- Velocidad del viento  
- Dirección del viento  
- Fecha/hora  

### 3. Carga
Los datos son almacenados en un archivo CSV para su uso posterior.

---

## 🤖 Automatización

El pipeline se ejecuta mediante un script en Python (`main.py`), el cual puede ser programado para ejecución automática usando:

- Cron (Linux/Mac)
- Programador de tareas (Windows)

Ejemplo en cron:
0 9 * * * python3 src/main.py

## 🧾 Logging (Trazabilidad)

Se implementa un sistema de logging que registra:

- Inicio del proceso  
- Ejecución exitosa  
- Cantidad de registros procesados  
- Errores detectados  

Archivo generado:

logs/pipeline.log

## ⚠️ Control de Errores

El pipeline incluye manejo básico de errores:

- Validación de respuesta de la API  
- Manejo de excepciones  
- Registro de fallos en logs  

## 🗂️ Estructura del Proyecto


data_pipeline/
│── data/
│ └── clima_santiago.csv
│── logs/
│ └── pipeline.log
│── src/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ └── main.py
│── requirements.txt
│── README.md


## 🚀 Ejecución del Proyecto

### 1. Instalar dependencias

pip install -r requirements.txt


### 2. Ejecutar el pipeline

cd src
python main.py

## 📊 Output

- Archivo de datos:  

data/clima_santiago.csv


- Archivo de logs:  

logs/pipeline.log

## 🔧 Tecnologías Utilizadas

- Python  
- Requests (API HTTP)  
- CSV  
- Logging  

## 📈 Posibles Mejoras

- Almacenamiento en base de datos (SQLite/PostgreSQL)  
- Ingesta de múltiples ciudades  
- Datos históricos  
- Visualización de datos  
- Dockerización del pipeline  



## 🧠 Conclusión

El desarrollo de este pipeline permitió comprender la importancia de la automatización en la ingesta de datos, así como la necesidad de estructurar procesos reproducibles, trazables y escalables, estableciendo una base sólida para futuras etapas del procesamiento de datos.

