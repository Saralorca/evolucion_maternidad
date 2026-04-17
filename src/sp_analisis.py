import pandas as pd
import scipy.stats as stats 

def normalidad (df, percepcion_sociedad):
  for percepcion in percepcion_sociedad:
    statistic, p_value = stats.shapiro(df[percepcion])

    if p_value > 0.05:
      print(f"Los datos de {percepcion.upper()} SI siguen una distribución normal")
    else:
      print(f"Los datos de {percepcion.upper()} NO siguen una distribución normal")

def homocedasticidad (df, col_control, percepcion_sociedad):
  for percepcion in percepcion_sociedad:
    df_grupos = []

    for valor in df[col_control].unique():
      df_grupos.append(df[df[col_control] == valor] [percepcion])

    statistic, p_value = stats.levene(*df_grupos)

    if p_value > 0.05:
      print(f"Para la columna {percepcion.upper()} las varianzas son homogéneas entre grupos, es decir, SI hay homocedasticidad")
    else:
      print(f"Para la columna {percepcion.upper()} las varianzas no son homogéneas entre grupos, es decir, NO hay homocedasticidad")

def mannwhitneyu (df, col_control, percepcion_sociedad):

  for percepcion in percepcion_sociedad:
    valores_control = df[col_control].unique()

    control = df[df[col_control] == valores_control[0]][percepcion]
    test = df[df[col_control] == valores_control[1]][percepcion]

    statistic, p_value = stats.mannwhitneyu(control, test)

    if p_value > 0.05:
      print(f'Para la métrica {percepcion.upper()}, las medianas son iguales, es decir, NO hay diferencias significativas entre los grupos')
    else:
      print(f'Para la métrica {percepcion.upper()}, las medianas no son iguales, es decir, SI hay diferencias significativas entre los grupos')