FROM python:3.10-slim

# Evita prompts raros durante instalación
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos requeriments primero (mejor cache)
COPY requeriments.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requeriments.txt

# Copiamos todo el proyecto dentro del contenedor
COPY . .

# Comando que se ejecuta cuando corre el container
CMD ["python", "inferencia.py"]