from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash



class Usuario(db.Model):
    __tablename__ = 'usuarios'

    usuario_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    rol = db.Column(db.String(20), default='usuario')  # Campo para el rol del usuario

    pedidos = db.relationship('Pedido', backref='cliente', lazy=True, foreign_keys='Pedido.usuario_id')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_admin(self):
        # Aquí puedes definir la lógica para determinar si el usuario es administrador
        # Por ejemplo, podrías tener un campo adicional en la tabla de usuarios que indique si es admin
        return self.rol == "admin"
    
    def __repr__(self):
        return f'<Usuario {self.email}> | {self.rol}'
    