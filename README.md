# Feedback-Classifier
Agente IA que realiza un análisis automático para clasificar, resumir y detectar patrones en feedback textual proveniente de múltiples fuentes (WhatsApp, formulario web, encuestas), clasifica el feedback en categorías y sentimiento para priorizar mejoras y presenta los insights en un dashboard interactivo.



🛠️ Tecnologías y Componentes del Proyecto
El proyecto se divide en dos servicios principales dockerizados:

1. Backend (API - FastAPI)
Framework: FastAPI

Servidor ASGI: Uvicorn

Base de datos / ORM: SQLite / SQLAlchemy

Machine Learning: PyTorch (torch), NumPy, Transformers / Pipelines de procesamiento de lenguaje natural (NLP).

Utilidades: Generación de reportes y manejo de archivos.

2. Frontend (Dashboard - Streamlit)
Framework visual: Streamlit

Visualización de datos: Plotly / Pandas

Comunicación HTTP: Librería requests para conectar con los endpoints de la API.

📦 Dependencias (requirements.txt)
El proyecto requiere las siguientes librerías principales tanto para el funcionamiento de los modelos de IA como para la interfaz visual:

fastapi

uvicorn

sqlalchemy

pydantic

streamlit

pandas

plotly

requests

torch (versión compatible con CPU)

numpy

⚙️ Cómo Levantar el Proyecto
Tienes dos formas de ejecutar el sistema completo: de manera automática con Docker (recomendado) o de forma manual.

Método 1: Automático con Docker Compose (Recomendado)
Esta opción levanta tanto la API en el puerto 8000 como el Dashboard en el puerto 8501 de forma simultánea.

Asegúrate de tener el puerto 8501 libre (si tenías una instancia previa de Streamlit corriendo, detenla con Ctrl + C).

Ejecuta el siguiente comando en la raíz del proyecto para construir y arrancar los contenedores:

Bash
docker-compose up --build
Una vez iniciados, ve a la pestaña "Ports" (Puertos) de tu entorno de Codespaces para acceder a:

API (Backend): Puerto 8000 (puedes ver la documentación en /docs).

Dashboard (Frontend): Puerto 8501.

Método 2: Manual (Sin Docker)
Si prefieres correr los servicios directamente en tu terminal:

Paso 1: Levantar el Backend (API)
Instala las dependencias del backend:

Bash
pip install -r requirements.txt
Inicia el servidor de FastAPI:

Bash
uvicorn Feedback-Classifier.app.main:app --reload --port 8000
Paso 2: Levantar el Frontend (Dashboard)
Abre una nueva pestaña de terminal en tu entorno.

Instala la librería gráfica si no la tienes:

Bash
pip install plotly
Ejecuta la aplicación de Streamlit apuntando al archivo del dashboard:

Bash
streamlit run Feedback-Classifier/dashboard/app.py --server.port=8501
Abre el puerto 8501 en las opciones de puertos de tu entorno para visualizar la interfaz gráfica.
