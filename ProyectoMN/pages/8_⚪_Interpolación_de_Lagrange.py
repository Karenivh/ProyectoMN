import streamlit as st

st.title("Interpolación de Lagrange")

st.markdown(
    """
    ### Definición
    
    La interpolación de Lagrange es un método utilizado para aproximar una función a través de un polinomio que pasa por un conjunto de puntos dados. Este método se basa en la idea de que dado un conjunto de puntos (x, y), se puede encontrar un polinomio de grado (n-1) que pase exactamente por esos puntos, donde n es el número de puntos dados.
    """
)
st.latex(r'''
   P(x) = y₁ * L₁(x) + y₂ * L₂(x) + ... + yn * Ln(x)
    ''')
st.markdown(
    """Donde:"""

)
st.latex(r'''
     y₁, y₂, ..., yn
    ''')
st.markdown("""son las coordenadas y de los puntos dados,""")
st.latex(r'''
    L₁(x), L₂(x), ..., Ln(x) 
    ''')
st.markdown('''son las funciones de Lagrange y se definen como:''')
st.latex(r'''
    Lk(x) = Π (x - xi) / (xk - xi) para k = 1, 2, ..., n
    ''')
st.markdown('''Aquí, xi son las coordenadas x de los puntos dados. ''')

st.image("https://www.geogebra.org/resource/AxrxHfDa/EzlxuXu5TcZDkrDQ/material-AxrxHfDa.png")
st.markdown(
    """
    El polinomio de Lagrange se utiliza para aproximar el valor de la función en un punto x utilizando los puntos dados. La aproximación se calcula evaluando el polinomio de Lagrange en el punto x.
    """
)

st.markdown(
    """
    ### Aplicaciones

    La interpolación de Lagrange tiene diversas aplicaciones, entre las que se incluyen:

    ◻️ Interpolación de datos: Permite aproximar valores desconocidos entre los puntos dados en una tabla de datos. Esto es útil en problemas de muestreo, estimación de valores faltantes y construcción de curvas suaves a partir de puntos discretos.

    ◻️ Ajuste de curvas: Se utiliza para ajustar un polinomio a un conjunto de puntos, lo que permite representar los datos de manera más concisa y simplificada.

    ◻️ Análisis numérico: Es una herramienta importante para la aproximación de funciones y resolución numérica de ecuaciones diferenciales.

    La interpolación de Lagrange se puede implementar en Python utilizando las fórmulas mencionadas anteriormente. Sin embargo, existen bibliotecas como NumPy y SciPy que ya incluyen funciones para realizar interpolación de Lagrange de manera más eficiente. Estas bibliotecas también ofrecen métodos de interpolación más avanzados, como la interpolación polinómica de Hermite y la interpolación spline cúbica.
    """
) 
 
st.markdown('''
    ### Ejemplos
''') 

st.image                   ("https://arturoguillen90.files.wordpress.com/2014/06/lagrange03.png")

st.video("https://www.youtube.com/watch?v=XWeZ6A3WUxs")

st.markdown(
    """
    ### Código
    """
) 
import streamlit as st

code = '''def lagrange_interpolation(x, y, x_interp):
    """
    Realiza la interpolación de Lagrange para aproximar los valores y_interp en los puntos x_interp,
    utilizando los puntos (x, y) dados.
    
    Parámetros:
        - x: lista de coordenadas x de los puntos conocidos.
        - y: lista de coordenadas y de los puntos conocidos.
        - x_interp: lista de puntos en los que se desea aproximar el valor de la función.
        
    Retorna:
        - Lista de valores y_interp que aproximan la función en los puntos x_interp.
    """
    n = len(x)
    n_interp = len(x_interp)
    y_interp = []
    
    for i in range(n_interp):
        interp_value = 0.0
        
        for j in range(n):
            basis = 1.0
            
            for k in range(n):
                if k != j:
                    basis *= (x_interp[i] - x[k]) / (x[j] - x[k])
            
            interp_value += y[j] * basis
        
        y_interp.append(interp_value)
    
    return y_interp

'''
st.code(code, language='python')