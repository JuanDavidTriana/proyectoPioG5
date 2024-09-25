def agregar_producto(carrito, producto, precio):
    carrito.append({"producto": producto, "precio": precio}) 

car = []  

while True:
    print("\n1. Agregar")
    print("2. Ver")
    print("3. Total")
    print("4. Salir")
    opt = input("Elige: ")
    
    if opt == "1":
        prod = input("Nombre: ")
        precio = float(input("Precio: "))  
        agregar_producto(car, prod, precio) 
    elif opt == "2":
        if len(car) > 0:  
            for i in range(len(car)):
                print("Producto: " + car[i]['producto'] + ", Precio: " + str(car[i]['precio']))  # Imprimir productos
        else:
            print("El carrito está vacío.")
    elif opt == "3":
        total = 0
        for i in range(len(car)):  
            total += car[i]['precio']
        print("Total: " + str(total)) 
    elif opt == "4":
        break
    else:
        print("Opción incorrecta") 
