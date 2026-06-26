FROM python:3.10-slim

WORKDIR /app

# Instalamos dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copiamos e instalamos dependencias Python
COPY requeriments.txt .
RUN pip install --no-cache-dir -r requeriments.txt

# Copiamos archivos necesarios
COPY inferencia.py .
COPY best_rain_model.pkl .
COPY preprocessor.joblib .

# Si querés incluir un CSV de prueba:
COPY weatherAUS_2026C1.csv .

# Ejecutamos el script
CMD ["python", "inferencia.py"]