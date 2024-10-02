while True:
    try:
        caluladora = int(input("Ingrese el divisor para el numero 5:"))
        divir = 5/caluladora
        print(divir)
        break
    except ZeroDivisionError:
        print("No se puede divir entre 0")
    except ValueError:
        print("Error valor no valido")