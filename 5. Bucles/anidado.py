import os

while True:
    print("----------- Menu -----------" )
    print("1. Pasta")
    print("2. Carne")
    print("3. Pollo")
    print("4. Salir")
    opcion = int(input("Elije una opcion: "))
    
    if opcion == 1:
        print("Prepara pastas")
        input("Enter para continua......")
        os.system("cls") # clear Linux o mac
    elif opcion == 2:
        print("Preparar Carne")
        input("Enter para continua......")
        os.system("cls")
    elif opcion == 3:
        print("Prepara Pollo")
        input("Enter para continua......")
        os.system("cls")
    elif opcion == 4:
        print("Saliendo...")
        break
    else:
        print("Opcion no valida")
        input("Enter para continua......")
        os.system("cls")