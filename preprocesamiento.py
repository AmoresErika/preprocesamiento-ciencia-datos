import pandas as pd

def cargar_datos(ruta):
    return pd.read_csv(ruta)

def eliminar_nulos(dataframe):
    return dataframe.dropna()

def eliminar_duplicados(dataframe):
    return dataframe.drop_duplicates()

def normalizar_columnas(dataframe):
    dataframe.columns = dataframe.columns.str.lower()
    return dataframe

def guardar_datos(dataframe, ruta):
    dataframe.to_csv(ruta, index=False)

print("Preprocesamiento listo")