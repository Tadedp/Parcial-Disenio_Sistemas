# API detector de mutantes

Detecta si secuencias de ADN pertenecen a mutantes o humanos: 
- Mediante un **HTTP POST → /mutant/** recibe un array de strings nxn conteniendo una secuencia de ADN (caracteres A,T,C y G unicamente). En caso de verificar un mutante, retorna HTTP 200-OK, en caso contrario un 403-Forbidden. Una persona es identificada como mutante si su ADN contiene más de una secuencia de cuatro letras iguales en cualquier dirección. 
- Mediante un **HTTP GET → /mutant/stats** retorna las estadísticas de las verificaciones de ADN con el formato: {“count_mutant_dna”: int, “count_human_dna”: int, “ratio”: float}

# Ejecución local

## Requisitos previos
- Tener Python 3.9 o superior instalado en tu máquina.
- Tener pip para gestionar las dependencias de Python.
- Tener PostgreSQL instalado y en funcionamiento en tu máquina (o puedes usar un servicio de base de datos en la nube como Render para PostgreSQL).

## Pasos para ejecutar la API localmente
- Clonar o descargar el repositorio.
- Instalar las dependencias (Asegúrate de estar en el directorio raíz del proyecto): 
```
pip install -r requirements.txt
```
- Ejecutar y configurar la base de datos usando un archivo .env, debe tener los siguientes valores:
```
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=mutantes
POSTGRES_USER=user
POSTGRES_PASSWORD=password
```
- Ejecutar la API en directorio app:
```
python main.py
```
# Despliegue en Render

Render es una plataforma de hosting que permite desplegar aplicaciones web de forma sencilla. A continuación, te explicamos cómo desplegar la base de datos y la API en Render.

## Desplegar la base de datos (PostgreSQL)

- Ve a Render y crea una cuenta o inicia sesión.
- En el panel de control, haz clic en New > PostgreSQL.
- Completa el formulario para crear la base de datos, proporcionando un nombre de base de datos, usuario y contraseña. Usa los mismos valores que en tu archivo docker-compose.yaml para que coincidan con la configuración de la API.
- Obtener los detalles de la base de datos: Una vez que la base de datos esté en ejecución, obtendrás una URL de conexión en el panel de Render.
- Actualizar las variables de entorno de la API: En el archivo .env de tu proyecto o en las configuraciones de la API en Render, configura las variables de entorno para que coincidan con la base de datos desplegada.

## Desplegar la API en Render

- En Render, ve a New > Web Service.
- Selecciona el repositorio GitHub del proyecto.
- En los Environment Variables, añade las variables de entorno necesarias para conectar con la base de datos que creaste antes.
- Haz clic en Create Web Service. Render comenzará a construir la API, instalará las dependencias y la ejecutará.
- Una vez que la API esté en ejecución, Render te proporcionará una URL pública para acceder a la API.

# Autores

 - Tadeo Drube - _Developer_ - [Tadedp](https://github.com/Tadedp)  
