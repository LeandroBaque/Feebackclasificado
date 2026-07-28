# Feedback-Classifier
Agente IA que realiza un análisis automático para clasificar, resumir y detectar patrones en feedback textual proveniente de múltiples fuentes (WhatsApp, formulario web, encuestas), clasifica el feedback en categorías y sentimiento para priorizar mejoras y presenta los insights en un dashboard interactivo.



Conversación con Gemini
Cuál es entonces?

¡Ya quedó perfecto! Fíjate en tu terminal: ¡El dashboard ya arrancó con éxito! 🎉

Dice claramente:
You can now view your Streamlit app in your browser. y te marca el puerto 8501.

¿Cómo lo abres ahora mismo?
Ve a la pestaña "Ports" (Puertos) en la parte inferior de tu Codespace.

Busca el puerto 8501 (que ahora sí estará activo y parpadeando o disponible).

Haz clic en el icono del globo terráqueo (Open in Browser) o mantén presionado el enlace para abrir tu dashboard interactivo en una pestaña nueva de tu navegador.

Y el link?

Para ver el link del dashboard en Codespaces:

Ve a la barra inferior o al panel lateral de tu entorno y haz clic en la pestaña "Ports" (Puertos).

Busca la fila correspondiente al puerto 8501.

Coloca el cursor sobre la columna "Forwarded Address" o "Local Address" de ese puerto, y verás aparecer un icono con forma de globo terráqueo u opción que dice "Open in Browser" (Abrir en el navegador). Haz clic ahí para abrirlo directamente.

Tu damelo

Como estás dentro de GitHub Codespaces, tu URL única se genera combinando el nombre de tu espacio con el puerto 8501.

Siguiendo el dominio que ya estás usando en tu navegador (...-8000.app.github.dev), solo debes cambiar el 8000 por el 8501.

Prueba abrir directamente este enlace en una nueva pestaña:

👉 [https://pybara-v6r9pp4xxpr63xq79-8501.app.github.dev](https://pybara-v6r9pp4xxpr63xq79-8501.app.github.dev)

Así me sale el dashboard

El error es porque falta instalar el paquete de gráficos plotly en tu entorno de terminal.

Ejecuta este comando rápido para instalarlo:

Bash
pip install plotly
Una vez que termine la instalación, recarga la página del dashboard en tu navegador y ya cargará correctamente.

Oye porque cuando clonó con git clone un repositorio en Github no se abre la carpeta de los archivos en Github donde lo clone?

Cuando clonas un repositorio con git clone, lo que haces es descargar los archivos dentro de una nueva carpeta en tu terminal, pero tu editor (como VS Code) sigue posicionado en la carpeta anterior donde estabas trabajando. Por eso no se abre automáticamente en pantalla.

Para solucionarlo y empezar a trabajar con el proyecto dentro de tu entorno, tienes que entrar a la carpeta recién clonada y abrirla:

Entra a la carpeta del proyecto:

Bash
cd nombre-del-repositorio
(Sustituye nombre-del-repositorio por el nombre exacto de la carpeta que se acaba de descargar).

Si estás usando VS Code o Codespaces y quieres abrirla por completo:

Bash
code .
Este comando recarga tu editor para que apunte directamente a la nueva carpeta con todos sus archivos listos.

Osea la subí a guthub pero no sé abre está subida en mi github

Cuando subes un repositorio a GitHub usando git push, los archivos se guardan y se quedan almacenados en los servidores de GitHub en la nube, pero tu entorno actual de trabajo (como tu terminal o editor local) no se cambia automáticamente a esa nueva página web. Sigue mostrando tu editor local.

Para ver tu proyecto ya subido y verificado en la plataforma web de GitHub, tienes dos opciones:

Abrir el enlace directamente desde la terminal: Muchos entornos o extensiones te permiten hacer clic directo sobre el enlace de tu repositorio (que suele aparecer en la misma terminal tras hacer el git push) para abrirlo en el navegador.

Entrar manualmente a tu perfil: Ve a github.com, inicia sesión en tu cuenta, haz clic en tu foto de perfil, selecciona "Repositories" (Repositorios) y allí verás listado el proyecto que acabas de subir listo para explorarlo.

ModuleNotFoundError: No module named 'plotly'

Traceback:

File "/workspaces/Feebackclasificado/Feedback-Classifier/dashboard/app.py", line 7, in <module>

import plotly.express as px

Ejecuta el siguiente comando en tu terminal para instalar el módulo que falta y solucionar el error de Streamlit:

Bash
pip install plotly
Una vez que finalice la instalación, recarga la pestaña de tu navegador en el puerto 8501 y el dashboard cargará sin problemas.

@LeandroBaque ➜ /workspaces/Feebackclasificado (main) $ docker-compose up --build

[+] Building 356.3s (25/25) FINISHED

 => [internal] load local bake definitions                                                     0.0s

 => => reading from stdin 1.00kB                                                               0.0s

 => [dashboard internal] load build definition from Dockerfile.dashboard                       0.1s

 => => transferring dockerfile: 793B                                                           0.0s

 => [api internal] load build definition from Dockerfile.backblaze                             0.1s

 => => transferring dockerfile: 1.00kB                                                         0.0s

 => [api internal] load metadata for docker.io/library/python:3.11-slim                        0.5s

 => [auth] library/python:pull token for registry-1.docker.io                                  0.0s

 => [dashboard internal] load .dockerignore                                                    0.0s

 => => transferring context: 2B                                                                0.0s

 => [dashboard internal] load build context                                                    0.1s

 => => transferring context: 54.59kB                                                           0.0s

 => [api 1/8] FROM docker.io/library/python:3.11-slim@sha256:db3ff2e1800a8581e2c48a27c3995339  3.3s

 => => resolve docker.io/library/python:3.11-slim@sha256:db3ff2e1800a8581e2c48a27c3995339d47b  0.0s

 => => sha256:c89b9f64c028c19ba92e195d7589d914b9cd1fc69f3c3dfeb931e93876ac2064 248B / 248B     0.0s

 => => sha256:6b265b8eae4a26a263eb55546aa430c1eef37032a7cd86393d98c6b779f28 14.42MB / 14.42MB  1.0s

 => => sha256:062e450697faa5f02a3a74eba9864ee4d79bc9cfbd65769fc6cdff2c05c6a 29.78MB / 29.78MB  1.0s

 => => sha256:9775d166087aba0afe5ba9a88859c04c08090e82ae218742d09fec9119e0335 1.29MB / 1.29MB  0.2s

 => => extracting sha256:062e450697faa5f02a3a74eba9864ee4d79bc9cfbd65769fc6cdff2c05c6a053      1.2s

 => => extracting sha256:9775d166087aba0afe5ba9a88859c04c08090e82ae218742d09fec9119e0335d      0.1s

 => => extracting sha256:6b265b8eae4a26a263eb55546aa430c1eef37032a7cd86393d98c6b779f28319      0.8s

 => => extracting sha256:c89b9f64c028c19ba92e195d7589d914b9cd1fc69f3c3dfeb931e93876ac2064      0.0s

 => [api internal] load build context                                                          0.1s

 => => transferring context: 54.04kB                                                           0.0s

 => [api 2/8] WORKDIR /app                                                                     2.0s

 => [api 3/8] RUN apt-get update && apt-get install -y curl unzip &&     rm -rf /var/lib/apt/  6.8s

 => [dashboard 4/8] COPY requirements.txt .                                                    0.1s

 => [api 4/8] RUN pip install --no-cache-dir     fastapi uvicorn sqlalchemy pydantic pydanti  16.4s

 => [dashboard 5/8] RUN pip install --no-cache-dir -r requirements.txt     --index-url http  155.4s

 => [api 5/8] RUN pip install --no-cache-dir     "numpy<2.0"     torch==2.1.0+cpu --index-u  101.5s

 => [api 6/8] COPY Feedback-Classifier/app/ ./app/                                             1.7s

 => [api 7/8] COPY Feedback-Classifier/ml_models/ ./ml_models/                                 0.1s

 => [api 8/8] RUN mkdir -p model_files                                                         2.8s

 => [api] exporting to image                                                                 155.5s

 => => exporting layers                                                                      105.1s

 => => exporting manifest sha256:ac05d3cdbcb075f4d2f0064bb787fde8dd38ba0bece9edf371c136aee6aa  0.0s

 => => exporting config sha256:73555692d719a1d635485139aa61759b7c42ec92ceacc3d6392de4949a9a89  0.0s

 => => exporting attestation manifest sha256:d43fe5e911b3c5919e5a82081858b26c844d818c9ae7eb7f  0.0s

 => => exporting manifest list sha256:239a07b984312100a09b037810d62f310a3f7e1144820dcaf864a71  0.0s

 => => naming to docker.io/library/feebackclasificado-api:latest                               0.1s

 => => unpacking to docker.io/library/feebackclasificado-api:latest                           50.0s

 => [dashboard 6/8] COPY Feedback-Classifier/app/ ./app/                                       1.9s

 => [dashboard 7/8] COPY Feedback-Classifier/ml_models/ ./ml_models/                           0.1s

 => [dashboard 8/8] RUN mkdir -p model_files                                                   1.0s

 => [dashboard] exporting to image                                                           184.6s

 => => exporting layers                                                                      141.6s

 => => exporting manifest sha256:213ecae9b66aad71f6685ee1e4bb19365f6e5f042ccdf29140a39c0f14ac  0.0s

 => => exporting config sha256:3852549af8c60da95723fb6ff7699d2f76dd1814e77789e542baac6bece075  0.0s

 => => exporting attestation manifest sha256:edb4d64d142f6c5f54741ca075aeda8dad75bb68c6a91d02  0.0s

 => => exporting manifest list sha256:d0f507c2fc1864d531cb298ec5e9ea0bbb048dfe6d53daae91247c8  0.0s

 => => naming to docker.io/library/feebackclasificado-dashboard:latest                         0.0s

 => => unpacking to docker.io/library/feebackclasificado-dashboard:latest                     42.8s

 => [api] resolving provenance for metadata file                                               0.1s

 => [dashboard] resolving provenance for metadata file                                         0.1s

[+] Running 6/6

 ✔ feebackclasificado-api                    Built                                             0.0s

 ✔ feebackclasificado-dashboard              Built                                             0.0s 

 ✔ Network feebackclasificado_default        Created                                           0.1s 

 ✔ Volume feebackclasificado_model_cache     Create...                                         0.0s

 ✔ Container feebackclasificado-api-1        Created                                           3.6s

 ✔ Container feebackclasificado-dashboard-1  Cre...                                            0.1s

Attaching to api-1, dashboard-1

Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint feebackclasificado-dashboard-1 (f74f4f9f145c7c5491a1e2dec012658435035d087996ccb1e0a532a5e5d30631): failed to bind host port 0.0.0.0:8501/tcp: address already in use que paso aqui que salio mal

El error es muy claro en las últimas líneas: el puerto 8501 ya está ocupado en tu sistema (address already in use).  
Desconocido

Esto pasa porque ya tienes una instancia de Streamlit corriendo en segundo plano (la que levantaste hace un momento con el comando streamlit run desde la terminal) y el contenedor de Docker está intentando usar exactamente el mismo puerto 8501 al mismo tiempo.

Cómo solucionarlo:
Detén el proceso anterior: Ve a la terminal donde dejaste corriendo Streamlit anteriormente y presiona las teclas Ctrl + C para apagarlo.

Vuelve a levantar Docker Compose: Ahora que el puerto 8501 quedó libre, ejecuta de nuevo:

Bash
docker-compose up
(Como ya se construyeron las imágenes, puedes quitar el --build para que arranque rapidísimo).

Una vez hecho esto, el contenedor del dashboard podrá tomar el puerto 8501 sin problemas y se abrirá correctamente desde la pestaña Ports de Codespaces.

comillas dobbles con mensaje gggraficos y metricas listas

Aquí tienes tu mensaje entre comillas dobles (te ajusté el "gggraficos" para que quede bien escrito):

"gráficos y métricas listas"

Si lo que buscas es usarlo para guardar tus cambios en GitHub (hacer un commit), el comando completo para pegar en tu terminal sería:

Bash
git commit -m "gráficos y métricas listas"
Oye ya que sabes todo del proyecto dame un readme bien sustentado de todo lo que se instala lo que se tiene y lo que hay que hacer para que se levanté el backend y el frontened

Aqui tienes una propuesta de README técnico y completo para tu repositorio, estructurado con todo lo que incluye el proyecto, las dependencias y los pasos detallados para levantar tanto el backend (API) como el frontend (dashboard) usando Docker Compose o de forma manual.



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
