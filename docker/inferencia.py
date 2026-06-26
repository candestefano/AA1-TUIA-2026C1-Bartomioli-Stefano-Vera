import pandas as pd
import joblib
from pycaret.classification import load_model, predict_model

INPUT_PATH = 'weatherAUS_2026C1.csv'


def preprocesar(df, prep):

    df = df.copy()

    # Fecha -> mes
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['mes'] = df['fecha'].dt.month

    # Eliminar columnas innecesarias
    df = df.drop(
        columns=['fecha', 'id', 'llueve_manana', 'lluvia_manana'],
        errors='ignore'
    )

    # Imputación
    for col in prep['col_imputar']:

        medias_grupo = prep['medias_imputacion'][col]['grupo']
        media_global = prep['medias_imputacion'][col]['global']

        df[col] = df.apply(
            lambda row:
                medias_grupo.get(
                    (row['ubicacion'], row['mes']),
                    media_global
                )
                if pd.isnull(row[col])
                else row[col],
            axis=1
        )

        df[col] = df[col].fillna(media_global)

    # Variable binaria
    df['llovio_hoy'] = df['llovio_hoy'].map(
        prep['llovio_hoy_map']
    )

    # One-Hot
    df = pd.get_dummies(
        df,
        columns=prep['cols_cat'],
        drop_first=True
    )

    # Alinear columnas
    df = df.reindex(
        columns=prep['columnas_finales'],
        fill_value=0
    )

    # Escalar
    df[prep['cols_num_scale']] = prep['scaler'].transform(
        df[prep['cols_num_scale']]
    )

    return df


# ==========================
# Flujo principal
# ==========================

prep = joblib.load('preprocessor.joblib')

model = load_model('best_rain_model')

df_input = pd.read_csv(INPUT_PATH)

df_procesado = preprocesar(df_input, prep)

predictions = predict_model(model, data=df_procesado)

salida = predictions[['prediction_label', 'prediction_score']]

salida.to_csv('/files/predicciones.csv', index=False)

print("Archivo guardado correctamente")

print(predictions[['prediction_label', 'prediction_score']])