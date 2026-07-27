
# 🛒 Tienda Virtual — Flask + Jinja2 + MariaDB

## 📋 Descripción

Este proyecto implementa una tienda virtual completa y modular utilizando **Python** con el framework **Flask** para la capa backend, **Jinja2** para el renderizado de vistas HTML, y **MariaDB** como motor de base de datos. 

La arquitectura se basa en **Flask Blueprints** para separar la lógica de la aplicación en módulos independientes, garantizando un código limpio, mantenible y escalable.

---

## 🧰 Tech Stack

| Componente | Tecnología |
| :--- | :--- |
| **Backend / API** | Python, Flask, Flask Blueprints |
| **ORM & Base de Datos** | Flask-SQLAlchemy, MariaDB |
| **Vistas / Renderizado** | Jinja2, Bootstrap 5, jQuery |
| **Migraciones** | `Flask-Migrate` |
| **Gestión de Dependencias** | `venv`, `requirements.txt` |

---

## 🏗 Arquitectura y Módulos

El sistema está diseñado utilizando el patrón de fábrica de aplicaciones (Application Factory) y divide sus responsabilidades en los siguientes módulos principales:

### Autenticación (`auth`)
Maneja el registro de nuevos usuarios, el inicio y cierre de sesión, y el control de acceso a rutas protegidas mediante roles.

### Tienda Pública (`public`)
Gestiona la vista del cliente final. Incluye la navegación por el catálogo de productos, la gestión del carrito de compras y el historial de pedidos de cada cliente.

### Panel de Administración (`admin`)
Interfaz restringida exclusivamente para administradores. Permite la gestión completa (operaciones CRUD) del inventario de productos y categorías, así como la revisión de pedidos y estados de cuenta de los clientes.

### Esquema de Datos (`models`)
Define la estructura relacional de la base de datos (Usuarios, Productos, Categorías, Pedidos) a través de los modelos de SQLAlchemy.

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonación del Repositorio
Clona el repositorio en tu máquina local e ingresa al directorio principal:
```bash
git clone <repo-url> .

```

### 2. Creación y Activación del Entorno Virtual

Es indispensable utilizar un entorno virtual para aislar las dependencias del proyecto y evitar conflictos:

```bash
python3 -m venv venv

# En Linux/Mac:
source venv/bin/activate
# En Windows:
# venv\Scripts\activate

pip install -r requirements.txt

```

### 3. Configuración de Variables de Entorno

Configura las credenciales de conexión creando un archivo `.env` en la raíz del proyecto (puedes tomar como referencia el archivo `.env.example` si existe):

```env
# Configuración base de Flask
SECRET_KEY=tu_clave_secreta_super_segura
FLASK_APP=app/app.py
FLASK_ENV=development

# Credenciales de conexión a MariaDB
DB_USER=root
DB_PASSWORD=tu_contraseña_aqui
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=nombre_de_tu_base_de_datos

```

### 4. Inicialización de la Base de Datos

Asegúrate de que el servidor MariaDB esté ejecutándose. Luego, inicializa las tablas y carga los datos de prueba (categorías y productos iniciales):

```bash
python seed.py

```

> ⚠️ **Nota:** Ejecuta este script únicamente una vez en entornos nuevos para evitar la duplicación de datos iniciales.

---

## 🗄 Gestión de Base de Datos y Migraciones

Todos los cambios posteriores en la estructura de la base de datos (nuevas tablas, columnas, etc.) se manejan de forma segura con `Flask-Migrate`:

### Generar una nueva migración

Tras modificar tus modelos en el código, genera el archivo de control:

```bash
flask db migrate -m "Descripción de los cambios, ej: add user role column"

```

### Aplicar cambios a MariaDB

Ejecuta la actualización para impactar la base de datos:

```bash
flask db upgrade

```

---

## 🎨 Integración del Frontend

### Motor de Plantillas

Las páginas HTML se generan dinámicamente desde el backend utilizando Jinja2, inyectando los datos pasados desde los controladores de cada módulo. Estas vistas se organizan dentro del directorio `app/templates/`.

### Diseño y Comportamiento

Se utiliza Bootstrap 5 vía CDN para el diseño responsivo y el sistema de grillas, complementado con jQuery para interacciones dinámicas en el DOM.

### Recursos Estáticos

Los archivos personalizados, como hojas de estilo (`css/`) e imágenes de productos (`img/`), se almacenan y sirven desde el directorio `app/static/`.

---

## ▶️ Ejecución y Despliegue

### Servidor Local de Desarrollo

Para levantar la aplicación en tu entorno local, asegúrate de tener el entorno virtual activado y ejecuta:

```bash
python app/app.py 
# Alternativa: flask run --host=0.0.0.0 --port=5000

```

### Despliegue en Producción

Para migrar el proyecto a un servidor en la nube, clona el código, configura el archivo `.env` con las credenciales de producción y aplica las migraciones (`flask db upgrade`). Finalmente, sirve la aplicación utilizando un servidor WSGI (como Gunicorn) detrás de un proxy inverso (como Nginx).

---

## 📁 Estructura del Proyecto

```text
├── app/                      # Paquete principal de la aplicación
│   ├── __init__.py           # Configuración (App Factory) y extensiones
│   ├── app.py                # Script de entrada principal
│   ├── config.py             # Configuraciones adicionales
│   ├── models/               # Modelos relacionales SQLAlchemy
│   ├── blueprints/           # Módulos principales (auth, public, admin)
│   ├── templates/            # Vistas Jinja2
│   └── static/               # Recursos (css, img)
├── migrations/               # Historial de versiones de la BD
├── .env.example              # Plantilla para variables de entorno
├── seed.py                   # Script de población de datos iniciales
├── .gitignore                # Reglas de exclusión de Git
└── requirements.txt          # Dependencias de Python

```

---

## 📝 Mantenimiento y Contribución

### Estructura Modular

Si agregas nuevas funcionalidades mayores, considera crear un nuevo Blueprint dentro de `app/blueprints/` en lugar de sobrecargar los controladores existentes.

### Integridad de Datos

Utiliza siempre la herramienta de migraciones para alterar el esquema. Nunca modifiques las tablas de MariaDB directamente desde un cliente SQL.

### Control de Dependencias

Actualiza tu archivo `requirements.txt` ejecutando el comando `pip freeze > requirements.txt` cada vez que instales un nuevo paquete en tu entorno virtual.

```

```
