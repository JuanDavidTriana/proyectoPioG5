def generar_tabla_multiplicar(numero, hasta=10):
    for i in range(1, hasta + 1):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))
generar_tabla_multiplicar(numero)
