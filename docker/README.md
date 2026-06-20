\# MLOps - Contenedor de Inferencia



Este proyecto contiene un contenedor Docker para realizar inferencias utilizando un modelo entrenado con PyCaret.



El modelo predice la variable objetivo a partir de datos meteorológicos de entrada.



\---



\##  Estructura del proyecto



La carpeta `docker` contiene los siguientes archivos:



docker/

├── inferencia.py

├── requirements.txt

├── Dockerfile

├── best\_rain\_model.pkl

└── README.md



\---



\##  Entrada de datos



El contenedor espera un archivo de entrada ubicado en:



/files/input.csv



Este archivo debe contener las variables predictoras, sin la columna objetivo.



\---



\##  Salida de datos



El contenedor genera automáticamente:



/files/output.csv



Este archivo contiene las predicciones del modelo.



\---



\##  Construcción de la imagen Docker



Desde la carpeta `docker`, ejecutar:



docker build -t tp-clasificacion .



\---



\##  Ejecución del contenedor



\### Linux / Mac:



docker run --rm -v $(pwd)/files:/files tp-clasificacion



\### Windows (PowerShell):



docker run --rm -v ${PWD}/files:/files tp-clasificacion



\---

