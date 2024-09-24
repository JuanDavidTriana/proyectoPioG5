salario = float(input("Introduce su salario anual: "))

if salario > 0:
    if salario > 50000:
        if salario > 100000:
            print("El inpuesto es del 30%")
        else:
            print("El impuesto es del 20%")
    else: 
        print("No pagan impuesto")
else:
    print("Salario no valido")