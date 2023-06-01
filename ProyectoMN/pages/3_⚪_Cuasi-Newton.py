import streamlit as st
st.title("Método de Cuasi-Newton")

st.markdown(
    """
    ### Definición
    El método de cuasi-Newton es una técnica utilizada para encontrar soluciones aproximadas a problemas de optimización no lineal. A diferencia del método de Newton, que requiere calcular y utilizar la matriz hessiana (derivadas parciales de segundo orden) en cada iteración, el método de cuasi-Newton aproxima la matriz hessiana mediante métodos iterativos y actualiza esta aproximación en cada iteración.
    
    La fórmula básica del método de cuasi-Newton para actualizar la aproximación de la matriz hessiana en cada iteración se conoce como "fórmula de actualización de BFGS" (Broyden-Fletcher-Goldfarb-Shanno). 
    """
)
st.latex(r'''
   H_k = H_{k-1} - \frac{H_{k-1}s_{k-1}s_{k-1}^T H_{k-1}}{s_{k-1}^T H_{k-1} s_{k-1}} + \frac{y_{k-1}y_{k-1}^T}{y_{k-1}^T s_{k-1}}
    ''')
st.markdown(
    """Donde:"""

)
st.latex(r'''
    H_k 
    ''')
st.markdown("""es la matriz hessiana aproximada en la iteración.""")
st.latex(r'''
    k, H_{k-1}
    ''')
st.markdown('''es la matriz hessiana aproximada en la iteración.''')
st.latex(r'''
     k-1, s_{k-1}
    ''')
st.markdown('''es el vector de diferencia entre las estimaciones de parámetros en las iteraciones k. ''')

st.latex(r'''
     k-1 (s_{k-1} = x_k - x_{k-1}), y_{k-1}
    ''')
st.markdown('''es el vector de diferencia entre los gradientes de la función objetivo en las iteraciones k y k-1.''')

st.latex(r'''
     (y_{k-1} = \nabla f(x_k) - \nabla f(x_{k-1}))
    ''')
st.markdown('''y T representa la transposición de un vector o matriz.''')

st.markdown(
    """
    Es importante destacar que existen otras variantes y modificaciones del método de cuasi-Newton, como el método L-BFGS, que utiliza una aproximación limitada de la matriz hessiana. Estas variantes pueden tener fórmulas de actualización ligeramente diferentes, pero la fórmula básica de actualización de BFGS es una de las más comunes y ampliamente utilizadas.
    """
)

st.markdown(
    """
    ### Aplicaciones

    El método de cuasi-Newton, específicamente la variante conocida como BFGS (Broyden-Fletcher-Goldfarb-Shanno), es ampliamente utilizado en diversas aplicaciones en campos como la optimización numérica, la ciencia de datos y el aprendizaje automático. Algunas de las aplicaciones más comunes del método de cuasi-Newton son las siguientes:

    💥 Optimización no lineal: El método de cuasi-Newton es utilizado para encontrar mínimos o máximos de funciones no lineales en problemas de optimización. Se aplica en áreas como la optimización de funciones objetivo en algoritmos de aprendizaje automático y la estimación de parámetros en modelos matemáticos complejos.

    💥 Aprendizaje automático: En algoritmos de aprendizaje automático, el método de cuasi-Newton se utiliza para optimizar la función de costo en modelos de regresión logística, redes neuronales y máquinas de vectores de soporte, entre otros. Ayuda a encontrar los parámetros que mejor ajustan los datos y permiten el entrenamiento eficiente de los modelos.

    💥 Ajuste de curvas: El método de cuasi-Newton se utiliza en el ajuste de curvas para encontrar una función que se ajuste a un conjunto de datos. Esto es útil en áreas como la interpolación y la aproximación de datos experimentales o observados.

    💥 Modelado de sistemas físicos: El método de cuasi-Newton se aplica en la resolución numérica de sistemas de ecuaciones diferenciales no lineales que describen fenómenos físicos. Es útil en áreas como la dinámica de fluidos, la mecánica estructural y la simulación de procesos físicos complejos.

    💥 Reconstrucción de imágenes: En el procesamiento de imágenes, el método de cuasi-Newton se utiliza para resolver problemas de reconstrucción de imágenes a partir de datos incompletos o ruidosos. Ayuda a encontrar imágenes que sean coherentes con los datos observados y que cumplan ciertas restricciones.

    Estas son solo algunas de las aplicaciones más comunes del método de cuasi-Newton. Su versatilidad y eficiencia lo convierten en una herramienta poderosa para resolver una amplia gama de problemas de optimización no lineal en diversas áreas de aplicación.
    """
) 
 
st.markdown('''
    ### Ejemplo
''') 
st.video("https://www.youtube.com/watch?v=8MtnDnnULPc")


st.markdown(
    """
    ### Código
    """
) 
import streamlit as st

code = '''import numpy as np

def bfgs_method(f, x0, max_iterations=100, epsilon=1e-6):
    n = len(x0)
    H = np.eye(n)  # Aproximación inicial de la matriz Hessiana inversa
    x = x0.copy()
    
    for _ in range(max_iterations):
        gradient = compute_gradient(f, x)
        if np.linalg.norm(gradient) < epsilon:
            break
        
        direction = -np.dot(H, gradient)
        step_size = backtracking_line_search(f, x, direction, gradient)
        x_new = x + step_size * direction
        
        y = compute_gradient(f, x_new) - gradient
        s = x_new - x
        
        Hy = np.dot(H, y)
        sHy = np.dot(s, Hy)
        
        H = H + np.outer(s, s) / np.dot(s, y) - np.outer(Hy, Hy) / sHy
        x = x_new
    
    return x

# Función de ejemplo: f(x) = x^2 + 2y^2
def f(x):
    return x[0]**2 + 2 * x[1]**2

# Cálculo del gradiente
def compute_gradient(f, x):
    h = 1e-6
    gradient = np.zeros_like(x)
    for i in range(len(x)):
        x_plus_h = x.copy()
        x_plus_h[i] += h
        gradient[i] = (f(x_plus_h) - f(x)) / h
    return gradient

# Búsqueda de línea mediante el método de retroceso (backtracking line search)
def backtracking_line_search(f, x, direction, gradient, alpha=0.4, beta=0.9):
    step_size = 1.0
    while f(x + step_size * direction) > f(x) + alpha * step_size * np.dot(gradient, direction):
        step_size *= beta
    return step_size

# Ejemplo de uso
x0 = np.array([1.0, 1.0])  # Punto inicial
x_opt = bfgs_method(f, x0)

print("Punto óptimo:", x_opt)
print("Valor óptimo:", f(x_opt))

'''
st.code(code, language='python')