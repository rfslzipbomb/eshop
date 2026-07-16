import os
from decimal import Decimal

from flask import current_app, flash, redirect, render_template, request, url_for
from flask_login import login_required
from werkzeug.utils import secure_filename

from app import db
from app.models import Categoria, Pedido, Producto, Usuario

from . import admin_bp
from .decorators import admin_requerido


def save_product_image(uploaded_file, upload_folder):
    if uploaded_file is None or uploaded_file.filename == '':
        return None

    filename = secure_filename(uploaded_file.filename)
    if not filename:
        return None

    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, filename)
    uploaded_file.save(file_path)
    return filename


@admin_bp.route('/dashboard')
@login_required
@admin_requerido
def dashboard():
    productos = Producto.query.order_by(Producto.id.desc()).all()
    categorias = Categoria.query.order_by(Categoria.id.asc()).all()
    clientes = Usuario.query.filter(Usuario.rol != 'admin').order_by(Usuario.id.desc()).all()
    pedidos = Pedido.query.order_by(Pedido.fecha.desc()).all()

    return render_template(
        'admin/dashboard.html',
        productos=productos,
        categorias=categorias,
        clientes=clientes,
        pedidos=pedidos,
    )


@admin_bp.route('/producto/nuevo', methods=['GET', 'POST'])
@login_required
@admin_requerido
def crear_producto():
    categorias = Categoria.query.order_by(Categoria.nombre.asc()).all()

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        descripcion = request.form.get('descripcion', '').strip()
        precio_texto = request.form.get('precio', '').strip()
        stock_texto = request.form.get('stock', '0').strip()
        categoria_id = request.form.get('categoria_id', type=int)
        activo = request.form.get('activo') == 'on'
        uploaded_file = request.files.get('imagen')

        if not nombre or not categoria_id:
            flash('El nombre y la categoría son obligatorios.', 'danger')
            return render_template('admin/crear_producto.html', categorias=categorias)

        try:
            precio = Decimal(precio_texto or '0')
            stock = int(stock_texto or 0)
        except (ValueError, ArithmeticError):
            flash('El precio y el stock deben ser valores válidos.', 'danger')
            return render_template('admin/crear_producto.html', categorias=categorias)

        producto = Producto(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            activo=activo,
            categoria_id=categoria_id,
        )

        filename = save_product_image(uploaded_file, current_app.config['UPLOAD_FOLDER'])
        if filename:
            producto.imagen = filename

        db.session.add(producto)
        db.session.commit()
        flash('Producto creado con éxito.', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/crear_producto.html', categorias=categorias)


@admin_bp.route('/producto/<int:id>/editar', methods=['GET', 'POST'])
@login_required
@admin_requerido
def editar_producto(id):
    producto = Producto.query.get_or_404(id)
    categorias = Categoria.query.order_by(Categoria.nombre.asc()).all()

    if request.method == 'POST':
        producto.nombre = request.form.get('nombre', '').strip()
        producto.descripcion = request.form.get('descripcion', '').strip()
        producto.activo = request.form.get('activo') == 'on'
        producto.categoria_id = request.form.get('categoria_id', type=int) or producto.categoria_id

        try:
            producto.precio = Decimal(request.form.get('precio', '').strip() or '0')
            producto.stock = int(request.form.get('stock', '0').strip() or 0)
        except (ValueError, ArithmeticError):
            flash('El precio y el stock deben ser valores válidos.', 'danger')
            return render_template('admin/crear_producto.html', producto=producto, categorias=categorias)

        uploaded_file = request.files.get('imagen')
        if uploaded_file and uploaded_file.filename:
            filename = save_product_image(uploaded_file, current_app.config['UPLOAD_FOLDER'])
            if filename:
                producto.imagen = filename

        db.session.commit()
        flash('Producto actualizado con éxito.', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/crear_producto.html', producto=producto, categorias=categorias)


@admin_bp.route('/producto/<int:id>/eliminar', methods=['POST'])
@login_required
@admin_requerido
def eliminar_producto(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado con éxito', 'success')
    return redirect(url_for('admin.dashboard'))


@admin_bp.route('/categoria/nueva', methods=['GET', 'POST'])
@login_required
@admin_requerido
def crear_categoria():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        descripcion = request.form.get('descripcion', '').strip()

        if not nombre:
            flash('El nombre de la categoría es obligatorio.', 'danger')
            return render_template('admin/crear_categoria.html')

        categoria = Categoria(nombre=nombre, descripcion=descripcion, activa=True)
        db.session.add(categoria)
        db.session.commit()
        flash('Categoría creada con éxito.', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/crear_categoria.html')


@admin_bp.route('/categoria/<int:id>/editar', methods=['GET', 'POST'])
@login_required
@admin_requerido
def editar_categoria(id):
    categoria = Categoria.query.get_or_404(id)

    if request.method == 'POST':
        categoria.nombre = request.form.get('nombre', '').strip()
        categoria.descripcion = request.form.get('descripcion', '').strip()
        categoria.activa = request.form.get('activa') == 'on'
        db.session.commit()
        flash('Categoría actualizada con éxito.', 'success')
        return redirect(url_for('admin.dashboard'))

    return render_template('admin/crear_categoria.html', categoria=categoria)


@admin_bp.route('/categoria/<int:id>/eliminar', methods=['POST'])
@login_required
@admin_requerido
def eliminar_categoria(id):
    categoria = Categoria.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    flash('Categoría eliminada con éxito', 'success')
    return redirect(url_for('admin.dashboard'))


@admin_bp.route('/cliente/<int:id>/toggle', methods=['POST'])
@login_required
@admin_requerido
def toggle_estado_cliente(id):
    cliente = Usuario.query.get_or_404(id)
    cliente.activo = not cliente.activo
    db.session.commit()
    flash('Estado del cliente actualizado', 'info')
    return redirect(url_for('admin.dashboard'))


@admin_bp.route('/pedido/<int:id>/estado', methods=['POST'])
@login_required
@admin_requerido
def actualizar_estado_pedido(id):
    pedido = Pedido.query.get_or_404(id)
    nuevo_estado = request.form.get('nuevo_estado')
    if nuevo_estado:
        pedido.estado = nuevo_estado.lower()
        db.session.commit()
        flash(f'Estado del pedido #{id} actualizado a {nuevo_estado}', 'success')
    return redirect(url_for('admin.dashboard'))