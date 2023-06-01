import streamlit as st

st.title("Derivación Númerica")

st.markdown(
    """
    ### Definición
    La derivación numérica es una técnica que se utiliza para aproximar la derivada de una función en un punto utilizando métodos computacionales. Estos métodos son útiles cuando no se dispone de una fórmula analítica para la función o cuando calcular la derivada analítica es difícil o costoso.

    Existen diferentes fórmulas utilizadas en la derivación numérica para aproximar la derivada de una función en un punto dado. Aquí se presentan algunas de las fórmulas más comunes:
    
    -Diferencias finitas hacia adelante:
    """
)
st.latex(r'''
   f'(x) ≈ (f(x + h) - f(x)) / h
    ''')
st.markdown(
    """Esta fórmula se basa en la aproximación de la derivada utilizando la pendiente de una línea secante entre dos puntos cercanos, donde "h" es un pequeño incremento en la variable "x"."""

)

st.markdown(
    """-Diferencias finitas hacia atrás:"""

)
st.latex(r'''
   f'(x) ≈ (f(x) - f(x - h)) / h
    ''')
st.markdown(
    """Al igual que en la fórmula hacia adelante, esta fórmula aproxima la derivada utilizando la pendiente de una línea secante entre dos puntos cercanos, pero en este caso se utiliza un punto ligeramente menor que "x"."""

)

st.markdown(
    """-Diferencias finitas centradas:"""

)
st.latex(r'''
   f'(x) ≈ (f(x + h) - f(x - h)) / (2h)
    ''')
st.markdown(
    """Esta fórmula aproxima la derivada utilizando la pendiente de una línea secante que pasa por dos puntos simétricos respecto al punto "x"."""

)
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Derivative.png/250px-Derivative.png")


st.markdown(
    """
    ### Aplicaciones

    La derivación numérica tiene una amplia gama de aplicaciones en diversas áreas. Algunas de las aplicaciones comunes de la derivación numérica incluyen:

    💾 Análisis de datos: La derivación numérica se utiliza en el análisis de datos para calcular la tasa de cambio de una función en puntos específicos. Esto puede ser útil para comprender patrones de cambio y tendencias en conjuntos de datos.

    💾 Optimización numérica: La derivación numérica se utiliza en problemas de optimización, donde se busca encontrar el valor óptimo de una función. Los métodos de optimización a menudo requieren cálculos de derivadas para guiar la búsqueda del valor óptimo.

    💾 Cálculo de velocidades y aceleraciones: La derivación numérica se utiliza en problemas de cinemática para calcular velocidades y aceleraciones a partir de datos de posición. Esto es útil en áreas como la mecánica, la física de partículas y la animación por computadora.

    💾 Ajuste de curvas: La derivación numérica se utiliza en el ajuste de curvas para encontrar la mejor aproximación de una función a un conjunto de datos. Ayuda a determinar la pendiente y la concavidad de la función en puntos específicos.

    💾 Procesamiento de imágenes: En el campo del procesamiento de imágenes, la derivación numérica se utiliza para calcular gradientes de intensidad en imágenes. Esto puede ayudar en tareas como detección de bordes, segmentación y mejora de imágenes.

    Estas son solo algunas de las muchas aplicaciones de la derivación numérica. En general, cualquier problema que requiera conocer la tasa de cambio instantánea de una función en un punto dado puede beneficiarse de la derivación numérica. Es una herramienta fundamental en el análisis numérico y desempeña un papel crucial en muchos campos científicos y de ingeniería.
    """
) 
 
st.markdown('''
    ### Ejemplos
''') 

st.image                   ("https://arturoguillen90.files.wordpress.com/2014/06/derivacionnumerica02.png?w=625&h=429")

st.video("https://www.youtube.com/watch?v=5nRYIPCUYTA")

st.markdown(
    """
    ### Código
    """
) 
import streamlit as st

code = '''def f(x):
    return x**2  # Ejemplo de función cuadrática

x = 1.5  # Punto en el cual se evalúa la derivada
h = 0.001  # Incremento utilizado en la fórmula de diferencias finitas

derivada = forward_difference(f, x, h)
print("La derivada en el punto", x, "es:", derivada)

'''
st.code(code, language='python')