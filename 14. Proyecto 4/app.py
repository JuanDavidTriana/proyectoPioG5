def pedirNotas():
    notas = []
    for i in range(3):
        while True:
            nota = float(input(f"Ingrese la nota {i+1}: "))
            if 0 <= nota <= 5:
                notas.append(nota)
                break
            else:
                print("Nota no valida. Debe estar entre 0 y 5")
    return notas



def calcularPromedio(notas):
    return sum(notas) / len(notas)

notas = pedirNotas()
promedio = calcularPromedio(notas)
print(f"El promedio es: {promedio:.2f}")
