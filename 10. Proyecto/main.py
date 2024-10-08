import os  # Importa el módulo os para interactuar con el sistema operativo

# Lista de productos disponibles, cada producto es un diccionario con nombre, precio y cantidad
productos = [
    {"nombre": "Anillo de diamante", "precio": 1000, "cantidad": 5},
    {"nombre": "Anillo de cuarzo", "precio": 20, "cantidad": 8},
    {"nombre": "Anillo de plata", "precio": 200, "cantidad": 12},
    {"nombre": "Anillo de oro", "precio": 400, "cantidad": 5}
]

carrito = []  # Inicializa una lista vacía para el carrito de compras

def limpiar_pantalla():
    # Limpia la pantalla según el sistema operativo
    if os.name == "nt":
        os.system("cls")  # Comando para limpiar en Windows
    else:
        os.system("clear")  # Comando para limpiar en Linux o Mac
        
def mostrar_productos():
    # Limpia la pantalla y muestra el menú de productos
    limpiar_pantalla()
    print(" -----------------------/Menú de productos-----------------------------------")
    for i, producto in enumerate(productos):
        # Muestra cada producto con su índice, nombre , precio y cantidad
        print(f"{i+1}. {producto['nombre']} - precio ${producto['precio']} - cantidad {producto['cantidad']}")

def agregar_al_carrito():
    # Limpia la pantalla y muestra los productos disponibles
    limpiar_pantalla()
    mostrar_productos()
    try:
        # Solicita al usuario seleccionar un producto para agregar al carrito
        opcion = int(input("Introduce el producto que desees agregar al carrito: "))
        if 1 <= opcion <= len(productos):
            # Solicita la cantidad que desea comprar
            cantidad = int(input("Ingrese la cantidad de productos que desees comprar: "))
            producto = productos[opcion - 1]  # Selecciona el producto correspondiente
            if cantidad > producto["cantidad"]:
                print("No hay suficientes existencias en stock")  # Verifica si hay suficiente stock
            else:
                # Reduce la cantidad en stock y añade el producto al carrito
                productos[opcion - 1]['cantidad'] -= cantidad
                carrito.append({"nombre": producto["nombre"], "precio": producto['precio'], "cantidad": cantidad})
                print(f"Felicidades, has añadido {cantidad} {producto['nombre']} exitosamente")  # Confirma la acción
    except Exception as e:
        print("Se ha presentado un error", e)  # Manejo de excepciones

def mostrar_carrito():
    # Limpia la pantalla y muestra el contenido del carrito
    limpiar_pantalla()
    if carrito:
        print("Carrito de compras.")
        for i, item in enumerate(carrito, 1):
            # Muestra cada artículo en el carrito con su nombre, precio y cantidad
            print(f"{i}. Producto: {item['nombre']} - ${item['precio']} - cantidad: {item['cantidad']}")
    else:
        print("El carrito está vacío")  # Mensaje si el carrito está vacío

def calcular_total():
    # Calcula y muestra el total de la compra
    total = sum(item["precio"] * item["cantidad"] for item in carrito)  # Suma el precio total de los artículos
    print(f"El total a pagar es ${total}")

def finalizar_compra():
    # Limpia la pantalla y muestra el carrito antes de finalizar la compra
    limpiar_pantalla()
    mostrar_carrito()
    if carrito:
        calcular_total()  # Calcula el total
        confirmar = input("¿Desea finalizar la compra (s/n)? ")  # Solicita confirmación al usuario

        if confirmar.lower() == "s":
            carrito.clear()  # Limpia el carrito si la compra se confirma
            print("Compra finalizada exitosamente")
        else:
            print("Compra cancelada")
    else:
        print("No hay productos en el carrito")  # Mensaje si no hay productos para comprar

def main():
    while True: 
        limpiar_pantalla()  # Limpia la pantalla en cada iteración
        print(" -----------------------Menú Joyería-----------------------------------------")
        print("1- Mostrar productos disponibles")
        print("2- Añadir productos al carrito")
        print("3- Mostrar carrito")
        print("4- Finalizar compra (pagar)")
        print("5- Salir de la compra")
        
        try:
            # Diccionario que asigna las opciones del menú a las funciones correspondientes
            opciones = {
                1: mostrar_productos,
                2: agregar_al_carrito,
                3: mostrar_carrito,
                4: finalizar_compra,
            }
        

            selecion = int(input("Ingrese opción: "))  # Solicita al usuario que elija una opción

            if selecion in opciones:
                opciones[selecion]()  # Llama a la función correspondiente
                input("Presione Enter para continuar.......")  # Pausa para continuar
            elif selecion == 5:
                break  # Sale del bucle y termina el programa

        except ValueError:
            print("Entrada inválida, por favor ingrese un número")  # Manejo de excepciones para entradas no numéricas
            input("Presione Enter para continuar.......")
        except Exception:
            print("Se ha presentado un error")  # Manejo de excepciones generales
            input("Presione Enter para continuar.......")

main()  # Llama a la función principal para ejecutar el programa