'''1.	Crear una calculadora con un diccionario'''

def suma(x,y):
    return x+y

def resta(x,y):
    return x-y

def multiplicacion(x,y):
    return x*y

def division(x,y):
    if y != 0:
        return x/y
    else:
        return "Error: Division por cero"

def exponente(x,y):
    return x**y # x elevedo a la potencia y

def menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Divicion")
    print("5. Exponente")
    print("6. Salir")

#Diccionario de operaciones
operaciones = {
    1: suma,
    2: resta,
    3: multiplicacion,
    4: division,
    5: exponente
}

#Programa principal
while True:
    menu() #Muesta el menu
    opcion= int(input("Seleciona una operacion: "))
    
    if opcion in operaciones:
        
        numero1 = float(input("Ingrese el primer numero: "))
        numero2 = float(input("Ingrese el primer numero: "))
        
        resultado = operaciones[opcion](numero1,numero2)
        
        print(f"El resultado es: {resultado}")
        
    elif opcion == 6:
        print("Saliendo...")
        break
    else:
        print("Error: Opcion no valida.... ")