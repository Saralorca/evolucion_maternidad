# evolucion_maternidad

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
