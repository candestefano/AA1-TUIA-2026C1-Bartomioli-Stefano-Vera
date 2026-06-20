import pandas as pd
import logging
from sys import stdout
from pycaret.classification import load_model, predict_model
import os

# ----------------------------
# Logger
# ----------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

logFormatter = logging.Formatter(
    "%(asctime)s %(levelname)s %(filename)s: %(message)s"
)

consoleHandler = logging.StreamHandler(stdout)
consoleHandler.setFormatter(logFormatter)
logger.addHandler(consoleHandler)

# ----------------------------
# Paths
# ----------------------------
MODEL_PATH = "best_rain_model"
INPUT_PATH = "/files/input.csv"
OUTPUT_PATH = "/files/output.csv"

# ----------------------------
# Cargar modelo
# ----------------------------
if not os.path.exists(MODEL_PATH + ".pkl"):
    logger.error(f"No se encontró el modelo en {MODEL_PATH}.pkl")
    exit(1)

model = load_model(MODEL_PATH)
logger.info("Modelo cargado correctamente")

# ----------------------------
# Leer datos de entrada
# ----------------------------
if not os.path.exists(INPUT_PATH):
    logger.error(f"No se encontró el archivo de entrada en {INPUT_PATH}")
    exit(1)

df_input = pd.read_csv(INPUT_PATH)
logger.info("Input cargado correctamente")

# ----------------------------
# Predicción
# ----------------------------
predictions = predict_model(model, data=df_input)
logger.info("Predicción realizada correctamente")

# PyCaret devuelve una columna llamada "prediction_label"
df_output = predictions[["prediction_label"]]
df_output.columns = ["RainTomorrow_predicted"]

# ----------------------------
# Guardar output
# ----------------------------
df_output.to_csv(OUTPUT_PATH, index=False)
logger.info(f"Output guardado en {OUTPUT_PATH}")
logger.info("Inferencia finalizada correctamente")
