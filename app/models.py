from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Tabla intermedia para la relación muchos a muchos entre Pedido y Comida
pedido_comida = db.Table('pedido_comida',
    db.Column('pedido_id', db.Integer, db.ForeignKey('pedido.id'), primary_key=True),
    db.Column('comida_id', db.Integer, db.ForeignKey('comida.id'), primary_key=True)
)

class Comida(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mesa = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False, default=0.0)
    comidas = db.relationship('Comida', secondary=pedido_comida, lazy='subquery',
                              backref=db.backref('pedidos', lazy=True))
