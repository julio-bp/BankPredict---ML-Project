from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np
from IPython.display import display
import matplotlib.pyplot as plt
import seaborn as sns

# Encuentra la raíz del proyecto usando __file__

BASE_DIR = Path(__file__).resolve().parent.parent

# Define la carpeta data_clean/

DATA_CLEAN_DIR = BASE_DIR / "data" / "cleaned"

# Limpieza y observación

def informe(x):
    print("Información del DataFrame:")
    print(x.info())
    print("Descripción estadística:")
    print(x.describe())
    print("Valores nulos:")
    print(x.isnull().sum())
    print("Tipos de datos:")
    print(x.dtypes)
    print("Primeras 5 filas:")
    print(x.head())
    print("Últimas 5 filas:")
    print(x.tail())
    print("Forma del DataFrame:")
    print(x.shape)
    print("columnas")
    print(x.columns)


def datos(x):
    print("datos nulos")
    print(x.isnull().sum())
    print("datos totales")
    print(x.count())   
    print("porcentaje de nulos")
    print(x.isnull().sum() / x.shape[0]*100)
    print("datos duplicados")
    print(x.duplicated().sum())


def eliminar_na(df):
    """
    Toma un dataframe y elimina NaN
    """
    cols = ["clnt_tenure_yr","clnt_tenure_mnth","gendr","num_accts","bal","calls_6_mnth","logons_6_mnth"]
    df = df.dropna(subset=cols)
    return df

def inspeccionar_columnas(df):
    """
    Imprime el nombre de cada columna, el número de valores únicos 
    y la lista de esos valores.
    """
    for col in df.columns:
        valores_unicos = df[col].unique()
        n_unicos = len(valores_unicos)
        
        print(f"COLUMNA: {col.upper()}")
        print(f"Número de valores únicos: {n_unicos}")
        print(f"Valores: {valores_unicos}")
        print("-" * 30) # Línea separadora

# Guardar dataframe final como csv en data/cleaned/

def save_data_clean(df, nombre):
    """
    Guarda el dataframe en la carpeta data/cleaned.
    """
    out_dir = DATA_CLEAN_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    file_name = f"{nombre}.csv"
    out_path = out_dir / file_name

    df.to_csv(out_path, index=False, sep=';')
    
    print(f"Guardado con éxito en: {out_path}")
    return "ok"

# Cargar csv de dataframe final

def load_data_clean(nombre_archivo):
    """
    Carga un archivo CSV desde la carpeta data/cleaned forzando el separador ;
    """
    path = DATA_CLEAN_DIR / nombre_archivo
    
    print(f"Buscando archivo en: {path}")
    
    return pd.read_csv(path, sep=';', engine='python')