import streamlit as st
st.title("Método del spline cúbico")

st.markdown(
    """
    ### Definición
    
    Un spline cúbico es una función definida en intervalos de dominio que están conectados entre sí en los puntos de control. En cada intervalo, el spline cúbico se define mediante una función polinómica de tercer grado, por lo que es suave y tiene derivadas continuas hasta el segundo orden. Esto garantiza una transición suave entre los intervalos adyacentes.

    El método más comúnmente utilizado para la construcción de splines cúbicos es el método de spline cúbico natural. En este enfoque, se establecen condiciones adicionales en los extremos del spline para asegurar una curva suave en los bordes. Estas condiciones adicionales implican que las segundas derivadas en los extremos sean cero, lo que produce un spline suave y natural.

    Para construir un spline cúbico natural, se sigue el siguiente procedimiento:

    -Dados los puntos de control, se divide el dominio en segmentos entre los puntos adyacentes.
    
    -Se calculan los coeficientes de los polinomios de tercer grado para cada segmento utilizando métodos como la interpolación o el método de mínimos cuadrados.
    
    -Se imponen las condiciones de suavidad en los puntos de conexión asegurando que las primeras y segundas derivadas sean continuas.
    
    -Se resuelve el sistema de ecuaciones resultante para obtener los valores de los coeficientes y, por lo tanto, la definición completa del spline cúbico.

    Una vez construido el spline cúbico, se puede utilizar para interpolar o aproximar puntos adicionales dentro del dominio definido por los puntos de control. También es posible evaluar el spline cúbico en cualquier punto dentro del dominio para obtener el valor de la función en ese punto.

    En resumen, los splines cúbicos son una poderosa herramienta matemática utilizada para construir curvas suaves y flexibles a través de un conjunto de puntos de control. Son ampliamente utilizados en gráficos por computadora y otras áreas relacionadas debido a su capacidad para representar curvas realistas y suaves.
    """
)
st.latex(r'''
    S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
    ''')
st.markdown(
    """Donde:"""

)
st.latex(r'''
    a_i, b_i, c_i y d_i 
    ''')
st.markdown("""son coeficientes específicos del intervalo""")
st.latex(r'''
    [x_i, x_{i+1}]
    ''')
st.markdown('''que deben ser calculados para ajustar la curva a los puntos de datos.''')

st.markdown('''x es la variable independiente o el punto en el que se desea evaluar la función spline cúbica.''')

st.markdown('''Para determinar los coeficientes del spline cúbico, se deben satisfacer las siguientes condiciones:''')

st.markdown('''1. Interpolación de los puntos de datos:''')

st.latex(r'''
     S_i(x_i) = y_i y S_i(x_{i+1}) = y_{i+1},
    ''')
st.markdown('''donde''')

st.latex(r'''
     y_i .... y_{i+1} 
    ''')

st.markdown(
    """
    son los valores de los puntos de datos correspondientes.
    """
)

st.markdown('''2. Continuidad en los puntos de interpolación: ''')

st.latex(r'''
     S_i
    ''')

st.markdown(
    """
    ### Aplicaciones

    Los splines cúbicos tienen una amplia gama de aplicaciones en varias áreas, incluyendo:

    💠 Gráficos por computadora: Los splines cúbicos se utilizan para representar curvas suaves en gráficos 2D y 3D, proporcionando una apariencia más realista y suave a las superficies y objetos renderizados.

    💠 Animación: Los splines cúbicos se utilizan para describir trayectorias suaves de animación, como el movimiento de personajes en videojuegos, animaciones en películas y efectos especiales.

    💠 Diseño y modelado de formas: Los splines cúbicos son ampliamente utilizados en diseño gráfico y CAD (diseño asistido por computadora) para modelar formas y curvas suaves, como en el diseño de automóviles, aviones, muebles, productos industriales, entre otros.

    💠 Interpolación y aproximación de datos: Los splines cúbicos se utilizan para interpolar o aproximar conjuntos de datos discretos, permitiendo estimar valores intermedios o suavizar irregularidades en los datos.

    💠 Análisis numérico: Los splines cúbicos son utilizados en métodos numéricos para la resolución de ecuaciones diferenciales y problemas de valor inicial, proporcionando soluciones más precisas y estables.

    Estas son solo algunas de las muchas aplicaciones de los splines cúbicos. Debido a su flexibilidad y capacidad para ajustarse a datos y curvas suaves, los splines cúbicos son una herramienta fundamental en muchas disciplinas científicas y técnicas.
    """
) 
 
st.markdown('''
    ### Ejemplo
''') 
st.video("https://www.youtube.com/watch?v=b1pgaR9Ne9I")

st.image("https://arturoguillen90.files.wordpress.com/2014/06/trazadorescubicos06.png?w=625&h=321")


st.markdown(
    """
    ### Código
    """
) 
import streamlit as st

code = '''import numpy as np
from scipy.interpolate import CubicSpline

# Puntos de datos
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 1, 3, 1, 2])

# Crear objeto CubicSpline
cs = CubicSpline(x, y)

# Puntos para evaluar el spline
x_eval = np.linspace(1, 5, num=100)
y_eval = cs(x_eval)

# Imprimir los valores del spline cúbico evaluado
for i in range(len(x_eval)):
    print(f"S({x_eval[i]}) = {y_eval[i]}")
'''
st.code(code, language='python')