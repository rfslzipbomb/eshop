from app import create_app
from whitenoise import WhiteNoise

# 1. Creamos la aplicación usando la fábrica
app = create_app()

# 2. Configuramos WhiteNoise para que gestione la carpeta static
# 'root' indica dónde están físicamente los archivos
# 'prefix' indica la ruta URL bajo la cual se servirán
app.wsgi_app = WhiteNoise(
    app.wsgi_app, 
    root="app/static/", 
    prefix="static/"
)

# 3. Bloque para desarrollo local
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)