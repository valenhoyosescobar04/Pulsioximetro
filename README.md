# Sistema de Pulsioximetro

Este proyecto implementa un sistema para monitorear y visualizar en tiempo real el nivel de oxigeno en la sangre y el ritmo cardiaco.

## Características

- **Simulación de Sensores**: Tres sensores virtuales que generan datos de nivel de oxigeno en la sangre y frecuencia cardiaca en tiempo real y los envían a una API basada en Flask.
- **Almacenamiento Centralizado**: Gestión de los datos simulados en una base de datos organizada para acceso eficiente.
- **Visualización Interactiva**: Gráficos dinámicos de líneas generados con `Chart.js` y tablas interactivas con opciones de filtrado por fecha y sensor.
- **Gráficos en Python**: Uso de `matplotlib` para representar los datos simulados de forma detallada.

## Tecnologías Utilizadas

- **Backend**: Python, Flask.
- **Frontend**: HTML, CSS, Chart.js.
- **Simulación y Gráficos**: Python (`matplotlib`, `requests`).
- **Base de Datos**: Servidor central para la gestión de datos.

## Requisitos

Asegúrate de tener instalado:

- Python 3.8 o superior.
- Las dependencias especificadas en `requirements.txt`.

## Instalación

1. Instala los requisitos mencionados en el archivo `requirements.txt`.
2. Ejecuta el archivo `app.py` para iniciar el servidor.
3. Abre el dominio \texttt{http://127.0.0.1:5000} en un navegador web.