# Importar la biblioteca os para acceder a las variables de entorno
import os 
# Cargar el archivo .env usando la biblioteca dotenv que lee y transforma las variables de entorno definidas en el archivo .env en variables de entorno del sistema operativo
from dotenv import load_dotenv

load_dotenv()

# Definir la clase Config que contendrá la configuración de la aplicación
class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    # Configurar la URI de la base de datos utilizando las variables de entorno definidas en el archivo .env
    SQLALCHEMY_DATABASE_URI = ( 
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

