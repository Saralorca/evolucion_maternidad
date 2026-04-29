# **Análisis de la evolución generacional de las mujeres sobre la maternidad**

## **Descripción del proyecto**

La maternidad desempeña un papel crucial en a sociedad y, sobre todo, en la vida de las mujeres. No obstante, su percepción ha ido cambiando a lo largo del tiempo en función del contexto histórico y social. Es por ello que esta investigación trata de analizar la evolución de la visión de la maternidad en mujeres de distintas generaciones en la provincia de Alicante, con el fin de identificar las diferencias y/o relaciones entre mujeres de diferentes grupos de edad, así como sus motivaciones o creencias acerca de este tema. Para llevar a cabo esta investigación se realiza una encuesta a mujeres de 18 a 75 años, la cual permite recopilar información y conocer las opiniones de las mujeres sobre la maternidad.

## **Estructura de carpetas**

- `data/`: Contiene los dataset originales (fuente: elaboración propia).
  - `INE/`: Contiene los dataset proporcionados por el INE
- `notebooks/`: Jupyter Notebooks con el proceso completo de limpieza y análisis.
- `pdf`: Archivos pdf con las preguntas del cuestionario realizado y la memoria de un trabajo de fin de grado (TFG).
- `src/`: Scripts de Python con funciones personalizadas para la limpieza de datos y análisis de los mismos.
- `requirements.txt`: Listado de librerías necesarias (Pandas, Seaborn, etc.) para ejecutar el proyecto.
- `.gitignore`: Archivo para evitar la subida de archivos basura y el entorno virtual (venv/).

## **Metodología y Limpieza de Datos:**

**Análisis preliminar de los datos**

Se ha realizado un proceso exhaustivo de limpieza para asegurar la integridad del análisis:

- **Validación de rangos**: Se detectaron y corrigieron errores en años de nacimiento (los datos mostraban registros de 2020 estando enfocado a mujeres mayores de 18 años).
- **Normalización**: Transformación de variables categóricas abiertas a categorías cerradas (por ejemplo, rangos de edad para un primer/a hijo/a) y unifcación de textos (corrección de errores tipográficos como "Sanitària publica").
- **Tratamiento de nulos**: Se identificaron nulos estructurales (preguntas filtro para las que son madres o no) y se mantuvieron para evitar sesgos, utilizando tipos de datos `Int64` para permitir valores `NaN` en cálculos numéricos.
- **Escalas**: Transformación de etiquetas de texto ("Nada de acuerdo") a valores numéricos (0-10) para permitir el análisis estadístico.

## **Hallazgos e Insights:**

- **Perfil de la muestra**: El análisis abarca mujeres de entre 19 y 74 años, siendo la edad media de maternidad los 29 años.
- **Percepción social Social de la Maternidad**: La mayoría de las mujeres no percibe que la sociedad vea la maternidad como un derecho o una elección clara (medias inferiores a 4/10).
- **Características de Madre**: Se observa una visión muy definida de la figura materna, destacando atributos como cuidadora (6,55/7), protectora y cariñosa, frente a valores ligeramente más bajos en paciencia u organización.
- **Adopción como alternativa**: Hay un consenso muy alto en la adopción como alternativa válida a la maternidad biológica (8,74/10).
- **Posición ideológica**: Hay una mayor inclinación por parte de las mujeres encuestadas a una ideología de izquierdas (3,61/10).

**Análisis comparativo ideología-percepción de la maternidad**

- En la percepción de la maternidad como una obligación o deber hemos comprobado que existen diferencias significativas entre los grupos ideológicos a través de las pruebas estadísticas de normalidad. Además, también podemos observarlas a través del primer gráfico: Las mujeres con una ideología de derecha tienden a estar más de acuerdo con que la sociedad percibe la maternidad como una obligación o deber, mientras que las mujeres con una ideología de derecha, tienden a estar más en desacuerdo.
- En la percepción de la maternidad como una elección también existen diferencias significativas entre los grupos. El segundo gráfico nos muestra lo contrario al caso anterior, es decir, las mujeres con una ideología de derecha tienden a estar de acuerdo con que la sociedad percibe la maternidad como una elección, mientras que las de una ideología de izquierda tienden a estar más en desacuerdo.
- En la percepción de la maternidad como un derecho ocurre lo mismo que en el primer caso.

**Conclusiones**

Tras haber realizado un análisis exhaustivo de los resultados obtenidos podemos llegar a varias conclusiones. En primer lugar, hemos visto que más de la mitad de las mujeres encuestadas tienen hijos o hijas, asimismo, la mayoría de las mujeres que no son madres también desearían serlo. En segundo lugar, la edad media a la que las madres, en este caso, han tenido su primer/a hijo/a es a los 28,66 años, cifra más baja que la edad media a la maternidad en España -según el Instituto Nacional de Estadística (INE) en 2024 era de 32,61 años-. Principalmente, las mujeres que quieren ser madres desearían serlo entre los 30 y 35 años.

Según los datos del INE, la tasa bruta de natalidad ha sufrido un notable descenso desde 1975 hasta 2024, pasando de 18,7 a 6,49 nacimientos por cada mil habitantes en este último año.
Por tanto, se podría decir que la baja natalidad de este país y el aumento de la edad media a la maternidad en los últimos años no viene propiciada por la falta de deseo de las mujeres en convertirse en madres (según el INE, en España en 2018 casi el 90% de las mujeres deseaba tener uno/a hijo/a o más), sino debido, esencialmente, a factores socioeconómicos. Las personas encuestadas destacan principalmente tres motivos por los cuales se retrasa la edad de la maternidad: la inestabilidad económica, la precariedad laboral y la difícil emancipación.

En tercer lugar, la mayoría de mujeres no considera que se haya sentido presionada para ser madre, no obstante, el 28% de ellas afirma haber sentido presión por parte de la sociedad en general y el 18% por parte de sus familiares. Por tanto, observamos que las mujeres siguen estando sometidas a una presión social para convertirse en madres, lo que podría generar frustración en aquellas mujeres que desean serlo y que por factores externos a ellas no lo son.

Siempre se han escuchado connotaciones positivas en cuanto a la maternidad, no obstante, en este caso concreto podemos destacar que prácticamente todas las mujeres que son madres han experimentado sensaciones como la preoupación (48%), miedo (33%), ansiedad (32%) o culpa (23%), entre otras, durante su maternidad. De modo que resalta que únicamente el 5% de éstas no haya experimentado ninguna de las sensaciones anteriormente mencionadas, cuando apenas se expresan de manera pública.

Las mujeres han estado vinculadas desde el principio de la historia a la maternidad, sin embargo, en este caso concreto vemos que la mayoría de mujeres niega esta unión mujer-maternidad. Ahora bien, si nos referimos al concepto de instinto maternal, el cual ha generado a lo largo del tiempo mucha controversia, observamos que casi la mitad de las mujeres considera que sí existe un instinto maternal innato en todas las mujeres. Por tanto, podríamos decir que los roles tradicionales relacionados con la maternidad siguen muy arraigados en la sociedad.

La mujer, además de estar vinculada a la maternidad, también se le atribuye el rol de cuidadora. Esto ha ido cambiando a lo largo del tiempo, al ir asignando responsabilidades a los madres, no obstante, éstas no son, ni mucho menos, equilibradas, pues las mujeres siguen siendo las principales responsables. A pesar de ello, más de la mitad de las mujeres considera que la responsabilidad de la madre y la del padre tiene el mismo peso en la crianza de los hijos/as.
