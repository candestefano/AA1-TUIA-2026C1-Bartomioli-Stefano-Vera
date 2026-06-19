FROM python:3.10-slim

# Evita prompts raros durante instalación
ENV PYTHONUNBUFFERED=1

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiamos requirements primero (mejor cache)
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el proyecto dentro del contenedor
COPY . .

# Comando que se ejecuta cuando corre el container
CMD ["python", "inferencia.py"]