import os
from dotenv import load_dotenv

load_dotenv(override=True)

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')

    database_url = os.getenv('DATABASE_URL') or os.getenv('SQLALCHEMY_DATABASE_URI')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_name = os.getenv('DB_NAME')

    # Nos aseguramos de que si DATABASE_URL es una cadena vacía "", se trate como None
    if database_url and database_url.strip():
        SQLALCHEMY_DATABASE_URI = database_url.strip()
    elif db_user and db_name:
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"
        )
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, '..', 'app.db')}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    