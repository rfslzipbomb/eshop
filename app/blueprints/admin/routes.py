from flask import render_template
from . import admin_bp

@admin_bp.route('admin/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')
@admin_bp.route('admin/products')
def products():
    return render_template('admin/products.html')
@admin_bp.route('admin/orders')
def orders():
    return render_template('admin/orders.html')
@admin_bp.route('admin /users')
def users():
    return render_template('admin/users.html')