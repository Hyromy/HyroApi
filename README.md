# HyroApi
API REST desarrollada con [Django](https://www.djangoproject.com) y [DRF](https://www.django-rest-framework.org) pensada para funcionar en [Render](https://render.com)

_HyroApi es sub-proyecto auxiliar de HyroBot._

## Requisitos
- Python 3.12
- pip

## Estructura del proyecto
Se tiene la estructura de un proyecto típico de Django

```sh
app/                   # aplicación principal
project/               # configuración del proyecto
tkn/                   # tokens y autenticación
create_superuser.py    # script de creación de un super usuario
manage.py              # script de gestión de Django
requirements.txt       # dependencias
```

## Variables de entorno
Aunque el proyecto funciona de manera local sin establecer el `.env`, a continuación se detallan las variables necesarias:

```sh
# Super usuario de la api
API_USER="nombre del super usuario de la api"
API_PASS="contraseña del super usuario"

# Configuración de la base de datos
DB_HOST="host de la db"                   # entorno productivo
DB_PORT="puerto de la db"                 # entorno productivo
DB_NAME="nombre de la db"                 # entorno productivo
DB_USER="usuario de la db"                # entorno productivo
DB_PASS="contraseña de la db"             # entorno productivo
    
# Claves de Django y render
SECRET_KEY="llave secreta de django"
PYTHON_VERSION=3.12.X                     # para despliegue en render.com    
```

> [!NOTE]
> EN caso de no declarar `API_USER` y `API_PASS` al ejecutar [build.sh](build.sh) se crea un [super usuario](create_superuser.py) con el usuario y la contraseña de `admin`

## Instalación
1. Crear y activar un entorno virtual:
    ```sh
    python -m venv env
    env\Scripts\activate  # Windows
    ```

2. Preparar el despliegue:
    1. Automático
        ```sh
        sh build.sh
        ```

    2. Manual
        ```sh
        pip install -r requirements         # instalación de dependencias
        python manage.py migrate            # aplicar migraciones
        python manage.py createsuperuser    # creación del super usuario
        ```    

## Despliegue
### Local
El proyecto se ejecuta en el puerto 8000, pero opcionalmente se puede especificar uno en `(port)`
```sh
python manage.py runserver (port)
```

### Productivo (Render)
1. Configuración general
    
    En el panel de Render, configurar las siguientes claves:
    - **Build Command**: `./build.sh`
    - **Start Command**: `gunicorn project.wsgi`

2. Variables de entorno

    Cargar el archivo [.env](#variables-de-entorno) con todas sus claves y valores configuradas

## Licencia
[Licencia MIT](LICENSE)
