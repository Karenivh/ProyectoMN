import streamlit as st

st.title("Aproximación discreta de mínimos cuadrados")

st.markdown(
    """
    ### Definición
    La aproximación discreta de mínimos cuadrados es un método utilizado para aproximar una función discreta a través de un modelo matemático, minimizando la suma de los errores cuadráticos entre los valores observados y los valores predichos por el modelo.

    La fórmula general para la aproximación discreta de mínimos cuadrados es:
    """
)
st.latex(r'''
   y = X * β
    ''')
st.markdown(
    """Donde:

    - y es el vector de valores observados.
    - X es la matriz de diseño que contiene las variables explicativas (o características) del modelo.
    - β es el vector de coeficientes desconocidos que se deben estimar."""

)

st.markdown('''El objetivo es encontrar los coeficientes β que minimizan la siguiente función objetivo:''')
st.latex(r'''
    min ||y - X * β||²
    ''')
st.markdown("""Esta función objetivo se puede resolver utilizando el método de la pseudoinversa o técnicas de álgebra lineal, como la descomposición QR o la descomposición de valores singulares.
        """)
st.markdown("""
        La aproximación discreta de mínimos cuadrados se utiliza en diversas áreas, como el análisis de datos, la regresión lineal, la estimación de parámetros y la construcción de modelos predictivos. Permite encontrar una relación lineal o no lineal entre las variables explicativas y los valores observados, y realizar predicciones basadas en este modelo.
        """)

st.markdown(
    """
    ### Aplicaciones

    La aproximación discreta de mínimos cuadrados tiene diversas aplicaciones en diferentes áreas. Algunas de las aplicaciones más comunes incluyen:

    📌 Regresión lineal: La aproximación discreta de mínimos cuadrados se utiliza para ajustar un modelo lineal a un conjunto de datos observados. Esto permite estimar la relación lineal entre variables y realizar predicciones basadas en el modelo ajustado.

    📌 Estimación de parámetros: La aproximación discreta de mínimos cuadrados se utiliza para estimar los parámetros desconocidos en un modelo matemático. Esto es útil en situaciones en las que se desea encontrar los valores óptimos que se ajustan a los datos observados.

    📌 Análisis de series de tiempo: La aproximación discreta de mínimos cuadrados se aplica en el análisis de series de tiempo para modelar y predecir patrones y tendencias. Permite ajustar un modelo lineal o no lineal a los datos de la serie temporal y realizar pronósticos a futuro.

    📌 Modelado y simulación: La aproximación discreta de mínimos cuadrados se utiliza en el modelado y simulación de sistemas físicos, económicos o sociales. Permite ajustar un modelo a los datos observados y utilizarlo para realizar simulaciones y análisis de sensibilidad.

    📌 Reconstrucción de imágenes: La aproximación discreta de mínimos cuadrados se utiliza en la reconstrucción de imágenes a partir de datos observados. Permite aproximar una imagen a partir de una serie de mediciones o muestras, lo cual es útil en áreas como la tomografía computarizada y la reconstrucción de imágenes médicas.

    Estas son solo algunas de las aplicaciones más comunes de la aproximación discreta de mínimos cuadrados. 
    """
) 
 
st.markdown('''
    ### Ejemplos
''') 
st.video("https://www.youtube.com/watch?v=rzv7V8vu3qg")

st.markdown('''🟣 Otro ejemplo matemático de la aproximación discreta de mínimos cuadrados se puede ilustrar mediante la aproximación de una función lineal a un conjunto de puntos.

Supongamos que tienes los siguientes puntos:

(1, 2), (2, 4), (3, 5), (4, 7), (5, 8)

Queremos encontrar una línea que se ajuste mejor a estos puntos utilizando la aproximación discreta de mínimos cuadrados.

Para esto, consideramos el modelo lineal:

y = mx + b

Donde "m" es la pendiente de la línea y "b" es el término independiente.

Nuestro objetivo es encontrar los valores de "m" y "b" que minimicen la suma de los errores cuadráticos entre los valores observados y los valores predichos por el modelo.

Usando la aproximación discreta de mínimos cuadrados, podemos escribir el sistema de ecuaciones:

Σy = n*b + Σx * m

Σxy = Σx*b + Σx² * m

Donde Σ representa la suma de los valores correspondientes.

Resolviendo este sistema de ecuaciones, podemos obtener los valores estimados de "m" y "b" que definen la línea que mejor se ajusta a los puntos.

En este caso, el sistema de ecuaciones sería:

5 = 5b + 15m

27 = 15b + 55m

Resolviendo este sistema de ecuaciones, obtendríamos los valores de "m" y "b" que definen la línea de mejor ajuste.

Una vez obtenidos los valores de "m" y "b", podemos usarlos para predecir los valores de "y" correspondientes a otros valores de "x" y evaluar la calidad de la aproximación.

Recuerda que este es solo un ejemplo básico de la aproximación discreta de mínimos cuadrados para una función lineal. El método se puede extender a modelos más complejos, como polinomios de mayor grado o funciones no lineales, ajustando los coeficientes correspondientes.''')
st.markdown(
    """
    ### Código
    """
) 
import streamlit as st

code = '''import numpy as np

def least_squares_approximation(X, y):
    """
    Realiza la aproximación discreta de mínimos cuadrados para ajustar un modelo a un conjunto de datos.
    
    Parámetros:
        - X: matriz de diseño que contiene las variables explicativas.
        - y: vector de valores observados.
        
    Retorna:
        - Los coeficientes del modelo ajustado.
    """
    coefficients = np.linalg.lstsq(X, y, rcond=None)[0]  # Ajuste de mínimos cuadrados
    
    return coefficients

# Variables explicativas (matriz de diseño)
X = np.array([[1, 2], [1, 3], [1, 4], [1, 5]])

# Valores observados
y = np.array([3, 4, 6, 8])

# Aproximación discreta de mínimos cuadrados
coefficients = least_squares_approximation(X, y)
print("Coeficientes del modelo ajustado:", coefficients)


'''
st.code(code, language='python')