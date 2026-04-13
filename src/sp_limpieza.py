import pandas as pd

def categorias_p4 (valor):
  """
  Estandariza y categoriza las respuestas abiertas de la columna P4 (edad ideal).
  
  La función procesa el texto para identificar intenciones o edades numéricas:
  - Detecta menciones a estabilidad económica o laboral.
  - Extrae números del texto mediante expresiones regulares.
  - Clasifica los valores numéricos en tres rangos generacionales:
    * Antes de los 30 años.
    * Entre 30 y 35 años (incluye casos donde se mencionan ambos límites).
    * Más de 35 años.

  Parameters:
  valor (str/int): El contenido de la celda de la columna P4.

  Returns:
  str: Una etiqueta categórica estandarizada o None si no hay coincidencia.
  """
  valor = str(valor).lower()
  if 'estable' in valor or 'estabilidad' in valor or 'economía' in valor:
    return 'Al tener estabilidad'
  if '30' in valor and '35' in valor:
    return 'Entre 30 y 35 años'
  import re
  numeros = re.findall(r'\d+', valor)
  if numeros:
    edad = int(numeros[0])
    if edad < 30: return 'Antes de los 30 años'
    if 30 <= edad <= 35: return 'Entre 30 y 35 años'
    if edad > 35: return "Más de 35 años"
 

def limpiar_escalas (df, columnas_escala): 
  """
  Limpia y transforma columnas de escalas Likert de texto a formato numérico entero.
  
  El proceso realiza las siguientes acciones:
  - Elimina las etiquetas de texto en los extremos de la escala:
    * "Nada de acuerdo 0" se convierte en "0".
    * "Totalmente de acuerdo 10" se convierte en "10".
  - Convierte los valores a tipo numérico (float/int).
  - Gestiona errores: si encuentra valores no numéricos (como texto inesperado), los transforma en nulos (NaN) para no romper el análisis.
  - Formatea el resultado final como tipo 'Int64', que permite valores enteros manteniendo la compatibilidad con valores nulos.

  Parameters:
  df (pd.DataFrame): El DataFrame que contiene los datos de la encuesta.
  columnas_escala (list): Lista con los nombres de las columnas que contienen escalas.

  Returns:
  None: Modifica el DataFrame original directamente (In-place).
  """
  for col in columnas_escala:
    if col in df.columns:
      df[col] = df[col].astype(str).str.replace('Nada de acuerdo 0', '0')
      df[col] = df[col].astype(str).str.replace('Totalmente de acuerdo 10', '10')
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
    df[col] = df[col].astype('Int64')

