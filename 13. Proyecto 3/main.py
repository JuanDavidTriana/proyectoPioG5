

from prettytable import PrettyTable

productos = [
    {"nombre": "Lapiz", "precio": 3500, "stock": 10},
    {"nombre": "Cuaderno", "precio": 18000, "stock": 20},
    {"nombre": "Papel", "precio": 6000, "stock": 15},
    {"nombre": "Boligrafo", "precio": 9000, "stock": 12},
    {"nombre": "Goma de Borrar", "precio": 1500, "stock": 25},
    {"nombre": "Tijeras", "precio": 12000, "stock": 10},
    {"nombre": "Pegamento", "precio": 5000, "stock": 18},
    {"nombre": "Marcador", "precio": 3000, "stock": 15},
]

carrito = []

def mostrar_productos(productos):
    table = PrettyTable()
    table.field_names = ["Indice", "Nombre", "Precio", "Stock"]
    for i, producto in enumerate(productos, start=1):
        table.add_row([i, producto["nombre"], producto["precio"], producto["stock"]])
    print(table)

def agregar_al_carrito(carrito, productos):
    mostrar_productos(productos)
    try:
        opcion = int(input("Introduce el producto que desees comprar: "))
        if 1 <= opcion <= len(productos):
            cantidad = int(input("Ingrese la cantidad de productos que desees comprar: "))
            producto = productos[opcion - 1]  # Selecciona el producto correspondiente
            if cantidad > producto["stock"]:
                print("No hay suficientes existencias en stock")
            else:
                # Reduce la cantidad en stock y a ade el producto al carrito
                productos[opcion - 1]['stock'] -= cantidad
                existe_en_carrito = False
                for item in carrito:
                    if item["nombre"] == producto["nombre"]:
                        item["stock"] += cantidad
                        existe_en_carrito = True
                        break
                if not existe_en_carrito:
                    carrito.append({"nombre": producto["nombre"], "precio": producto['precio'], "stock": cantidad})
                print(f"Felicidades, has anadido {cantidad} {producto['nombre']} exitosamente")
    except Exception as e:
        print("Se ha presentado un error", e)
    return carrito, productos
        

def mostrar_carrito(carrito):
    if not carrito:
        print("El carrito esta vacio")
    else:
        table = PrettyTable()
        table.field_names = ["Indice", "Producto", "Precio", "Cantidad"]
        for i, item in enumerate(carrito, start=1):
            table.add_row([i, item["nombre"], item["precio"], item["stock"]])
        print(table)
    return carrito

def eliminar_producto_del_carrito(carrito_de_compra, lista_de_productos):
    """Elimina un producto del carrito y actualiza el stock en la lista de productos."""
    mostrar_carrito(carrito_de_compra)
    try:
        indice_eliminar = int(input("Introduce el producto que desees eliminar del carrito: "))
        if 1 <= indice_eliminar <= len(carrito_de_compra):
            producto_eliminar = carrito_de_compra.pop(indice_eliminar - 1)
            for producto in lista_de_productos:
                if producto["nombre"] == producto_eliminar["nombre"]:
                    producto["stock"] += producto_eliminar["stock"]
                    print(f"Has eliminado {producto_eliminar['nombre']} del carrito")
                    break
        else:
            print("El producto no existe")
    except Exception as e:
        print("Se ha presentado un error", e)
    return carrito_de_compra, lista_de_productos

def mostar_total_carrito(carrito):
    total = 0
    for item in carrito:
        total += item["stock"] * item["precio"]
    print(f"Total: ${total}")
    return carrito

def cancelar_compra(carrito, productos):
    for item in carrito:
        for p in productos:
            if p["nombre"] == item["nombre"]:
                p["stock"] += item["stock"]
                break
    carrito = []
    print("Se ha cancelado la compra")
    return carrito, productos

def confirmar_pago(carrito):
    mostrar_carrito(carrito)
    mostar_total_carrito(carrito)
    opcion = input("Desea confirmar la compra? (s/n): ")
    if opcion.lower() == "s":
        return True
    else:
        return False

from datetime import datetime

def generar_recibo(carrito, total, medio_pago, cambio=0):
    now = datetime.now()
    print(f"Fecha: {now.strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 40)
    print("Recibo de compra")
    print("-" * 40)
    table = PrettyTable()
    table.field_names = ["Producto", "Precio", "Cantidad", "Subtotal"]
    for item in carrito:
        table.add_row([item["nombre"], item["precio"], item["stock"], item["precio"] * item["stock"]])
    table.add_row(["Total", "", "", total])
    print(table)
    table2 = PrettyTable()
    table2.field_names = ["Medio de pago", "Cambio"]
    if medio_pago == "Tarjeta":
        table2.add_row([medio_pago, ""])
    else:
        table2.add_row([medio_pago, cambio])
    print(table2)
    print("-" * 40)
    print("Gracias por su compra")
    print("-" * 40)
    
def pedir_pago(carrito):
    print("Introduce el medio de pago: \n1. Tarjeta\n2. Efectivo")
    try:
        opcion = int(input("Opcion: "))
        if opcion == 1:
            return "Tarjeta"
        elif opcion == 2:
            pago = int(input("Ingrese con cuanto va a pagar: "))
            total = 0
            for item in carrito:
                total += item["stock"] * item["precio"]
            if pago >= total:
                cambio = pago - total
                generar_recibo(carrito, total, "Efectivo", cambio)
                return "Efectivo", cambio
            else:
                print("No tiene suficiente dinero")
                return pedir_pago()
        else:
            print("Opcion no valida")
            return pedir_pago()
    except Exception as e:
        print("Se ha presentado un error", e)
        return pedir_pago()
    

def menu(carrito, productos):
    """
    Muestra el men  principal del cajero y permite al usuario interactuar
    para agregar productos al carrito, eliminarlos, mostrar el carrito, pagar
    y cancelar la compra. Si el usuario selecciona pagar, se le solicita el
    medio de pago y se muestra el recibo de la compra. Si el usuario selecciona
    cancelar la compra, se cancela la compra y se vuelve al men  principal.

    Parameters
    ----------
    carrito : list
        Carrito de compras actual
    productos : list
        Lista de productos disponibles

    Returns
    -------
    carrito, productos
        Carrito y productos actualizados
    """
    while True:
        print("Bienvenido al cajero de la papeler a")
        print("-------------------------------/Men  de productos-----------------------------------")
        print("1. Ver productos")
        print("2. Agregar al carrito")
        print("3. Eliminar del carrito")
        print("4. Mostrar carrito")
        print("5. Pagar")
        print("6. Cancelar")
        print("7. Salir")
        
