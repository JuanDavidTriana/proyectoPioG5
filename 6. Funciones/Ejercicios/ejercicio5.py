'''Sistema de Tienda con Carrito de Compras
Crea un sistema de tienda donde el usuario pueda agregar productos a un carrito, ver el carrito y calcular el total de la compra. Usa funciones para agregar productos, mostrar el carrito y calcular el total.
'''

def agregar_producto(carrito, producto, precio):
    carrito.append({"producto": producto, "precio": precio})
    print("Producto agregado exitosamente...") 

def mostar_carrito(carrito):
    if carrito:  
        for item in carrito:
            print(f"Producto: {item['producto']}, Precio: {item['precio']}")  
    else:
        print("El carrito está vacío.")

def calcular_total(carrito):
    return sum(item['precio'] for item in carrito)
    
def menu_opciones():
    print("-------------Menu-------------")
    print("\n1. Agregar producto")
    print("2. Ver carrito")
    print("3. Calcular total")
    print("4. Salir")

#Carrito 
carrito = []  

while True:
    menu_opciones()
    opcion = input("Elije una opcion: ")
    
    if opcion == "1":
        producto = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))  
        agregar_producto(carrito, producto, precio) 
        
    elif opcion == "2":
        mostar_carrito(carrito)
        
    elif opcion == "3":
        total = calcular_total(carrito)
        print(f"Total del carrito es de : ${total}")   
        
    elif opcion == "4":
        print("Saliendo....")
        break
    else:
        print("Opción incorrecta") 
