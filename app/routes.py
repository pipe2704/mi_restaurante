from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Comida, Pedido

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/menu')
def menu():
    comidas = Comida.query.all()
    return render_template('menu.html', comidas=comidas)

@bp.route('/menu/add', methods=['GET', 'POST'])
def add_comida():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        nueva_comida = Comida(nombre=nombre, precio=precio)
        db.session.add(nueva_comida)
        db.session.commit()
        return redirect(url_for('main.menu'))
    return render_template('add_comida.html')

@bp.route('/menu/delete/<int:id>')
def delete_comida(id):
    comida = Comida.query.get(id)
    db.session.delete(comida)
    db.session.commit()
    return redirect(url_for('main.menu'))

@bp.route('/pedidos')
def pedidos():
    pedidos = Pedido.query.all()
    return render_template('pedidos.html', pedidos=pedidos)

@bp.route('/pedidos/add', methods=['GET', 'POST'])
def add_pedido():
    if request.method == 'POST':
        mesa = request.form['mesa']
        comidas_ids = request.form.getlist('comidas')
        comidas = Comida.query.filter(Comida.id.in_(comidas_ids)).all()
        total = sum([comida.precio for comida in comidas])
        nuevo_pedido = Pedido(mesa=mesa, total=total, comidas=comidas)
        db.session.add(nuevo_pedido)
        db.session.commit()
        return redirect(url_for('main.pedidos'))
    comidas = Comida.query.all()
    return render_template('add_pedido.html', comidas=comidas)

@bp.route('/pedidos/delete/<int:id>')
def delete_pedido(id):
    pedido = Pedido.query.get(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for('main.pedidos'))
