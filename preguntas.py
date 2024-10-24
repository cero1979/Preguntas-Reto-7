



import numpy as np


import matplotlib.pyplot as plt

# Configuración de la simulación
tiempo = np.arange(0, 24, 0.5)  # Intervalo de tiempo de 0 a 24 horas, en pasos de 0.5 horas

# Parámetros del problema
A = 60  # Nivel promedio de ruido en dB
T = 24  # Período de 24 horas

# Definición de desfases para cada zona
desfases = {
    1: -np.pi,  # Ruido máximo a las 12:00 p.m.
    2: np.pi,           # Ruido máximo a las 6:00 p.m.
    3: -np.pi / 3,  # Ruido máximo a las 9:00 a.m.
    4: -np.pi / 4,  # Ruido máximo a las 3:00 p.m.
    5: np.pi        # Ruido máximo a la medianoche
}

# Amplitudes para cada zona
amplitudes = {
    1: 10,  # Ruido máximo a las 12:00 p.m.
    2: 12,  # Ruido máximo a las 6:00 p.m.
    3: 15,  # Ruido máximo a las 9:00 a.m.
    4: 8,   # Ruido máximo a las 3:00 p.m.
    5: 11   # Ruido máximo a la medianoche
}

# Función que modela el ruido en función del tiempo, desfase y un componente aleatorio
def ruido_zona(t, desfase, zona):
    """Función que modela el nivel de ruido en función del tiempo, desfase y un componente aleatorio."""
    return A + amplitudes[zona] * np.sin(2 * np.pi * t / T + desfase) + np.random.normal(0, 3, len(t))

# Función para graficar la función senoidal pura sin perturbación
def senoidal_pura(t, desfase, zona):
    """Función que modela el nivel de ruido ideal, sin perturbación aleatoria."""
    return A + amplitudes[zona] * np.sin(2 * np.pi * t / T + desfase)

# Función para graficar el ruido en la zona seleccionada
def graficar_zona(zona):
    if zona not in desfases:
        print("Zona no válida. Por favor, elige una zona entre 1 y 5.")
        return
    
    desfase = desfases[zona]  # Obtener el desfase para la zona seleccionada
    ruido = ruido_zona(tiempo, desfase, zona)  # Calcular el ruido con perturbación
    ruido_senoidal = senoidal_pura(tiempo, desfase, zona)  # Calcular el ruido sin perturbación
    
    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    
    # Graficar los puntos con perturbación
    plt.scatter(tiempo, ruido, label=f'Zona {zona} (Dato recolectado)', color='blue')
    
    # Graficar la línea continua sin perturbación
    plt.plot(tiempo, ruido_senoidal, label=f'Zona {zona} (Curva Senoidal)', color='red', linestyle='--')
    
    # Configuración del gráfico
    plt.title(f'Simulación del Ruido en la Zona {zona}')
    plt.xlabel('Tiempo (Horas)')
    plt.ylabel('Nivel de Ruido (dB)')
    plt.legend()
    plt.grid(True)
    plt.show()

import numpy as np
from IPython.display import display, Math


# Función que genera preguntas para cada zona
def generar_pregunta(zona):
    if zona not in range(1, 6):
        print("Zona no válida. Por favor, elige una zona entre 1 y 5.")
        return
    
    # Parámetros para la zona seleccionada
    A_zona = A
    B_zona = amplitudes[zona]
    phi_zona = desfases[zona]
    
    # Generación de preguntas específicas para la zona seleccionada
    preguntas = [
        f"1. Interpretación de Parámetros (Nivel Promedio y Amplitud):\n"
        f"Observa la gráfica de la Zona {zona}. Explica qué representan los parámetros A = {A_zona} y B = {B_zona} en términos del nivel promedio y la amplitud del ruido.",

        f"2. Cálculo del Nivel de Ruido en un Momento Específico:",
        Math(f"R(t) = {A_zona} + {B_zona} \\sin\\left( \\frac{{2\\pi t}}{{{T}}} - \\left({round(phi_zona, 2)}\\right) \\right)"),
        "Calcula manualmente el nivel de ruido a las 6:00 a.m. (t = 6 horas).",

        f"3. Momento del Máximo Ruido (Desfase φ):\n"
        f"En la **Zona {zona}**, el ruido máximo ocurre en un horario determinado. ¿Qué valor de φ se utiliza en esta zona y cómo afecta a la hora en que se alcanza el nivel máximo de ruido?",

        f"4. Manipulación de Parámetros (Amplitud):\n"
        f"Si decides aumentar la amplitud de la variación del ruido en la Zona {zona} a B = {B_zona + 5}, ¿cómo esperas que cambie la gráfica? Explica qué pasará con los picos y valles de la onda.",

        f"5. Reescribir la Función en Términos de seno:",
        Math(f"R(t) = {A_zona} + {B_zona} \\cos\\left( \\frac{{2\\pi t}}{{{T}}} - \\left({round(phi_zona + np.pi/2, 2)}\\right) \\right)")
    ]
    
    # Imprimir las preguntas para la zona seleccionada
    for pregunta in preguntas:
        if isinstance(pregunta, Math):
            display(pregunta)
        else:
            print(pregunta)
        print()
