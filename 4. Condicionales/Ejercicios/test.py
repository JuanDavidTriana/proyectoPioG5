try:
    numero = int(input("Valor de dividor: "))

    operacion = 2/numero
    print(operacion)
except ZeroDivisionError:
    print("No se puede dividir por 0")
except ValueError:
    print("Valor no valido tiene que ser un numero entero")
except:
    print("Error")