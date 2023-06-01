import streamlit as st

st.title("Integración Númerica")

st.markdown(
    """
    ### Definición
    
    La integración numérica es una técnica utilizada para aproximar el valor de una integral definida de una función utilizando métodos computacionales. Esta técnica es útil cuando no se puede obtener una solución analítica exacta de la integral o cuando calcularla analíticamente es difícil o costoso.

    Existen varios métodos de integración numérica, siendo los más comunes:
    
    ※ Regla del trapecio:
    
    La regla del trapecio aproxima el valor de una integral utilizando la suma de áreas de trapecios formados por los puntos de la función evaluados en intervalos igualmente espaciados. La fórmula general para la regla del trapecio es:
    """
)
st.latex(r'''
   ∫[a, b] f(x) dx ≈ (h/2) * [f(a) + 2f(x₁) + 2f(x₂) + ... + 2f(xₙ-1) + f(b)]
    ''')
st.markdown(
    """Donde "a" y "b" son los límites de integración, "n" es el número de intervalos y "h" es la longitud de cada intervalo."""

)

st.markdown(
    """※ Regla de Simpson:"""

)

st.markdown(
    """La regla de Simpson aproxima el valor de una integral utilizando la suma de áreas de segmentos curvos (generalmente parábolas) formados por puntos de la función evaluados en intervalos igualmente espaciados. La fórmula general para la regla de Simpson es:"""
)
st.latex(r'''
   ∫[a, b] f(x) dx ≈ (h/3) * [f(a) + 4f(x₁) + 2f(x₂) + 4f(x₃) + ... + 4f(xₙ-1) + f(b)]
    ''')
st.markdown(
    """Al igual que en la regla del trapecio, "a" y "b" son los límites de integración, "n" es el número de intervalos y "h" es la longitud de cada intervalo."""

)
st.image("https://upload.wikimedia.org/wikipedia/commons/0/08/NumInt-MC.png")


st.markdown(
    """
    ### Aplicaciones

    La derivación numérica tiene una amplia gama de aplicaciones en diversas áreas. Algunas de las aplicaciones comunes de la derivación numérica incluyen:

    💥 Cálculo de áreas y volúmenes: La integración numérica se utiliza para calcular áreas de regiones y volúmenes de sólidos en geometría y análisis espacial. Por ejemplo, se puede utilizar para calcular el área bajo una curva, el volumen de un sólido de revolución o el área de una superficie irregular.

    💥 Análisis de datos: La integración numérica se utiliza en el análisis de datos para calcular sumas acumulativas y promedios ponderados. Esto es útil para calcular áreas bajo curvas de distribución, estimar valores acumulados de datos o calcular promedios ponderados en series de tiempo.

    💥 Estadística: En estadística, la integración numérica se utiliza para calcular probabilidades y funciones de distribución. Se utiliza para calcular áreas bajo curvas de distribución de probabilidad como la normal, la t de Student, la chi-cuadrado, entre otras.

    💥 Finanzas: En el campo de las finanzas, la integración numérica se utiliza para valorar derivados financieros, calcular el valor presente neto de flujos de efectivo futuros y estimar probabilidades de eventos financieros.

    💥 Modelado y simulación: La integración numérica es esencial en el modelado y simulación de sistemas dinámicos. Se utiliza para calcular cambios en variables a lo largo del tiempo y para simular la evolución de sistemas complejos en áreas como la biología, la economía, la dinámica de fluidos, entre otros.

    Estas son solo algunas de las muchas aplicaciones de la integración numérica. En general, cualquier problema que requiera calcular el área bajo una curva, el volumen de un sólido o sumas acumulativas puede beneficiarse de la integración numérica. Es una herramienta esencial en el análisis numérico y desempeña un papel crucial en muchos campos científicos, de ingeniería y de análisis de datos.
    """
) 
 
st.markdown('''
    ### Ejemplo
''') 
st.video("https://www.youtube.com/watch?v=Vqr9hB7d2P4&pp=ygUraW50ZWdyYWNpw7NuIG51bcOpcmljYSBlamVyY2ljaW9zIHJlc3VlbHRvcw%3D%3D")

st.markdown(
    """
    ### Código
    """
) 
import streamlit as st

code = '''import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2

a = 0  # Límite inferior del intervalo
b = 1  # Límite superior del intervalo
n = 4  # Número de intervalos

# Calcular la aproximación de la integral utilizando el método del trapecio
h = (b - a) / n  # Longitud de cada intervalo
x = np.linspace(a, b, n+1)  # Puntos extremos de cada intervalo
y = f(x)  # Valores de la función en los puntos extremos

# Calcular las áreas de los trapecios
areas = h * (y[:-1] + y[1:]) / 2
aprox_integral = np.sum(areas)

# Graficar los trapecios y la función
plt.plot(x, y, 'b', linewidth=2, label='f(x)')
plt.fill_between(x, y, alpha=0.3)
plt.bar(x[:-1], y[:-1], width=h, align='edge', alpha=0.3, edgecolor='k')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Aproximación numérica de la integral')
plt.legend()

# Mostrar la aproximación de la integral en el gráfico
plt.text(0.5, 0.5, f'Aprox. Integral = {aprox_integral:.4f}', fontsize=12, ha='center')

# Mostrar el gráfico
plt.show()


'''
st.code(code, language='python')