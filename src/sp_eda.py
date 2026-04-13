import pandas as pd

def analisis_preliminar (df):
  """
  Realiza un análisis exploratorio preliminar sobre un DataFrame dado.
  
  Este análisis incluye:
  - Muestra aleatoria de 5 filas del DataFrame.
  - Información general del DataFrame (tipo de datos, nulos, etc.).
  - Porcentaje de valores nulos por columna.
  - Conteo de filas duplicadas.
  - Distribución de valores para columnas categóricas.
  - Estadísticas de las columnas numéricas.

  Parameters:
  df (pd.DataFrame): DataFrame a analizar

  Returns:
  None
  """
  display(df.sample(5))

  print("------------------------------------------------------")

  print("DIMENSIONES")
  print(f"Nuestro conjunto de datos presenta un total de {df.shape[0]} filas y {df.shape[1]} columnas")

  print("--------------------------------------------------------")

  print("INFO")
  display(df.info())

  print("--------------------------------------------------------")

  print("NULOS")
  display(round(df.isnull().mean()*100), 2)

  print("--------------------------------------------------------")

  print("DUPLICADOS")
  print(f"Hay {df.duplicated().sum()} duplicados en el conjunto de datos")

  print("--------------------------------------------------------")

  print("FRECUENCIA CATEGÓRICAS")
  for col in df.select_dtypes(include='O').columns:
    print(df[col].value_counts())
    print("----------------")

  print("--------------------------------------------------------")

  print("ESTADÍSTICAS NUMÉRICAS")
  display(df.describe().T)