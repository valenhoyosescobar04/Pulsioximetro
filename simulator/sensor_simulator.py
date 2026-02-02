import random
import time
import requests
import threading
import matplotlib.pyplot as plt
from collections import deque

# Configuración de la API y sensores
API_URL = "http://127.0.0.1:5000/recibir"
INTERVALO_DATOS = 5  # Intervalo de envío en segundos

# Generar IDs de los sensores para tres personas
PERSONAS = ["Persona1", "Persona2", "Persona3", "Persona4"]
SENSORES = [f"PULSIOXI_{i+1}" for i in range(4)]

# Datos en tiempo real para graficar
datos_oxigeno = {persona: deque(maxlen=100) for persona in PERSONAS}
datos_ritmo = {persona: deque(maxlen=100) for persona in PERSONAS}
tiempos = deque(maxlen=100)

# Función para simular datos de un pulsioxímetro y enviarlos a la API
def simulate_sensor_data(persona, idsensor):
    print(f"Iniciando simulación para {persona}")
    while True:
        nivel_oxigeno = round(random.uniform(100, 150), 2)
        ritmo_cardiaco = round(random.uniform(80, 160), 2)

        print(f"{persona}: Generado Oxígeno={nivel_oxigeno}, Ritmo={ritmo_cardiaco}")

        # Enviar datos a la API
        registro = {
            "idsensor": idsensor,
            "oxigeno": nivel_oxigeno,
            "ritmo": ritmo_cardiaco
        }

        try:
            response = requests.post(API_URL, json=registro)
            if response.status_code == 201:
                print(f"Datos enviados exitosamente para {persona}: {response.json()}")
            else:
                print(f"Error al enviar datos para {persona}: {response.text}")
        except Exception as e:
            print(f"Error de conexión para {persona}: {e}")

        # Agregar datos a las colas para graficar
        datos_oxigeno[persona].append(nivel_oxigeno)
        datos_ritmo[persona].append(ritmo_cardiaco)

        time.sleep(INTERVALO_DATOS)

# Función para graficar en tiempo real los datos simulados
def graficar_biometricos():
    plt.ion()  # Activa el modo interactivo
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    while True:
        print("Actualizando gráfica...")  # Confirmación de actualización
        ax1.clear()
        ax2.clear()
        
        for persona in PERSONAS:
            print(f"Datos actuales de oxígeno para {persona}: {list(datos_oxigeno[persona])}")
            print(f"Datos actuales de ritmo para {persona}: {list(datos_ritmo[persona])}")
            ax1.plot(range(len(datos_oxigeno[persona])), datos_oxigeno[persona], label=f"{persona} - Oxígeno")
            ax2.plot(range(len(datos_ritmo[persona])), datos_ritmo[persona], label=f"{persona} - Ritmo")

        # Configuración de los ejes de la gráfica de oxígeno
        ax1.set_title("Nivel de Oxígeno en Sangre (SpO2)")
        ax1.set_xlabel("Tiempo")
        ax1.set_ylabel("Saturación (%)")
        ax1.set_ylim(90, 101)
        ax1.legend(loc="upper right")

        # Configuración de los ejes de la gráfica de ritmo cardíaco
        ax2.set_title("Ritmo Cardíaco (ECG Simulado)")
        ax2.set_xlabel("Tiempo")
        ax2.set_ylabel("Ritmo (lpm)")
        ax2.set_ylim(50, 120)
        ax2.legend(loc="upper right")

        # Pausa para actualizar la gráfica
        plt.pause(0.1)

# Ejecutar simulación de sensores y graficar
if __name__ == "__main__":
    # Crear un hilo para cada persona que simula datos
    for i, persona in enumerate(PERSONAS):
        threading.Thread(target=simulate_sensor_data, args=(persona, SENSORES[i]), daemon=True).start()
    
    # Ejecutar la gráfica en el hilo principal
    graficar_biometricos()
