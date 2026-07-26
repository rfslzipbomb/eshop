import sys
import os

# Asegura que Python encuentre la carpeta app
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db
from app.models import Usuario, Categoria, Producto

app = create_app()

with app.app_context():
    # 0. Limpiar datos existentes (opcional pero recomendado)
    db.session.query(Producto).delete()
    db.session.query(Categoria).delete()
    db.session.query(Usuario).delete()
    db.session.commit()

with app.app_context():
    # Categorías
    cat_blusas = Categoria(nombre='Blusas', descripcion='Tops, blusas y prendas superiores exclusivas de SIZ')
    cat_chaquetas = Categoria(nombre='Chaquetas', descripcion='Chaquetas, blazers y prendas de abrigo')
    cat_vestidos = Categoria(nombre='Vestidos', descripcion='Vestidos para ocasiones especiales y uso diario')
    cat_ofertas = Categoria(nombre='Ofertas', descripcion='Prendas seleccionadas con precios especiales')

    db.session.add_all([cat_blusas, cat_chaquetas, cat_vestidos, cat_ofertas])
    db.session.commit()

    # Productos
    productos = [
        # --- BLUSAS ---
        Producto(nombre='Top Bliss', precio=19.00, stock=15, categoria_id=cat_blusas.id),
        Producto(nombre='Top Linna', precio=19.00, stock=15, categoria_id=cat_blusas.id),
        Producto(nombre='Top Perla', precio=18.00, stock=15, categoria_id=cat_blusas.id),
        Producto(nombre='Top Glow Aqua', precio=17.00, stock=12, categoria_id=cat_blusas.id),
        Producto(nombre='Dress Shine', precio=18.00, stock=10, categoria_id=cat_blusas.id),
        Producto(nombre='Top Glow', precio=17.00, stock=15, categoria_id=cat_blusas.id),
        Producto(nombre='Top Gala', precio=19.00, stock=15, categoria_id=cat_blusas.id),
        Producto(nombre='Top Bliss White', precio=19.00, stock=12, categoria_id=cat_blusas.id),
        Producto(nombre='Top Perla Pink', precio=18.00, stock=12, categoria_id=cat_blusas.id),
        Producto(nombre='Top Glow Pink', precio=17.00, stock=12, categoria_id=cat_blusas.id),
        Producto(nombre='Top Nova Black', precio=19.00, stock=15, categoria_id=cat_blusas.id),
        Producto(nombre='Top Noir', precio=18.00, stock=12, categoria_id=cat_blusas.id),
        Producto(nombre='Top Belle', precio=19.00, stock=15, categoria_id=cat_blusas.id),
        Producto(nombre='Top Linna Black', precio=19.00, stock=15, categoria_id=cat_blusas.id),
        Producto(nombre='Top Glow Brown', precio=17.00, stock=12, categoria_id=cat_blusas.id),
        Producto(nombre='Top Gala Black', precio=19.00, stock=15, categoria_id=cat_blusas.id),
        Producto(nombre='Top Nova Wine', precio=19.00, stock=12, categoria_id=cat_blusas.id),
        Producto(nombre='Top Velvet', precio=17.00, stock=12, categoria_id=cat_blusas.id),
        Producto(nombre='Top Gala Aqua', precio=19.00, stock=12, categoria_id=cat_blusas.id),
        Producto(nombre='Top Nova White', precio=19.00, stock=12, categoria_id=cat_blusas.id),

        # --- CHAQUETAS ---
        Producto(nombre='Onyx Jacket', precio=30.00, stock=8, categoria_id=cat_chaquetas.id),
        Producto(nombre='Chaqueta Biker Cuerina (Efecto Piel)', precio=35.00, stock=8, categoria_id=cat_chaquetas.id),
        Producto(nombre='Blazer Oversize Elegante', precio=32.00, stock=10, categoria_id=cat_chaquetas.id),
        Producto(nombre='Chaqueta Cropped Trench', precio=28.00, stock=12, categoria_id=cat_chaquetas.id),
        Producto(nombre='Chaqueta Denim Semicrop', precio=26.00, stock=12, categoria_id=cat_chaquetas.id),
        Producto(nombre='Bomber Jacket Satinada', precio=25.00, stock=10, categoria_id=cat_chaquetas.id),

        # --- VESTIDOS ---
        Producto(nombre='Vestido Sparkle Glitz', precio=32.00, stock=8, categoria_id=cat_vestidos.id),
        Producto(nombre='Vestido Silk Romance', precio=28.00, stock=10, categoria_id=cat_vestidos.id),
        Producto(nombre='Vestido Bodycon Chic', precio=24.00, stock=12, categoria_id=cat_vestidos.id),
        Producto(nombre='Vestido Cozy Long Sleeve', precio=22.00, stock=12, categoria_id=cat_vestidos.id),
        Producto(nombre='Vestido Night Aura', precio=29.00, stock=10, categoria_id=cat_vestidos.id),

        # --- OFERTAS ---
        Producto(nombre='Blusa Asymmetric Muse', precio=19.00, stock=15, categoria_id=cat_ofertas.id),
        Producto(nombre='Top Teardrop Vibe', precio=18.00, stock=12, categoria_id=cat_ofertas.id),
        Producto(nombre='Blusa Lace Romance', precio=19.00, stock=12, categoria_id=cat_ofertas.id),
        Producto(nombre='Body Wild Print', precio=20.00, stock=12, categoria_id=cat_ofertas.id),
        Producto(nombre='Blusa One Shoulder Glow', precio=18.00, stock=15, categoria_id=cat_ofertas.id),
        Producto(nombre='Blusa Square Elegance', precio=19.00, stock=15, categoria_id=cat_ofertas.id)
    ]

    db.session.add_all(productos)

    # Usuarios
    admin = Usuario(nombre='Administrador', email='admin@tienda.com', rol='admin')
    admin.set_password('admin123')

    cliente = Usuario(nombre='Juan Pérez', email='juan@email.com', rol='cliente')
    cliente.set_password('cliente123')

    db.session.add_all([admin, cliente])
    db.session.commit()

    print("✅ Datos de prueba insertados correctamente")