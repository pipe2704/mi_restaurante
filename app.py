# Importar los módulos necesarios de Flask y render_template
from flask import Flask, render_template, request, redirect, url_for

# Crear una instancia de Flask
app = Flask(__name__)

# Lista para almacenar los pedidos (simulación)
pedidos = []

# Rutas existentes
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/hacer_pedido', methods=['GET', 'POST'])
def hacer_pedido():
    if request.method == 'POST':
        # Obtener datos del formulario
        cliente_nombre = request.form['clienteNombre']
        cliente_telefono = request.form['clienteTelefono']
        mesa_numero = request.form['mesaNumero']
        entradas = request.form.get('entradas')
        cantidad_entradas = int(request.form.get('cantidadEntradas', 0))
        platos_principales = request.form.get('platosPrincipales')
        cantidad_platos_principales = int(request.form.get('cantidadPlatosPrincipales', 0))
        bebidas = request.form.get('bebidas')
        cantidad_bebidas = int(request.form.get('cantidadBebidas', 0))
        postres = request.form.get('postres')
        cantidad_postres = int(request.form.get('cantidadPostres', 0))

        # Calcular total del pedido
        total = (precio_producto(entradas) * cantidad_entradas +
                 precio_producto(platos_principales) * cantidad_platos_principales +
                 precio_producto(bebidas) * cantidad_bebidas +
                 precio_producto(postres) * cantidad_postres)

        # Crear resumen del pedido
        resumen_html = f"<li class='list-group-item'><strong>Cliente:</strong> {cliente_nombre} <strong>Mesa:</strong> {mesa_numero}</li>"
        if cantidad_entradas > 0:
            resumen_html += f"<li class='list-group-item'>{cantidad_entradas}x {entradas}</li>"
        if cantidad_platos_principales > 0:
            resumen_html += f"<li class='list-group-item'>{cantidad_platos_principales}x {platos_principales}</li>"
        if cantidad_bebidas > 0:
            resumen_html += f"<li class='list-group-item'>{cantidad_bebidas}x {bebidas}</li>"
        if cantidad_postres > 0:
            resumen_html += f"<li class='list-group-item'>{cantidad_postres}x {postres}</li>"

        # Almacenar el pedido en la lista de pedidos (simulación)
        pedidos.append({
            'cliente': cliente_nombre,
            'mesa': mesa_numero,
            'total': total,
            'resumenHtml': resumen_html  # Ajustado para coincidir con el nombre en el template
        })

        return redirect(url_for('resumen_pedidos'))

    return render_template('hacer_pedido.html')

@app.route('/reservaciones')
def reservaciones():
    return render_template('reservaciones.html')

@app.route('/resumen_pedidos')
def resumen_pedidos():
    return render_template('resumen_pedidos.html', pedidos=pedidos)

# Función para obtener el precio de un producto seleccionado
def precio_producto(producto):
    if producto:
        return float(producto.split(' - ')[1].replace('$', ''))
    return 0.0

# Ejecutar la aplicación si se llama directamente
if __name__ == '__main__':
    app.run(debug=True)
