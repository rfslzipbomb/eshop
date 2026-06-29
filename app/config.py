# Importar la biblioteca os para acceder a las variables de entorno
import os 
# Cargar el archivo .env usando la biblioteca dotenv que lee y transforma las variables de entorno definidas en el archivo .env en variables de entorno del sistema operativo
from dotenv import load_dotenv

load_dotenv()

# Definir la clase Config que contendrá la configuración de la aplicación
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Construir ruta absoluta para la base de datos SQLite por defecto
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    default_sqlite = f"sqlite:///{os.path.join(BASE_DIR, 'eshop.db')}"
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', default_sqlite)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

