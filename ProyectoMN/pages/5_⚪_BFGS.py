import streamlit as st

st.title("Método BFGS")

st.markdown(
    """
    ### Definición
    El método BFGS (Broyden-Fletcher-Goldfarb-Shanno) es un algoritmo de optimización no lineal utilizado para encontrar mínimos o máximos locales de una función objetivo. Es un método de cuasi-Newton que aproxima la matriz hessiana de la función objetivo mediante actualizaciones iterativas utilizando la información de las derivadas de primer orden.

    El objetivo del método BFGS es encontrar un punto estacionario de una función objetivo, donde el gradiente (vector de derivadas parciales) de la función es igual a cero. El método BFGS utiliza la información del gradiente para aproximar la matriz hessiana, que representa la curvatura de la función objetivo.

    La fórmula del método BFGS para actualizar la aproximación de la matriz hessiana se basa en la fórmula de actualización Broyden-Fletcher-Goldfarb-Shanno. A continuación, se muestra la fórmula general para la actualización de la matriz hessiana en el método BFGS:
    """
)
st.latex(r'''
   H_{k+1} = (I - \rho_k s_k y_k^T) H_k (I - \rho_k y_k s_k^T) + \rho_k s_k s_k^T
    ''')
st.markdown(
    """Donde:"""

)
st.latex(r'''
    H_{k+1}
    ''')
st.markdown('''es la matriz hessiana aproximada en la (k+1)-ésima iteración.''')

st.latex(r'''
    H_k 
    ''')
st.markdown('''es la matriz hessiana aproximada en la k-ésima iteración.''')

st.latex(r'''
    \rho_k
    ''')
st.markdown('''es un coeficiente de actualización que se calcula en función de los vectores.''')

st.latex(r'''
    s_k = x_{k+1} - x_k
    ''')
st.markdown('''es el cambio en la posición del punto en la k-ésima iteración.''')

st.latex(r'''
    y_k = \nabla f_{k+1} - \nabla f_k 
    ''')
st.markdown('''es el cambio en el gradiente de la función objetivo en la k-ésima iteración.''')


st.markdown(
    """
    La fórmula se basa en una aproximación de la matriz hessiana inversa, utilizando información de los cambios en el punto y los gradientes en cada iteración. La matriz hessiana aproximada se actualiza de manera que conserve ciertas propiedades, como la simetría y la definición positiva.

    Es importante tener en cuenta que la fórmula del método BFGS se utiliza en combinación con el algoritmo de actualización de la dirección de búsqueda, que utiliza la matriz hessiana aproximada para calcular la dirección óptima de búsqueda en cada iteración. La fórmula de actualización BFGS permite que la aproximación de la matriz hessiana se ajuste y mejore iterativamente a medida que el algoritmo avanza hacia el mínimo o máximo local.
    """
)

st.markdown(
    """
    ### Aplicaciones

    El método BFGS (Broyden-Fletcher-Goldfarb-Shanno) tiene una amplia gama de aplicaciones en diversas áreas. Algunas de las aplicaciones comunes del método BFGS son las siguientes:

    ◻️ Optimización no lineal: El método BFGS se utiliza para encontrar mínimos o máximos locales de funciones no lineales. Es especialmente útil en problemas de optimización sin restricciones, donde se requiere encontrar valores óptimos para múltiples variables.

    ◻️ Ajuste de curvas y superficies: El método BFGS se utiliza en el ajuste de curvas y superficies, donde se busca encontrar la mejor aproximación a un conjunto de datos mediante una función paramétrica. Puede ayudar a encontrar los parámetros óptimos que minimicen la diferencia entre los datos observados y la función ajustada.

    ◻️ Modelado de sistemas físicos: El método BFGS se aplica en la modelización de sistemas físicos, como la dinámica de partículas o la mecánica de fluidos. Puede utilizarse para encontrar el equilibrio o la configuración óptima de un sistema físico en función de variables de entrada y condiciones iniciales.

    ◻️ Diseño de estructuras: El método BFGS se utiliza en el diseño de estructuras y optimización estructural. Puede ayudar a encontrar la distribución de materiales óptima que minimice el peso o maximice la resistencia de una estructura dada ciertas restricciones.

    ◻️ Análisis de datos y minería de datos: El método BFGS se utiliza en análisis de datos y minería de datos para encontrar relaciones y patrones en grandes conjuntos de datos. Puede ayudar a encontrar los parámetros óptimos en modelos estadísticos o de machine learning para ajustarse a los datos y realizar predicciones precisas.

    Estas son solo algunas de las muchas aplicaciones del método BFGS. Debido a su eficiencia y capacidad para encontrar soluciones óptimas en problemas no lineales, el método BFGS es ampliamente utilizado en campos como la ciencia, la ingeniería, la economía y otros ámbitos donde la optimización de funciones es fundamental.
    """
) 
 
st.markdown('''
    ### Ejemplos
''') 

st.image                   ("https://dlegorreta.files.wordpress.com/2015/03/funcic3b3n_rosenbrock.jpeg")

st.video("https://www.youtube.com/watch?v=mRo-NUGYZ9w")

st.markdown(
    """
    ### Código
    """
) 
import streamlit as st

code = '''import numpy as np

def bfgs_method(objective, gradient, x0, max_iterations=100, epsilon=1e-6):
    n = len(x0)
    H = np.eye(n)  # Aproximación inicial de la matriz hessiana

    for _ in range(max_iterations):
        g = gradient(x0)
        if np.linalg.norm(g) < epsilon:
            break

        p = -np.dot(H, g)  # Dirección de búsqueda

        alpha = line_search(objective, gradient, x0, p)  # Tamaño de paso mediante una búsqueda de línea

        x1 = x0 + alpha * p  # Nuevo punto

        s = x1 - x0
        y = gradient(x1) - g

        Hy = np.dot(H, y)

        # Actualización de la matriz hessiana
        H = H + np.outer(s, s) / np.dot(s, y) - np.outer(Hy, Hy) / np.dot(y, Hy)

        x0 = x1

    return x0

def line_search(objective, gradient, x, p, alpha=1.0, rho=0.9, c=1e-4):
    # Búsqueda de línea utilizando el método de Armijo
    f0 = objective(x)
    g0 = np.dot(gradient(x), p)
    alpha *= c

    while objective(x + alpha * p) > f0 + alpha * c * g0:
        alpha *= rho

    return alpha

'''
st.code(code, language='python')