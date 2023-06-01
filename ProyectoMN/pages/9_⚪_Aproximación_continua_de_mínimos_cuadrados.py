import streamlit as st

st.title("Aproximación continua de mínimos cuadrados")

st.markdown(
    """
    ### Definición
    La aproximación continua de mínimos cuadrados, también conocida como ajuste de mínimos cuadrados, es un método utilizado para aproximar una función continua a partir de un conjunto de puntos dados, minimizando la suma de los errores cuadráticos entre los puntos y la función aproximada.

    La fórmula general para la aproximación continua de mínimos cuadrados es:
    """
)
st.latex(r'''
   y(x) = a₀ + a₁ * x + a₂ * x² + ... + an * xⁿ
    ''')
st.markdown(
    """Donde: y(x) es la función aproximada, x es la variable independiente,"""

)
st.latex(r'''
    a₀, a₁, a₂, ..., an
    ''')
st.markdown("""son los coeficientes que se determinan para minimizar la suma de los errores cuadráticos.""")

st.markdown('''El procedimiento para obtener los coeficientes en el ajuste de mínimos cuadrados implica el uso de técnicas de álgebra lineal, como la resolución de sistemas de ecuaciones lineales o el método de la pseudoinversa. El objetivo es minimizar la función objetivo:''')
st.latex(r'''
    E(a₀, a₁, a₂, ..., an) = Σ [y(xᵢ) - (a₀ + a₁ * xᵢ + a₂ * xᵢ² + ... + an * xᵢⁿ)]²
    ''')
st.markdown('''Donde (xᵢ, yᵢ) son los puntos conocidos.''')

st.markdown(
    """
    La aproximación continua de mínimos cuadrados se utiliza en diversas áreas, como ajuste de curvas, regresión lineal y no lineal, modelado de datos experimentales y estimación de parámetros en modelos matemáticos.
    """
)

st.image("https://www.researchgate.net/publication/341539870/figure/fig19/AS:893485192323073@1590034878498/Figura-6-Recta-de-aproximacion-por-minimos-cuadrados-de-situacion-precio-y-area-de.ppm")

st.markdown(
    """
    ### Aplicaciones

    La aproximación continua de mínimos cuadrados tiene diversas aplicaciones en diferentes áreas. Algunas de las aplicaciones más comunes incluyen:

    📌 Ajuste de curvas: La aproximación continua de mínimos cuadrados se utiliza para ajustar una curva o una función a un conjunto de puntos de datos. Esto es útil en áreas como el análisis de datos, la modelización matemática y la predicción de tendencias. Por ejemplo, se puede utilizar para ajustar una función polinómica a datos experimentales y obtener una representación matemática de los mismos.

    📌 Regresión lineal: La aproximación continua de mínimos cuadrados se utiliza en la regresión lineal para encontrar la mejor línea recta que se ajuste a un conjunto de datos. Esto permite estimar relaciones lineales entre variables y realizar predicciones basadas en la relación lineal encontrada.

    📌 Regresión no lineal: Además de la regresión lineal, la aproximación continua de mínimos cuadrados se puede utilizar para ajustar modelos no lineales a datos. Esto es útil cuando los datos siguen una forma no lineal y se busca encontrar una función que se ajuste mejor a los datos.

    📌 Análisis de series de tiempo: La aproximación continua de mínimos cuadrados se utiliza en el análisis de series de tiempo para modelar y predecir patrones y tendencias. Se pueden utilizar funciones polinómicas o modelos más complejos para ajustar los datos de la serie temporal y realizar pronósticos a futuro.

    📌 Interpolación de datos: La aproximación continua de mínimos cuadrados se puede utilizar para interpolar datos faltantes o suavizar datos ruidosos. Permite aproximar valores desconocidos entre puntos de datos conocidos y obtener una representación más suave de los datos.

    Estas son solo algunas de las aplicaciones más comunes de la aproximación continua de mínimos cuadrados. La versatilidad de este método y su capacidad para aproximar funciones a partir de datos hacen que sea ampliamente utilizado en diversas áreas de la ciencia, la ingeniería y la estadística.
    """
) 
 
st.markdown('''
    ### Ejemplo
''') 
st.video("https://www.youtube.com/watch?v=6sbccHMUO7Y")

st.markdown(
    """
    ### Código
    """
) 
import streamlit as st

code = '''import numpy as np

def least_squares_approximation(x, y, degree):
    """
    Realiza la aproximación continua de mínimos cuadrados para ajustar un polinomio de grado dado a un conjunto de puntos (x, y).
    
    Parámetros:
        - x: lista de coordenadas x de los puntos conocidos.
        - y: lista de coordenadas y de los puntos conocidos.
        - degree: grado del polinomio de aproximación.
        
    Retorna:
        - Los coeficientes del polinomio de aproximación.
    """
    A = np.vander(x, degree + 1, increasing=True)  # Matriz de Vandermonde
    coefficients = np.linalg.lstsq(A, y, rcond=None)[0]  # Ajuste de mínimos cuadrados
    
    return coefficients

# Puntos conocidos
x_known = [0, 1, 2, 3, 4, 5]
y_known = [2, 3, 5, 8, 11, 14]

# Grado del polinomio de aproximación
degree = 2

# Aproximación continua de mínimos cuadrados
coefficients = least_squares_approximation(x_known, y_known, degree)
print("Coeficientes del polinomio de aproximación:", coefficients)

'''
st.code(code, language='python')