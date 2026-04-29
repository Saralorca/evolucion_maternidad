# evolucion_maternidad

La maternidad desempeña un papel crucial en a sociedad y, sobre todo, en la vida de las mujeres. No obstante, su percepción ha ido cambiando a lo largo del tiempo en función del contexto histórico y social. Es por ello que esta investigación trata de analizar la evolución de la visión de la maternidad en mujeres de distintas generaciones en la provincia de Alicante, con el fin de identificar las diferencias y/o relaciones entre mujeres de diferentes grupos de edad, así como sus motivaciones o creencias acerca de este tema. Para llevar a cabo esta investigación se realiza una encuesta a mujeres de 18 a 75 años, la cual permite recopilar información y conocer las opiniones de las mujeres sobre la maternidad.

## **Archivo eda**:

**Análisis preliminar de los datos**

- **P1**: Los estadísticos nos muestran que el valor máximo es 2020, es incorrecto porque el cuestionario está enfocado a mujeres mayores de 18 años.
- **P2.1**: Tiene nulos, filas en las que no hay respuestas porque va dirigida a mujeres que no han sido madres (dejarla así)
- **P3**: Los nulos que hay son filas sin respuesta porque va dirigida a mujeres que sí han sido madres (la dejamos así). Cambiar a Int64 para que soporte los nulos.
  Los estadísticos muestran que el valor mínimo es 2, es incorrecto porque no ha podido tener su primer hijo con 2 años. Convertir esa respuesta en nulo.
- **P4**: Crear categorías de respuestas, ya que las respuestas, al ser abiertas, varían entre rangos de edad y momentos vitales. Los nulos son filas sin respuesta porque va dirigida a mujeres que no han sido madres.
- **P7**: los nulos son huecos vacíos porque la pregunta va dirigida a mujeres que sí han sido madres (dejarla así)
- **P8.1, P8.2, P8.3**: sustituir el Nada de acuerdo por 0 y Totalmente de acuerdo por 10 y cambiar a int.
- **P21**: Sustituir respuesta "Sanitària publica" por "Sanitaria pública"

## **Archivo limpieza_datos**

- **P1**: Se han quitado las dos filas en las que año de nacimiento es 2020
- **P3**: Se ha convertido la respuesta = 2 en nulo. Se ha cambiado a Int64 para que soporte los nulos.
- **P4**: Se han creado categorías de respuestas: "Antes de los 30 años", "Entre 30 y 35 años", "Más de 35 años", "Al tener estabilidad".
- **P8.1, P8.2, P8.3**: Se ha sustituido el "Nada de acuerdo 0" por "0" y "Totalmente de acuerdo 10" por "10". Los "N.S" y "N.C" se han convertido en nulos. Se ha cambiado a Int64 para que soporte los nulos.
- **P21**: Se ha sustituido la respuesta "Sanitària publica" por "Sanitaria pública".

- No se van a gestionar los nulos ya que, o bien son respuestas como "N.S" o "N.C" poco representativas o son respuestas vacías ya que la pregunta solo debe responderla o las mujeres que son madres o las que no lo son.

## **Archivo análisis**

**Estadísticos numéricos**:

- **P1**: El año de nacimiento medio es 1983 (41 años) y la mediana (el año de nacimiento más repetido) es 1987 (37 años). El año de nacimiento mínimo es 1950 (74 años) y el máximo 2005 (19 años), es decir, el grupo de edad de las mujeres que han participado en este cuestionario es de 19 a 74 años.
- **P3**: La edad mínima en la que una mujer encuestada ha sido madre es de 16 años y, la máxima, 41 años. La edad media en la que las mujeres han tenido su primer hijo/a es 29 años, coincidiendo con la mediana.
- **P5**: En cuanto a la presión que han sentido las mujeres para ser madres la media es de 2,66 y la mediana es de 1. La desviación estándar es de 3,11, lo que indica que hay mayor variabilidad en las respuestas.
- **P8.1**: "La sociedad percibe la maternidad como una obligación o un deber como mujer". En una escala del o al 10, la media de respuestas está en un 4,43, es decir, que la media se inclina un poco más a no estar a favor de la anterior afirmación.
- **P8.2**: "La sociedad percibe la maternidad como una elección". La media es de 3,68, es decir, se inclina más a estar en contra de la anterior afirmación.
- **P8.3**: "La sociedad percibe la maternidad como un derecho". La media es de 3,74, por tanto, tienden a estar en contra de la anterior afirmación.
- **P14.1**: En una escala del 1 al 7, la media es de 6,42, es decir, la mayoría describirían a una madre como cariñosa, más que distante.
- **P14.2**: En una escala del 1 al 7, la media es de 6,52, es decir, la mayoría describirían a una madre como protectora.
- **P14.3**: En una escala del 1 al 7, la media es de 6,30, es decir, la mayoría describirían a una madre como sacrificada.
- **P14.4**: En una escala del 1 al 7, la media es de 6,06, es decir, la mayoría describirían a una madre como organizada.
- **P14.5**: En una escala del 1 al 7, la media es de 6,42, es decir, la mayoría describirían a una madre como fuerte.
- **P14.6**: En una escala del 1 al 7, la media es de 5,97, es decir, la mayoría describirían a una madre como paciente.
- **P14.7**: En una escala del 1 al 7, la media es de 6,55, es decir, la mayoría describirían a una madre como cuidadora.
- **P16**: En una escala del 0 al 10, la media es de 8,74 y la mediana de 10, por tanto, la mayoría de las encuestadas considera que la adopción es una alterniva a la maternidad biológica.
- **P20**: En una escala del 0 al 10, la media es de 3,61, y la mediana de 4, por tanto, hay una mayor inclinación a una ideología de izquierdas.

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
