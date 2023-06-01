import streamlit as st

st.title("Método de Newton")

st.markdown(
    """
    ### Definición
    El método de Newton, también conocido como el método de Newton-Raphson, es un algoritmo utilizado para encontrar las raíces de una función no lineal. Fue desarrollado por el matemático inglés Sir Isaac Newton y el matemático escocés Joseph Raphson en el siglo XVII.

    El método de Newton se basa en la idea de aproximar la raíz de una función mediante una serie de iteraciones sucesivas. Comienza con una suposición inicial de la raíz y luego utiliza la fórmula iterativa:
    """
)
st.latex(r'''
   x_(n+1) = x_n - f(x_n) / f'(x_n)
    ''')
st.image("https://www.uv.es/~diaz/mn/new-1.gif")
st.markdown(
    """Donde:"""

)
st.latex(r'''
    x_n
    ''')
st.markdown("""es la suposición inicial o la aproximación anterior de la raíz.""")
st.latex(r'''
    f(x_n)
    ''')
st.markdown('''es el valor de la función evaluada''')
st.latex(r'''
    f'(x_n)
    ''')
st.markdown('''es la derivada de la función evaluada ''')

st.markdown(
    """
    El proceso se repite iterativamente, actualizando la aproximación de la raíz en cada paso hasta que se alcance una precisión deseada o se cumpla un criterio de convergencia establecido.

    El método de Newton es eficiente y converge rápidamente hacia la raíz deseada, especialmente cuando se elige una suposición inicial cercana a la raíz real. Sin embargo, puede tener problemas de convergencia si la función es altamente no lineal, si hay múltiples raíces cercanas o si la suposición inicial está lejos de la raíz. En tales casos, se pueden utilizar variantes del método de Newton o se pueden aplicar otros métodos numéricos para encontrar las raíces de la función.
    """
)

st.markdown(
    """
    ### Aplicaciones

    Este método se utiliza en una amplia variedad de aplicaciones en campos como matemáticas, física, ingeniería y ciencias computacionales. Algunas de las aplicaciones más comunes del método de Newton son:

    ◻️ Resolución de ecuaciones no lineales: El método de Newton es ampliamente utilizado para encontrar las raíces de ecuaciones no lineales. Puede ser utilizado para resolver ecuaciones algebraicas, ecuaciones trascendentales o sistemas de ecuaciones.

    ◻️ Optimización: El método de Newton se puede utilizar para encontrar los mínimos o máximos de una función. Al aplicar el método de Newton a la derivada de una función, se puede encontrar el punto crítico de la función y determinar si es un mínimo o máximo.

    ◻️ Interpolación polinómica: El método de Newton se puede utilizar para realizar interpolación polinómica de puntos dados. A partir de un conjunto de puntos, se puede construir un polinomio de Newton que pase a través de esos puntos.

    ◻️ Ajuste de curvas: El método de Newton se puede utilizar en el ajuste de curvas para encontrar la mejor aproximación polinómica a un conjunto de datos. Se puede utilizar para encontrar los coeficientes de un polinomio que mejor se ajuste a los datos.

    ◻️ Resolución de sistemas de ecuaciones: El método de Newton se puede utilizar para resolver sistemas de ecuaciones no lineales. Al extender el método a sistemas de ecuaciones, se puede encontrar una solución aproximada a través de iteraciones sucesivas.

    Estas son solo algunas de las aplicaciones más comunes del método de Newton. Su versatilidad y eficiencia lo convierten en una herramienta valiosa en el campo de la computación científica y la resolución de problemas numéricos.
    """
) 
 
st.markdown('''
    ### Ejemplos
''') 

st.image                   ("https://metododenewton.files.wordpress.com/2010/04/11.jpg")

st.video("https://www.youtube.com/watch?v=8MtnDnnULPc")

st.markdown(
    """
    ### Código
    """
) 
import streamlit as st

code = '''def newton_method(f, f_prime, x0, tol, max_iter):
    Implementación del método de Newton para encontrar la raíz de una función.
    
    Args:
        f: La función objetivo.
        f_prime: La derivada de la función objetivo.
        x0: Aproximación inicial.
        tol: Tolerancia para la convergencia.
        max_iter: Número máximo de iteraciones permitidas.
    
    Returns:
        La aproximación de la raíz encontrada.
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fx) < tol:
            return x  # Se alcanzó la convergencia
        x = x - fx / fpx
    return x  # Se alcanzó el número máximo de iteraciones sin convergencia
'''
st.code(code, language='python')