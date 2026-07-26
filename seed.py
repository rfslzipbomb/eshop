import os
import re
import sys

# Asegura que Python encuentre la carpeta app
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db
from app.models import Usuario, Categoria, Producto

app = create_app()


def _normalize_name(value):
    value = value.lower()
    replacements = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ñ': 'n',
    }
    value = ''.join(replacements.get(char, char) for char in value)
    return re.sub(r'[^a-z0-9]+', '_', value).strip('_')


def get_product_image_filename(nombre):
    mapping = {
        'top_bliss': 'top_bliss.PNG',
        'top_linna': 'top_linna.PNG',
        'top_perla': 'top_perla.PNG',
        'top_glow_aqua': 'top_glow_aqua.PNG',
        'dress_shine': 'azimetrica.PNG',
        'top_glow': 'top_glow.PNG',
        'top_gala': 'top_gala.PNG',
        'top_bliss_white': 'top_bliss_white.PNG',
        'top_perla_pink': 'top_perla_pink.PNG',
        'top_glow_pink': 'top_glow_pink.PNG',
        'top_nova_black': 'top_nova_black.PNG',
        'top_noir': 'top_glow.PNG',
        'top_belle': 'top_belle.PNG',
        'top_linna_black': 'top_linna_black.PNG',
        'top_glow_brown': 'top_glow_brown.PNG',
        'top_gala_black': 'top_gala.PNG',
        'top_nova_wine': 'top_nova_wine.PNG',
        'top_velvet': 'top_velvet.PNG',
        'top_gala_aqua': 'top_gala_aqua.PNG',
        'top_nova_white': 'top_nova_white.PNG',
        'onyx_jacket': 'onyx_jacket.PNG',
        'chaqueta_biker_cuerina_efecto_piel': 'biker.jfif',
        'blazer_oversize_elegante': 'blazer_overzice.jfif',
        'chaqueta_cropped_trench': 'chaqueta_cropper.jfif',
        'chaqueta_denim_semicrop': 'chaqueta_denim.jfif',
        'bomber_jacket_satinada': 'bomber.jfif',
        'vestido_sparkle_glitz': 'Vestido_Sparkle_Glitz.jfif',
        'vestido_silk_romance': 'Vestido_Silk_Romance.jpg',
        'vestido_bodycon_chic': 'Vestido_Bodycon_Chic.jfif',
        'vestido_cozy_long_sleeve': 'Vestido_Cozy_Long_Sleeve.jfif',
        'vestido_night_aura': 'vestido.jpeg',
        'blusa_asymmetric_muse': 'un_hombro.PNG',
        'top_teardrop_vibe': 'gota.PNG',
        'blusa_lace_romance': 'randa.PNG',
        'body_wild_print': 'body.PNG',
        'blusa_one_shoulder_glow': 'un_hombro.PNG',
        'blusa_square_elegance': 'cuello_cuadrado.PNG',
    }
    return mapping.get(_normalize_name(nombre))


def seed_data():
    with app.app_context():
        # 0. Limpiar datos existentes (opcional pero recomendado)
        db.session.query(Producto).delete()
        db.session.query(Categoria).delete()
        db.session.query(Usuario).delete()
        db.session.commit()

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
            Producto(nombre='Top Bliss', precio=19.00, stock=15, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Bliss')),
            Producto(nombre='Top Linna', precio=19.00, stock=15, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Linna')),
            Producto(nombre='Top Perla', precio=18.00, stock=15, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Perla')),
            Producto(nombre='Top Glow Aqua', precio=17.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Glow Aqua')),
            Producto(nombre='Dress Shine', precio=18.00, stock=10, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Dress Shine')),
            Producto(nombre='Top Glow', precio=17.00, stock=15, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Glow')),
            Producto(nombre='Top Gala', precio=19.00, stock=15, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Gala')),
            Producto(nombre='Top Bliss White', precio=19.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Bliss White')),
            Producto(nombre='Top Perla Pink', precio=18.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Perla Pink')),
            Producto(nombre='Top Glow Pink', precio=17.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Glow Pink')),
            Producto(nombre='Top Nova Black', precio=19.00, stock=15, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Nova Black')),
            Producto(nombre='Top Noir', precio=18.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Noir')),
            Producto(nombre='Top Belle', precio=19.00, stock=15, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Belle')),
            Producto(nombre='Top Linna Black', precio=19.00, stock=15, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Linna Black')),
            Producto(nombre='Top Glow Brown', precio=17.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Glow Brown')),
            Producto(nombre='Top Gala Black', precio=19.00, stock=15, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Gala Black')),
            Producto(nombre='Top Nova Wine', precio=19.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Nova Wine')),
            Producto(nombre='Top Velvet', precio=17.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Velvet')),
            Producto(nombre='Top Gala Aqua', precio=19.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Gala Aqua')),
            Producto(nombre='Top Nova White', precio=19.00, stock=12, categoria_id=cat_blusas.id, imagen=get_product_image_filename('Top Nova White')),

            # --- CHAQUETAS ---
            Producto(nombre='Onyx Jacket', precio=30.00, stock=8, categoria_id=cat_chaquetas.id, imagen=get_product_image_filename('Onyx Jacket')),
            Producto(nombre='Chaqueta Biker Cuerina (Efecto Piel)', precio=35.00, stock=8, categoria_id=cat_chaquetas.id, imagen=get_product_image_filename('Chaqueta Biker Cuerina (Efecto Piel)')),
            Producto(nombre='Blazer Oversize Elegante', precio=32.00, stock=10, categoria_id=cat_chaquetas.id, imagen=get_product_image_filename('Blazer Oversize Elegante')),
            Producto(nombre='Chaqueta Cropped Trench', precio=28.00, stock=12, categoria_id=cat_chaquetas.id, imagen=get_product_image_filename('Chaqueta Cropped Trench')),
            Producto(nombre='Chaqueta Denim Semicrop', precio=26.00, stock=12, categoria_id=cat_chaquetas.id, imagen=get_product_image_filename('Chaqueta Denim Semicrop')),
            Producto(nombre='Bomber Jacket Satinada', precio=25.00, stock=10, categoria_id=cat_chaquetas.id, imagen=get_product_image_filename('Bomber Jacket Satinada')),

            # --- VESTIDOS ---
            Producto(nombre='Vestido Sparkle Glitz', precio=32.00, stock=8, categoria_id=cat_vestidos.id, imagen=get_product_image_filename('Vestido Sparkle Glitz')),
            Producto(nombre='Vestido Silk Romance', precio=28.00, stock=10, categoria_id=cat_vestidos.id, imagen=get_product_image_filename('Vestido Silk Romance')),
            Producto(nombre='Vestido Bodycon Chic', precio=24.00, stock=12, categoria_id=cat_vestidos.id, imagen=get_product_image_filename('Vestido Bodycon Chic')),
            Producto(nombre='Vestido Cozy Long Sleeve', precio=22.00, stock=12, categoria_id=cat_vestidos.id, imagen=get_product_image_filename('Vestido Cozy Long Sleeve')),
            Producto(nombre='Vestido Night Aura', precio=29.00, stock=10, categoria_id=cat_vestidos.id, imagen=get_product_image_filename('Vestido Night Aura')),

            # --- OFERTAS ---
            Producto(nombre='Blusa Asymmetric Muse', precio=19.00, stock=15, categoria_id=cat_ofertas.id, imagen=get_product_image_filename('Blusa Asymmetric Muse')),
            Producto(nombre='Top Teardrop Vibe', precio=18.00, stock=12, categoria_id=cat_ofertas.id, imagen=get_product_image_filename('Top Teardrop Vibe')),
            Producto(nombre='Blusa Lace Romance', precio=19.00, stock=12, categoria_id=cat_ofertas.id, imagen=get_product_image_filename('Blusa Lace Romance')),
            Producto(nombre='Body Wild Print', precio=20.00, stock=12, categoria_id=cat_ofertas.id, imagen=get_product_image_filename('Body Wild Print')),
            Producto(nombre='Blusa One Shoulder Glow', precio=18.00, stock=15, categoria_id=cat_ofertas.id, imagen=get_product_image_filename('Blusa One Shoulder Glow')),
            Producto(nombre='Blusa Square Elegance', precio=19.00, stock=15, categoria_id=cat_ofertas.id, imagen=get_product_image_filename('Blusa Square Elegance'))
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


if __name__ == '__main__':
    seed_data()
